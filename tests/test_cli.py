import pytest
from click.testing import CliRunner
from cloner import cli

from unittest.mock import patch


def test_repo_path(monkeypatch):
    monkeypatch.delenv("CLONER_PATH", raising=False)
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 1


def test_no_args(monkeypatch):
    runner = CliRunner()
    result = runner.invoke(cli.main, [])
    assert result.exit_code == 1


def test_three_args(monkeypatch):
    runner = CliRunner()
    result = runner.invoke(cli.main, ['a', 'b', 'c'])
    assert result.exit_code == 1


def test_one_arg(monkeypatch):
    runner = CliRunner()
    result = runner.invoke(cli.main, ['a'])
    assert result.exit_code == 0


def test_two_args(monkeypatch):
    runner = CliRunner()
    result = runner.invoke(cli.main, ['a', 'b'])
    assert result.exit_code == 0
