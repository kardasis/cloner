from click.testing import CliRunner
from cloner import cli


def test_repo_path_must_exist(monkeypatch):
    monkeypatch.delenv("CLONER_PATH", raising=False)
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 1
