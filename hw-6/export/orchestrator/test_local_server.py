import requests
import json

url = "http://127.0.0.1:8000/v1/chat/completions"
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Hola, ¿puedes responder este mensaje?"}
    ],
    "temperature": 0.0,
    "stream": False
}

response = requests.post(url, json=payload)

print(f"Status code: {response.status_code}")
try:
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
except Exception:
    print(response.text) 