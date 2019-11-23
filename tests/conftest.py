import pytest
from stub import StubHandler


@pytest.fixture
def stub_handler():
    return StubHandler()
