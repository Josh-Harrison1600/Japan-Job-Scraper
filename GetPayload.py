import requests
import json
import JapanDevSettings
api_url = "https://meili.japan-dev.com/multi-search"

payload = JapanDevSettings._test_payload()

response = requests.post(api_url, json=payload, headers=JapanDevSettings.HEADERS)
data = response.json()
print(json.dumps(data, indent=4))