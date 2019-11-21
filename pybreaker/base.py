import abc
from typing import Tuple


class BaseCircuitBreaker(abc.ABC):

    @abc.abstractmethod
    def increment(self) -> None:
        raise Exception(
            'an increment method should be defined '
            'on circuit breaker handler'
        )

    @abc.abstractmethod
    def catch_exceptions(self) -> Tuple[Exception]:
        raise Exception(
            'an exception class should be defined '
            'on circuit breaker handler so you can except for it '
            'when the circuit is open'
        )

    @abc.abstractmethod
    def is_open(self) -> bool:
        raise Exception(
            'an validation method is_open should be defined '
            'on circuit breaker handler'
        )

    @abc.abstractmethod
    def failure_key(self) -> str:
        """Failure key

            Defines the key that will be used to store
            the circuit breaker errors counter.
        """
        raise Exception(
            'an key should be defined '
            'to track the errors amount'
        )

    @abc.abstractmethod
    def max_failures(self) -> int:
        """Max failures
            The amount of failures required to open the circuit.
        """
        raise Exception('the max failure amount should be defined')

    @abc.abstractmethod
    def timeout(self) -> int:
        """timeout

            Defines for how long the circuit key will remain,
            until it close the circuit again.
        """
        raise Exception(
            'an timeout should be defined '
            'so the circuit can close properly'
        )

