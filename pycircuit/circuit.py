from functools import wraps

from pycircuit.base import BaseCircuitBreaker
from pycircuit.exceptions import CircuitBreakerOpen


def circuit_breaker(handler: BaseCircuitBreaker):
    def factory(method):
        @wraps(method)
        def circuit(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except handler.catch_exceptions:
                if handler.is_open():
                    raise CircuitBreakerOpen(method)

                handler.ping()
        return circuit
    return factory