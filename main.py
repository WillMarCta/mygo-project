from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from sqlalchemy import text
from backend.postgresqldb.db import engine
from backend.routers import leads_sync_router
from backend.routers.leads_sync_router import router 


@asynccontextmanager
async def lifespan(_: FastAPI):
    """testing database connection on startup"""
    print("🚀 Conectando a la base de datos...")
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Base de datos conectada exitosamente.")
    except Exception as e:
        print(f"❌ ERROR al conectar a la base de datos: {e}")
    
    yield

    print("🛑 Limpiando recursos antes de apagar...")

app = FastAPI(lifespan=lifespan)

app.include_router(leads_sync_router.router, tags=["Ingestion"])
