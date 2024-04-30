#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """ Function definition here"""
    pipeline = [
        # unwind the topics array to work with individual scores
        {"$unwind": "$topics"},
        # Group by student name and calculate average score
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        # Sort by average score in descending order
        {"$sort": {"averageScore": -1}}
    ]
    # Execute the aggregation pipeline
    result = mongo_collection.aggregate(pipeline)
    return list(result)
