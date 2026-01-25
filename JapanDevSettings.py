TOLERABLE_LANGUAGE_LEVEL = [
    "japanese_level_not_required",
    "japanese_level_conversational"
]

TOLERABLE_EXPERIENCE_LEVEL = [
    "seniority_level_junior",
    "seniority_level_mid_level"
]

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Authorization": "Bearer 3838486cea4344beaef2c4c5979be249fc5736ea4aab99fab193b5e7f540ffae",
    "X-Meilisearch-Client": "Meilisearch instant-meilisearch (v0.20.1) ; Meilisearch JavaScript (v0.42.0)"
}

def _main_payload(offset):
    main_payload = {
        "queries": [
            {
                "indexUid": "Job_production",
                "q": "",
                "limit": 21,
                "offset": offset,
                "facets": ["location", "job_type_names"],
                "attributesToHighlight":["*"]
            }
        ]
    }
    return main_payload

def _test_payload():
    payload = {
        "queries": [
            {
                "indexUid": "Job_production",
                "q": "",
                "limit": 1, 
                "facets": [
                    "seniority_level", 
                    "japanese_level_enum", 
                    "candidate_location", 
                    "sponsors_visas",
                    "company_is_startup"
                ]
            }
        ]
    }
    return payload