import unittest
from requests import HTTPError
import spotify.track as track


class TestGetTrack(unittest.TestCase):
    """
    Testing Strategy

    Partition on response:
        - response is valid
        - response is invalid
    """

    def test_valid_response(self):
        trackId = "1LeWIs2hP2r5yOQnVuYoI5"
        result = track.getTrack(trackId)
        self.assertTrue(isinstance(track, dict), "expected response to be a dictionary")

    def test_invalid_response(self):
        trackId = "invalid id"
        with self.assertRaises(HTTPError): 
            track.getTrack(trackId)
