import pytest
import os
from blog_agents import tools

@pytest.fixture(autouse=True)
def mock_blog_context(tmp_path):
    """Automatically mock the blog context for all tests using pytest's tmp_path."""
    test_blog_dir = str(tmp_path / "test_blog")
    os.makedirs(os.path.join(test_blog_dir, "scratch"), exist_ok=True)
    
    old_dir = tools._current_blog_dir
    tools._current_blog_dir = test_blog_dir
    yield
    tools._current_blog_dir = old_dir
