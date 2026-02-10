from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL ="postgresql+psycopg://postgres:123456@localhost:5432/mygo_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



try: 
    with engine.connect() as conn: 
        print("Conexión exitosa a PostgreSQL") 
except Exception as e:
    print("Error:", e)