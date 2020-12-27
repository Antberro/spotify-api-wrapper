import unittest
from requests import HTTPError
from spotify.spotifyClient import SpotifyClient
from spotify.constant import CLIENT_ID, CLIENT_SECRET


class TestGetArtist(unittest.TestCase):
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
        artistId = "73sIBHcqh3Z3NyqHKZ7FOL"
        client.artist.getArtist(artistId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        artistId = ""
        with self.assertRaises(HTTPError): 
            client.artist.getArtist(artistId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetSeveralArtists(unittest.TestCase):
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
        artistId1 = "73sIBHcqh3Z3NyqHKZ7FOL"
        artistId2 = "2YZyLoL8N0Wb9xBt1NhZWg"
        artistId3 = "711MCceyCBcFnzjGY4Q7Un"
        artistIds = [artistId1, artistId2, artistId3]
        client.artist.getSeveralArtists(artistIds)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        artistId1 = ""
        artistId2 = ""
        artistId3 = ""
        artistIds = [artistId1, artistId2, artistId3]
        with self.assertRaises(HTTPError): 
            client.artist.getSeveralArtists(artistIds)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetAlbums(unittest.TestCase):
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
        artistId = "73sIBHcqh3Z3NyqHKZ7FOL"
        client.artist.getAlbums(artistId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        artistId = ""
        with self.assertRaises(HTTPError): 
            client.artist.getAlbums(artistId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetTopTracks(unittest.TestCase):
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
        artistId = "73sIBHcqh3Z3NyqHKZ7FOL"
        client.artist.getTopTracks(artistId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        artistId = ""
        with self.assertRaises(HTTPError): 
            client.artist.getTopTracks(artistId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO


class TestGetRelatedArtists(unittest.TestCase):
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
        artistId = "73sIBHcqh3Z3NyqHKZ7FOL"
        client.artist.getRelatedArtists(artistId)

    # covers: client credential flow, response is invalid
    def test_invalid_client_cred(self):
        client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
        artistId = ""
        with self.assertRaises(HTTPError): 
            client.artist.getRelatedArtists(artistId)

    # covers: authorization code flow, response is valid
    def test_valid_auth_code(self):
        pass #TODO

    # covers: authorization code flow, response is invalid
    def test_invalid_auth_code(self):
        pass #TODO