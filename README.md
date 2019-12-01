# Circuitpy

Circuitpy is a abstract Python library for dealing with circuit breakers, it makes easy to use with anything or anywhere, you can use with `redis`, `sql`, `in memory cache`, `apis` and etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install circuitpy
```

## Usage

First you need to choose which storage you gonna use, you can use anything as storage since it implements three methods from [`Storage` interface](https://github.com/rafa-acioly/circuitpy/blob/master/circuitpy/base.py#L5)

> **Tip: Redis lib already has this methods by default, so it's easy to use.**

## Using redis

```python
import redis
from circuitpy.base import BaseCircuitBreaker

redis_cli = redis.Redis(host='localhost', port=6379, db=0)

class RequestCircuitBreaker(BaseCircuitBreaker):

    storage = redis_cli
    expected_exception = (Exception,)
    failure_threshold = 100
    recovery_timeout = 1
    failure_key = "request_cb"
```


## Using custom storage

```python
from circuitpy.base import Storage

class CustomStorage(Storage):

    def increment(self, key: str) -> None:
        """increment the errors quantity"""

    def get(self, key: str) -> int:
        """retrieve the errors quantity"""

    def expire(self, key: str, ttl: int) -> None:
        """implement some sort of expiration for the key parameter"""
```

```python
from circuitpy.base import BaseCircuitBreaker

class RequestCircuitBreaker(BaseCircuitBreaker):

    storage = CustomStorage()
    expected_exception = (Exception,)
    failure_threshold = 100
    recovery_timeout = 1
    failure_key = "request_cb"
```

## Implementation

```python
from circuitpy.circuit import circuit_breaker
from circuitpy.exceptions import CircuitBreakerOpen

@circuit_breaker(handler=RequestCircuitBreaker())
def lazy_method():
    try:
        # do stuff
    except CircuitBreakerOpen as open_circuit:
        logger.info(open_circuit)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/rafa-acioly/circuitpy/LICENSE)
