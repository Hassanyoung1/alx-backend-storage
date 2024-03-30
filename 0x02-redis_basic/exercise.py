#!/usr/bin/env python3

"""
a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis
(using redis.Redis()) and flush the instance using flushdb.
"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    key = method.__qualname__
    data = {
        "inputs": key + ":inputs",
        "outputs": key + ":outputs"
    }
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(data["inputs"], str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(data["outputs"], str(output))
        return output
    return wrapper


def replay(method:Callable) ->  Callable:
    key = method.__qualname__
    data = {
        "inputs": key + ":inputs",
        "outputs": key + ":outputs"
    }
    inputs = self._redis.lrange(data["inputs"], 0, -1)
    outputs = self._redis.lrange(data["outputs"], 0, -1)
    print(f"{key} was called {self._redis.get(key)} times:")
    for i, o in zip(inputs, outputs):
        print(f"{key}({i}) -> {o}")

    return method



class Cache:
    """
    A class to store data in Redis
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    """
    A method to store data in Redis
    """
    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int, float, None]:
        value = self._redis.get(key)
        if fn is not None:
            value = fn(value)
        else:
            return value


    def get_str(self, key: str) -> str:
        return self.get(key, str)


    def get_int(self, key: str) -> int:
        return self.get(key, int)
