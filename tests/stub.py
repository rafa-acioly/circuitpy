from circuitpy.base import BaseCircuitBreaker


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
    expected_exception = (Exception,)
    failure_threshold = 0
    recovery_timeout = 1
    failure_key = "myhandler_cb"
