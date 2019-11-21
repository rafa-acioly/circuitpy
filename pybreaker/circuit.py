from functools import wraps

from pybreaker.base import BaseCircuitBreaker
from pybreaker.exceptions import CircuitBreakerOpen


def circuit_breaker(circuit: BaseCircuitBreaker):
    def circuit_breaker_method(method):
        @wraps(method)
        def circuit_breaker_wrapper(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except circuit.catch_exceptions:
                if circuit.is_open():
                    raise CircuitBreakerOpen

                circuit.increment()
        return circuit_breaker_wrapper
    return circuit_breaker_method
