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

    def getAlbum(self, albumId: str, market: str = None) -> dict:
        """
        Get the album with the given Spotify id.

        Args:
            albumId (str): The Spotify id for the album.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a album object in json format
        """
        pass

    def getSeveralAlbums(self, albumIds: list, market: str = None) -> dict:
        """
        Get multiple albums with the given Spotify ids. Maximum of 20 ids.

        Args:
            albumIds (list): The list of Spotify album ids.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a collection of album objects in json format
        """
        pass

    def getTracksOfAlbum(self, albumId: str, limit: int = 20, offset: int = 0, market: str = None) -> dict:
        """
        Get the tracks of the album with the given albumId.

        Args:
            albumId (str): The Spotify id for the album.
            limit (int, optional): The maximum number of tracks to return. Range from [1, 50]. Defaults to 20.
            offset (int, optional): The index of the first track to return. Defaults to 0.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a collection of track objects wrapped in a paging object in json format
        """
        pass