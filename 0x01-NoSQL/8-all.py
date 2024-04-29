#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """ Function definition here"""
    all_docs = list(mongo_collection.find())
    return all_docs
