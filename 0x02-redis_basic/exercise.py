#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Class Cache  definition"""
    def __init__(self):
        """instanciation method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that generates a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
