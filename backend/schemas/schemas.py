from pydantic import BaseModel
from typing import List, Optional

class CompanyResponse(BaseModel):
    id: int
    name: str
    domain: str
    industry: Optional[str] = None
    revenue: Optional[int] = None
    technologies: Optional[List[str]] = None
    icp_score: Optional[int] = None
    bant_score: Optional[int] = None
    affinity_score: Optional[int] = None


class Config:
    from_attributes = True
    


