#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
from typing import Union, Callable
from uuid import uuid4
import functools


def count_calls(method: Callable) -> Callable:
    """Wrapper method for incrementing key"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Class Cache  definition"""
    def __init__(self):
        """instanciation method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that generates a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ convert the data back to the desired format."""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with the str conversion function"""
        return (self.get(key=key, fn=lambda d: d.decode("utf-8")))

    def get_int(self, key: str) -> int:
        """parametrize Cache.get with the int conversion function"""
        return (self.get(key=key, fn=int))
