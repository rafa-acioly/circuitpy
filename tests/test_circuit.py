import pytest

class TestCircuitBreaker:

    @pytest.mark.skip
    def test_circuit_is_open(self, stub_handler):

        @circuit_breaker(handler: stub_handler)
        def handler():
            raise Exception

        with pytest.raises(CircuitBreakerOpen):
            handler()
