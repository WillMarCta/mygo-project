from sqlalchemy import Column, Integer, String, BigInteger, DateTime, ARRAY
from sqlalchemy.sql import func
from backend.postgresqldb.db import Base


 
class Company(Base):
    __tablename__ = "companies"

    id=Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    domain = Column(String(255), unique=True, nullable=False)
    industry = Column(String(255))
    revenue = Column(BigInteger) # USD
    technologies = Column(ARRAY(String))
    icp_score = Column(Integer) # 0-100
    bant_score = Column(Integer)
    affinity_score = Column(Integer)
    hq_location = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())