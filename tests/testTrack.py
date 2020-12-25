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


class TestGetSeveralTracks(unittest.TestCase):
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
        trackIds = [
            "1LeWIs2hP2r5yOQnVuYoI5",
            "0qdQUeKVyevrbKhAo0ibxS",
            "6Ac4NVYYl2U73QiTt11ZKd"
        ]
        client.track.getSeveralTracks(trackIds)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        trackIds = [
            "invalid id1",
            "invalid id2",
            "invalid id3" 
        ]
        with self.assertRaises(HTTPError): 
            client.track.getSeveralTracks(trackIds)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetAudioFeatures(unittest.TestCase):
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
        client.track.getAudioFeatures(trackId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        trackId = "invalid id"
        with self.assertRaises(HTTPError): 
            client.track.getAudioFeatures(trackId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetSeveralAudioFeatures(unittest.TestCase):
    """
    Testing Strategy

    Partition on authorization flow:
        - client credential flow
        - authorization code

    Partition on response:
        - response is valid
    """
    # covers: client credential flow, response is valid
    def test_valid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        trackIds = [
            "1LeWIs2hP2r5yOQnVuYoI5",
            "0qdQUeKVyevrbKhAo0ibxS",
            "6Ac4NVYYl2U73QiTt11ZKd"
        ]
        client.track.getSeveralAudioFeatures(trackIds)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO


class TestGetAudioAnalysis(unittest.TestCase):
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
        client.track.getAudioAnalysis(trackId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        trackId = "invalid id"
        with self.assertRaises(HTTPError): 
            client.track.getAudioAnalysis(trackId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO