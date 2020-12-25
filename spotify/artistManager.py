from spotify.constant import BASE_URL


class ArtistManager(object):

    def __init__(self, client):
        self.client = client

    def getArtist(self) -> dict:
        pass

    def getSeveralArtists(self) -> dict:
        pass

    def getAlbums(self) -> dict:
        pass

    def getTopTracks(self) -> dict:
        pass

    def getRelatedArtists(self) -> dict:
        pass