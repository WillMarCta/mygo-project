from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models.models import Company
from backend.postgresqldb.db import get_db
from backend.services.apollo_services import fetch_company_from_apollo as call_external_api
from backend.services.scoring import calculate_affinity_score

router = APIRouter(prefix="/Ingestion", tags=["Ingestion"])

@router.post("/save", response_model=None)
async def sync_company_data(domain: str, db: Session = Depends(get_db)):
    try:
        external_data = fetch_company_from_apollo(domain)
        company = db.query(Company).filter(Company.domain == domain).first()

        score = calculate_affinity_score(external_data)
    
    if company:
        # ACTUALIZAR: Si existe, solo cambiamos los valores viejos por los nuevos
        company.name = external_data.name
        company.revenue = external_data.revenue
        print(f"🔄 Actualizando datos de: {domain}")
    else:
        # CREAR: Si es nuevo, instanciamos uno nuevo
        company = Company(
            name=external_data.name,
            domain=external_data.domain,
            revenue=external_data.revenue,
            industry=external_data.industry,
            technologies=external_data.technologies
        )
        db.add(company)
        print(f"✨ Creando nuevo registro para: {domain}")

    db.commit()
    db.refresh(company)
    return company



