from pycircuit.base import BaseCircuitBreaker


class StubStorage:

    errors_quantity: int = 0

    def increment(self, key: str) -> int:
        self.errors_quantity += 1

    def expire(self, key: str, ttl: int) -> None:
        pass

    def get(self, key: str) -> int:
        return self.errors_quantity


class StubHandler(BaseCircuitBreaker):
    storage = StubStorage()
    catch_exceptions = (Exception,)
    max_failures = 0
    timeout = 1
    failure_key = "myhandler_cb"
