#!/usr/bin/env python3
"""
a Python function that returns the list of a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    return mongo_collection.find({"topics": topic})
