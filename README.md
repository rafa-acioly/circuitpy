# Pybreaker

pybreaker is a abstract Python library for dealing with circuit breakers.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pybreaker
```

## Usage

Implement your storage handler so the circuit breaker can store
all the failures.

> **You can use the redis lib that already have this methods**

## Using redis

```python
import redis
from pybreaker.base import BaseCircuitBreaker


redis_cli = redis.Redis(host='localhost', port=6379, db=0)

class RequestCircuitBreaker(BaseCircuitBreaker):

    storage = redis_cli
    catch_exceptions = (Exception, KeyError,)
    max_failures = 100
    timeout = 1
    failure_key = "request_cb"
```


## Using custom storage

```python
from pybreaker.base import Storage

class CustomStorage(Storage):

    def increment(self, key: str) -> None:
        """increment the errors quantity"""

    def get(self, key: str) -> int:
        """retrieve the errors quantity"""
    
    def expire(self, key: str, ttl: int) -> None:
        """implement some sort of expiration for the key parameter"""
```

```python
from pybreaker.base import BaseCircuitBreaker

class RequestCircuitBreaker(BaseCircuitBreaker):

    storage = CustomStorage()
    catch_exceptions = (Exception, KeyError,)
    max_failures = 100
    timeout = 1
    failure_key = "request_cb"
```

## Implementation

```python
from pybreaker.circuit import circuit_breaker

@circuit_breaker(handler=RequestCircuitBreaker())
def lazy_method():
    pass
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/rafa-acioly/pybreaker/LICENSE)