#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""

import pymongo


def list_all(mongo_collection):

    """return an empty list if no document in collection"""

    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
