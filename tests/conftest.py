import pytest
from typer.testing import CliRunner


@pytest.fixture
def cli_runner():
    return CliRunner()
