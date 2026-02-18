import requests
from backend.services.external_companymodel import ExternalCompanyModel 

APOLLO_API_KEY = "xzyn8EQODtSDovkwbTuDCw"
APOLLO_URL = "https://api.apollo.io/v1/organizations/enrich?api_key=XXX&domain=microsoft.com"

def fetch_company_from_apollo() -> list[ExternalCompanyModel]:
    """fetching company data from Apollo API"""
    payload = {
        "api_key": APOLLO_API_KEY,
        "page": 1,
        "per_page": 1
    }

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    
    try:
        response = requests.post(APOLLO_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
         raise RuntimeError(f"HTTP error occurred: {http_err.response.status_code}") from http_err
    except requests.exceptions.RequestException as req_err:
        raise RuntimeError("No se pudo conectar con el servidor de Apollo") from req_err
    
    data = response.json()
    people = data.get("people", [])
    
    companies: list[ExternalCompanyModel] = []

    for person in people:
        org = person.get("organization", {})
        companies.append(
            ExternalCompanyModel(
                name=org.get("name"),
                domain=org.get("website_url"),
                industry=org.get("industry"),
                revenue=org.get("annual_revenue"),
                technologies=org.get("technologies", [])
            )
        )

    return companies