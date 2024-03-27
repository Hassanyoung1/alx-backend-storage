#!/usr/bin/env python3
"""
a Python function that returns the list of a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
