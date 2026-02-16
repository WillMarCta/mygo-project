from pydantic import BaseModel
class ExternalCompanyModel(BaseModel):

    name: str
    domain: str
    industry: str
    revenue: float
    technollogies: list[str]
