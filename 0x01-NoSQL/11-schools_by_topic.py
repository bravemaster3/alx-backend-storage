#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """ Function definition here"""
    my_schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(my_schools)
