from unittest.mock import Mock, MagicMock, patch
import pytest

from pybreaker.circuit import circuit_breaker
from pybreaker.exceptions import CircuitBreakerOpen
from pybreaker.base import BaseCircuitBreaker
from .stub import StubStorage, StubHandler


class TestCircuitBreaker:

    @pytest.fixture
    def circuit_handler(self, stub_handler):
        return circuit_breaker(handler=stub_handler)

    def test_circuit_is_open(self, circuit_handler):
        """
        Test method raise the circuit breaker default exception
        """
        with pytest.raises(CircuitBreakerOpen):
            circuit_handler(Mock(side_effect=Exception))()

    def test_circuit_ping_storage(self, circuit_handler):
        """
        Test that the ping method is called to increment the circuit breaker
        """
        with patch.object(BaseCircuitBreaker, 'is_open') as mock_base, \
                patch.object(StubHandler, 'ping') as mock_ping:
            mock_base.return_value = False
            circuit_handler(Mock(side_effect=Exception))()
            assert mock_ping.called
