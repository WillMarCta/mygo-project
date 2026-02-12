import requests
from backend.services.external_companymodel import ExternalCompany

APOLLO_API_KEY = "xzyn8EQODtSDovkwbTuDCw"
APOLLO_URL = "https://api.apollo.io/api/v1/mixed_people/api_search"

def fetch_company_from_apollo(domain: str) -> ExternalCompany:
    """fetching company data from Apollo API"""
    payload = {
        "api_key": APOLLO_API_KEY,
        "q_organization_domains_list": [domain], # Lista requerida por Apollo
        "person_titles": ["IT Manager", "VP of IT", "IT Director"],
        "currently_using_any_of_technology_uids": ["sap", "sap_s4_hana", "sap_ewm"],
        "person_seniorities": ["vp", "director", "manager"],
        "organization_revenue_min": 500000000, # ICP: $500M+    
        "page": 1,
        "per_page": 1
    }

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    
    response = requests.post(APOLLO_URL, json=payload, headers=headers, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Error Apollo API: {response.text}")
            
    data = response.json()
    people = data.get("people", []) # El endpoint devuelve 'people'
    
    if not people:
        raise ValueError(f"No prospect found for {domain} matching ICP criteria.")
    
    # SOLUCIÓN AL ERROR: Definir org_data extrayendo la info del primer lead
    org_data = people[0].get("organization", {}) #
    
    return ExternalCompany(
        name=org_data.get("name"),
        domain=domain,
        industry=None, # Search solo devuelve 'has_industry' (bool)
        revenue=None,  # Search solo devuelve 'has_revenue' (bool)
        technologies=[] 
    )