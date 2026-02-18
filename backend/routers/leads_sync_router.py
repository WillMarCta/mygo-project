from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models.models import Company
from backend.postgresqldb.db import get_db
from backend.services.apollo_services import fetch_company_from_apollo


router = APIRouter(prefix="/Ingestion", tags=["Ingestion"])

@router.post("/call_api_and_save_info", response_model=None)
async def sync_company_data(db:Session = Depends(get_db)):

    external_companies = fetch_company_from_apollo()

    for data in external_companies:
        new_company = Company(
            name=data.name,
            domain=data.domain,
            revenue=data.revenue,
            industry=data.industry,
            technologies=data.technologies
        )
        db.add(new_company)

    db.commit()
    return {"status": "ok", "saved": len(external_companies)}