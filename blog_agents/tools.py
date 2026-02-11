"""Small set of tools for agents: mock web search, fetch_webpage, storage, Vale linting."""
from typing import Dict, Any, List, Optional
import json
import os
import subprocess
import re

BLOGS_ROOT = os.path.join(os.path.dirname(__file__), "..", "blogs")
os.makedirs(BLOGS_ROOT, exist_ok=True)

_current_blog_dir: Optional[str] = None


def set_blog_context(blog_name: str) -> str:
    """Set the current blog context. Creates the blog folder and blog_data subfolder."""
    global _current_blog_dir
    slug = slugify(blog_name)
    _current_blog_dir = os.path.join(BLOGS_ROOT, slug)
    os.makedirs(os.path.join(_current_blog_dir, "blog_data"), exist_ok=True)
    return _current_blog_dir


def get_blog_dir() -> str:
    """Get current blog directory. Raises if not set."""
    if _current_blog_dir is None:
        raise RuntimeError("Blog context not set. Call set_blog_context(blog_name) first.")
    return _current_blog_dir


def get_data_dir() -> str:
    """Get blog_data directory for current blog."""
    return os.path.join(get_blog_dir(), "blog_data")


def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    return slug[:50]


def save_artifact(name: str, content: str) -> str:
    """Save artifact to current blog's blog_data folder."""
    path = os.path.join(get_data_dir(), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def save_draft(name: str, content: str) -> str:
    """Save draft markdown to blog root (not blog_data)."""
    path = os.path.join(get_blog_dir(), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def web_search(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Mock web search - replace with actual API."""
    return [
        {"title": f"Result {i} for {query}", "url": f"https://example.com/{query}/{i}", "snippet": "Short snippet"}
        for i in range(1, limit + 1)
    ]


def fetch_webpage(url: str) -> Dict[str, Any]:
    """Mock fetch_webpage - replace with real fetcher."""
    return {"url": url, "text": f"Mocked content for {url}", "status": 200}


def save_json(name: str, data: Dict[str, Any]) -> str:
    """Save JSON to current blog's blog_data folder."""
    path = os.path.join(get_data_dir(), name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return path


def run_vale(file_path: str, config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Run Vale prose linter on a file.
    Returns dict with 'success', 'output', 'error_count', 'warning_count', 'suggestions'.
    """
    cmd = ["vale"]
    if config_path:
        cmd.extend(["--config", config_path])
    cmd.append(file_path)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        output = result.stdout + result.stderr
        
        errors = len(re.findall(r'\berror\b', output, re.IGNORECASE))
        warnings = len(re.findall(r'\bwarning\b', output, re.IGNORECASE))
        
        match = re.search(r'(\d+) errors?, (\d+) warnings? and (\d+) suggestions?', output)
        if match:
            errors, warnings, suggestions = int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            suggestions = 0
        
        return {
            "success": result.returncode == 0,
            "output": output,
            "error_count": errors,
            "warning_count": warnings,
            "suggestion_count": suggestions,
            "file": file_path
        }
    except FileNotFoundError:
        return {"success": False, "output": "Vale not installed. Run: brew install vale", "error_count": -1}
    except subprocess.TimeoutExpired:
        return {"success": False, "output": "Vale timed out", "error_count": -1}


def lint_draft(draft_name: str = "draft.md") -> Dict[str, Any]:
    """Run Vale on the current blog's draft."""
    draft_path = os.path.join(get_blog_dir(), draft_name)
    if not os.path.exists(draft_path):
        return {"success": False, "output": f"Draft not found: {draft_path}", "error_count": -1}
    
    config_path = os.path.join(BLOGS_ROOT, ".vale.ini")
    if not os.path.exists(config_path):
        config_path = None
    
    return run_vale(draft_path, config_path)
