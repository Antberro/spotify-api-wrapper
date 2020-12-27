import unittest
from requests import HTTPError
from spotify.spotifyClient import SpotifyClient
from spotify.constant import CLIENT_ID, CLIENT_SECRET


class TestGetAlbum(unittest.TestCase):
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
        albumId = "6cx4GVNs03Pu4ZczRnWiLd"
        client.album.getAlbum(albumId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        albumId = ""
        with self.assertRaises(HTTPError): 
            client.album.getAlbum(albumId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetSeveralAlbums(unittest.TestCase):
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
        albumId1 = "6cx4GVNs03Pu4ZczRnWiLd"
        albumId2 = "5z090LQztiqh13wYspQvKQ"
        albumId3 = "0BwWUstDMUbgq2NYONRqlu"
        albumIds = [albumId1, albumId2, albumId3]
        client.album.getSeveralAlbums(albumIds)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        albumId1 = "6cx4GVNs03Pu4ZczRnWiLd"
        albumId2 = "5z090LQztiqh13wYspQvKQ"
        albumId3 = "0BwWUstDMUbgq2NYONRqlu"
        albumIds = [albumId1, albumId2, albumId3]
        with self.assertRaises(HTTPError): 
            client.album.getSeveralAlbums(albumIds)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetTracks(unittest.TestCase):
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
        albumId = "6cx4GVNs03Pu4ZczRnWiLd"
        client.album.getTracks(albumId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        albumId = "6cx4GVNs03Pu4ZczRnWiLd"
        with self.assertRaises(HTTPError): 
            client.album.getTracks(albumId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO