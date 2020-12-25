import unittest
from requests import HTTPError
from spotify.spotifyClient import SpotifyClient
from spotify.constant import CLIENT_ID, CLIENT_SECRET


class TestClientCredentialFlow(unittest.TestCase):
    """
    Testing Strategy

    Partition on response:
        - response is valid
        - response is invalid
    """

    def test_valid_response(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

    def test_invalid_response(self):
        clientId = "invalid id"
        clientSecret = "invalid secret"
        with self.assertRaises(HTTPError): 
            SpotifyClient.usingClientCredential(clientId, clientSecret)


class TestAuthorizationCredentialFlow(unittest.TestCase):
    pass #TODO