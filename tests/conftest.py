import pytest


@pytest.fixture(autouse=True)
def repo_path_set(monkeypatch):
    monkeypatch.setenv("CLONER_PATH", "/path/to/my/repos")
