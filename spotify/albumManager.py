from spotify.constant import BASE_URL


class AlbumManager(object):
    """
    Class responsible for managing requests about albums to the Spotify Web API.
    """

    def __init__(self, client):
        """
        Creates an instance of AlbumManager.

        Args:
            client (SpotifyClient): The client to send requests to.
        """
        self.client = client

    def getAlbum(self) -> dict:
        pass

    def getSeveralAlbums(self) -> dict:
        pass

    def getTracksOfAlbum(self) -> dict:
        pass