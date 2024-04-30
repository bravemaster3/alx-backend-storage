#!/usr/bin/env python3
"""
implement a get_page function
"""


import requests
import redis
import functools


def track_access(func):
    @functools.wraps(func)
    def wrapper(url):
        # Initialize Redis connection
        redis_conn = redis.Redis()

        # Track the number of times the URL is accessed
        count_key = f"count:{url}"
        redis_conn.incr(count_key)

        return func(url)

    return wrapper


def cache_result(func):
    @functools.wraps(func)
    def wrapper(url):
        # Initialize Redis connection
        redis_conn = redis.Redis()

        # Check if the result is cached
        cached_result = redis_conn.get(url)
        if cached_result:
            return cached_result.decode('utf-8')

        # Call the original function to fetch the HTML content
        html_content = func(url)

        # Cache the result with an expiration time of 10 seconds
        redis_conn.setex(url, 10, html_content)

        return html_content

    return wrapper


@track_access
@cache_result
def get_page(url: str) -> str:
    # Fetch the HTML content from the URL
    response = requests.get(url)
    return response.text
