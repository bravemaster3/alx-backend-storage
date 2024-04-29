#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB:
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
