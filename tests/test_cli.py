import pytest
from click.testing import CliRunner
from cloner import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli.command, ['not-a-valid-url'])
    assert result.exit_code == 1
