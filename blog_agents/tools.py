"""Small set of tools for agents: mock web search, fetch_webpage, storage."""
from typing import Dict, Any, List
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "blog_data")
os.makedirs(DATA_DIR, exist_ok=True)


def save_artifact(name: str, content: str) -> str:
    path = os.path.join(DATA_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


# Mock / simple web_search - replace with an actual web search implementation
def web_search(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    # For now return a structured placeholder. Tests and examples use fixtures.
    return [
        {"title": f"Result {i} for {query}", "url": f"https://example.com/{query}/{i}", "snippet": "Short snippet"}
        for i in range(1, limit + 1)
    ]


# Mock fetch_webpage - replace with a fetcher that returns HTML or parsed content
def fetch_webpage(url: str) -> Dict[str, Any]:
    return {"url": url, "text": f"Mocked content for {url}", "status": 200}


def save_json(name: str, data: Dict[str, Any]) -> str:
    path = os.path.join(DATA_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return path
