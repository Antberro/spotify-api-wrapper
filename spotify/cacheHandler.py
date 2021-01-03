import os
import json
from spotify.constant import CACHE_PATH


class CacheHandler(object):
    """
    Represents a CacheHandler that is used to save and load data
    in a local cache.
    """

    def __init__(self):
        """
        Creates an instance of CacheHandler.
        """
        self.filepath = CACHE_PATH

    def loadData(self, field: str):
        """
        Get the data with the specified field in the cache.

        Args:
            field (str): The field to get data from.
        """
        
        try:
            with open(self.filepath) as file:
                cache = json.load(file)
                return cache[field]

        except IOError as e:
            print(e)
            print("IOError: Could not read from cache.json")

    def saveData(self, field: str, data):
        """
        Save the given data with the given field in the cache.

        Args:
            field (str): The field to get data from.
            data (str, int): The data to save in the cache.
        """
        
        try:
            with open(self.filepath) as file:
                newCache = json.load(file)
                newCache[field] = data

            with open(self.filepath, "w") as file:
                json.dump(newCache, file)
                
        except IOError as e:
            print(e)
            print("IOError: Could not read from cache.json")