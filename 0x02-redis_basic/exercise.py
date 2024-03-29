#!/usr/bin/env python3

"""
a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis
(using redis.Redis()) and flush the instance using flushdb.
"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
""""def count_calls(methods: Callable):
    count += 1
    return count"""


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
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key
