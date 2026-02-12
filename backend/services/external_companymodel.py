from pydantic import BaseModel

class ExternalCompany(BaseModel):

    name: str | None
    domain: str | None
    industry: str | None
    revenue: int | None
    technologies: list[str] | None