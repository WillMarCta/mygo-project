from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from sqlalchemy import text
from backend.postgresqldb.db import engine


# Esto se ejecuta UNA VEZ al iniciar el servidor
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