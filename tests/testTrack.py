import unittest
from requests import HTTPError
from spotify.spotifyClient import SpotifyClient
from spotify.constant import CLIENT_ID, CLIENT_SECRET


class TestGetTrack(unittest.TestCase):
    """
    Testing Strategy

    Partition on authorization flow:
        - client credential flow
        - authorization code

    Partition on response:
        - response is valid
        - response is invalid
    """
    
    # covers: client credential flow, response is valid
    def test_valid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        trackId = "1LeWIs2hP2r5yOQnVuYoI5"
        client.track.getTrack(trackId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        trackId = "invalid id"
        with self.assertRaises(HTTPError): 
            client.track.getTrack(trackId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO
