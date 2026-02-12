def calculate_icp_score(company):
    """calculating the ICP score for a given company"""
    score = 0 

    #industry rules
    industry_weights = {
        "life sciences": 30,
        "Consumer Goods": 25,
        "manufacturing": 20,
        "Technology": 20,
    }

    score += industry_weights.get(company, 0)

    #reveue rules

    revenue_brackets = [
        (1_000_000_000, 40),
        (500_000_000, 30),
        (100_000_000, 20),
    ]

    for limit, points in revenue_brackets:
        if company.revenue and company.revenue >= limit:
            score += points
            break

    #technolofy rules
    tech_weights = {
        "SAP": 30,
        "Salesforce": 20,
        "HubSpot": 10,
        "SAP S/4HANA": 30,
        "SAP Central Finance": 20,
        "SAP ECC": 15,
        "SAP R/3": 10,
        "SAP EWM": 25,
        "SAP SCM": 20,
        "SAP APO": 15,
        "SAP FI/CO": 15,
        "SAP BPC": 10,
        "SAP Analytics Cloud": 10,
        "SAP PP": 10,
        "SAP SuccessFactors": 15,
    }

    if company.technologies:
        for tech in company.technologies:
            score += tech_weights.get(tech, 0)

    return score

def calculate_bant_score(company):
    """calculating the BANT score for a given company"""
    score = 0

    #budget rules
    if company.revenue:
        if company.revenue >= 500_000_000:
            score += 30
        elif company.revenue >= 100_000_000:
            score += 20

    #authority rules
    score += 20

    # Need (placeholder)
    score += 30

    # Timing (placeholder)
    score += 20

    return score

def calculate_affinity_score(icp_score, bant_score):
    """calculating the final affinity score based on ICP and BANT scores"""
    return int(icp_score * 0.6 + bant_score * 0.4)