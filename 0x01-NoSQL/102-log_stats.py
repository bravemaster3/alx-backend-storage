#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most present IPs
in the collection nginx of the database logs:
"""


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient()
    db = client['logs']
    collection = db.nginx
    print(f"{len(list(collection.find()))} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(
            f"\tmethod {method}: "
            f"{len(list(collection.find({'method': method})))}"
        )
    print(
        f"{len(list(collection.find({'method': 'GET', 'path': '/status'})))}"
        f" status check"
    )
    aggr_collection = collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "ip_count": {"$sum": 1}  # Count occurrences of each IP
        }},
        {"$sort": {"ip_count", -1}},  # Sort by ip_count in descending order
        {"$limit": 10}  # Limit to top 10 documents
    ])
    print("IPs:")
    for log in list(aggr_collection):
        print(f"\t{log.ip}")
