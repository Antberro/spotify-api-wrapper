import os
import json
from spotify.constant import CACHE_PATH


class BaseCache(object):
    """
    Base class that represents a cache that is used to get and save data.
    """

    def get(self, key: str):
        """
        Get the data with the specified key in the cache.

        Args:
            key (str): The key to get data from.

        Exceptions:
            raises KeyError if key is not in cache
            raises IOError if json file cannot be read
        """
        pass

    def save(self, key: str, value):
        """
        Save the given data with the given key in the cache.

        Args:
            key (str): The key to get data from.
            value (str, int): The data to save in the cache.

        Exceptions:
            raises IOError if json file cannot be read
        """
        pass

    def empty(self):
        """
        Empties the cache.

        Exceptions:
            raises IOError if json file cannot be read
        """
        pass


class MemoryCache(BaseCache):

    def __init__(self):
        self.data = {}

    def get(self, key: str):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError

    def save(self, key: str, value):
        self.data[key] = value

    def empty(self):
        self.data = {}


class LocalCache(BaseCache):

    def __init__(self):
        self.cacheFile = CACHE_PATH

    def get(self, key: str):
        try:
            with open(self.cacheFile) as file:
                data = json.load(file)
                if key in data:
                    return data[key]
                else:
                    raise KeyError
        except IOError as e:
            print(e)

    def save(self, key: str, value):
        try:
            # open json cache and add new key, value pair
            with open(self.cacheFile) as file:
                data = json.load(file)
                data[key] = value

            # write new dictionary to json
            with open(self.cacheFile, 'w') as file:
                json.dump(data, file)
        except IOError as e:
            print(e)

    def empty(self):
        try:
            with open(self.cacheFile, 'w') as file:
                json.dump({}, file)
        except IOError as e:
            print(e)