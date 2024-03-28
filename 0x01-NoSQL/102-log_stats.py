#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


if __name__ == "__main__":
    """ script that provides some stats about Nginx logs stored in MongoDB: """
    """ - Database: logs """
    """ - Collection: nginx """
    """ Display: """
    """ - first line: x logs where x is the number of documents in the logs collection """
    """ - Second line: Methods: """
    """ - 5 lines with the number of documents with the method """
    """ - GET method: """
    """ - POST method: """
    """ - PUT method: """
    """ - PATCH method: """
    """ - DELETE method: """
    """ - One line with the number of documents with: """
    """ - method set to GET """
    """ - path set to /status """

    client = MongoClient('mongodb://127.0.01:27017')
    logs = client.logs.nginx
    print(f"{logs.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    filter_path = {"method": "GET", "path": "/status"}
    print(f"{logs.count_documents(filter_path)} status check")
    print("IPs:")
    ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
