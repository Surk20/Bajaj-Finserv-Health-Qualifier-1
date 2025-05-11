import requests
import json

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

payload = json.dumps({
  "name": "Surbhi Kudiwal",
  "regNo": "0827CI221132",
  "email": "surbhikudiwal220319@acropolis.in"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
