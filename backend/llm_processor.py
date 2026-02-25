import os, json, requests
from datetime import datetime

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

PROMPT = """
You are a monetization strategist.

Based on this data:
{data}

Generate 3 monetization ideas in JSON array format:
[
  {{
    "title": "",
    "strategy": "",
    "execution_steps": [],
    "difficulty": "",
    "risks": []
  }}
]
"""

def run_llm():
    with open("data/raw.json") as f:
        raw = f.read()

    payload = {"inputs": PROMPT.format(data=raw)}
    r = requests.post(HF_API_URL, headers=HEADERS, json=payload, timeout=60)
    result = r.json()[0]["generated_text"]

    json_start = result.find("[")
    ideas = json.loads(result[json_start:])

    out = {
        "generated_at": datetime.utcnow().isoformat(),
        "ideas": ideas
    }

    with open("data/ideas.json", "w") as f:
        json.dump(out, f, indent=2)

if __name__ == "__main__":
    run_llm()