from typing import Optional
from pydantic import BaseModel



class ExternalCompanyModel(BaseModel):
    name: Optional[str] = None
    domain: str
    industry: Optional[str] = None
    revenue: Optional[float] = 0.0
    technologies: list[str] = []
