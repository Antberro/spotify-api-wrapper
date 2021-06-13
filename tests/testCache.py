import unittest
from spotify.spotifyClient import SpotifyClient
from spotify import cache


class TestMemoryCache(unittest.TestCase):
    """
    Testing Strategy

    Partition on command:
        - get item from cache
        - save item to cache
        - empty cache

    Partition on item availability:
        - item is in cache
        - item is not in cache
    """
    
    # covers: save item, get item, empty, item is in cache
    def test_item_in_cache(self):

        cache = cache.MemoryCache()
        keys = ['a', 'b', 'c']
        values = ['aaa', 'bbb', 'ccc']

        # save items to cache
        for i in range(len(keys)):
            cache.save(keys[i], values[i])

        # get items from cache
    	for i in range(len(keys)):
            item = cache.get(keys[i])
            self.assertEqual(item, values[i], "expected values to be equal")

        cache.empty()


    # covers: get item, item is not in cache
    def test_item_not_in_cache(self):

        cache = cache.MemoryCache()
        with self.assertRaises(KeyError): 
            cache.get('a')


class TestLocalCache(unittest.TestCase):
    """
    Testing Strategy

    Partition on command:
        - get item from cache
        - save item to cache
        - empty cache

    Partition on item availability:
        - item is in cache
        - item is not in cache
    """
    
    # covers: save item, get item, empty, item is in cache
    def test_item_in_cache(self):

        cache = cache.LocalCache()
        keys = ['a', 'b', 'c']
        values = ['aaa', 'bbb', 'ccc']

        # save items to cache
        for i in range(len(keys)):
            cache.save(keys[i], values[i])

        # get items from cache
    	for i in range(len(keys)):
            item = cache.get(keys[i])
            self.assertEqual(item, values[i], "expected values to be equal")

        cache.empty()


    # covers: get item, item is not in cache
    def test_item_not_in_cache(self):

        cache = cache.LocalCache()
        with self.assertRaises(KeyError): 
            cache.get('a')