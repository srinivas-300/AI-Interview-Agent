import requests
import os
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("tavily_service")

def tavily_search(query: str) -> str:

    query = query[:380]
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}

    api_key = os.getenv("TAVILY_API_KEY")
    payload = {
        "api_key": api_key,
        "query": query,
        "max_results": 10,
        "include_answer": True,
        "include_raw_content": True
    }

    log.info(f"Sending Tavily payload: {payload}")

    try:
        resp = requests.post(url, json=payload, headers=headers)
        data = resp.json()
    except Exception as e:
        log.error(f"Tavily response not JSON. Raw: {resp.text}")
        return "[ERROR] Tavily response not JSON"

    if "results" not in data:
        log.error(f"Tavily ERROR response: {data}")
        return f"[ERROR] Unexpected Tavily response: {data}"

    log.info("Tavily search successful.")
    return "\n".join([r.get("content", "") for r in data["results"]])
