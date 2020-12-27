from spotify.constant import BASE_URL


class ArtistManager(object):
    """
    Class responsible for managing requests about artists to the Spotify Web API.
    """

    def __init__(self, client):
        self.client = client

    def getArtist(self, artistId: str) -> dict:
        """
        Get the artist with the given Spotify id.

        Args:
            artistId (str): The Spotify id for the artist.

        Returns:
            dict: response from Spotify Web API, an artist object in json format
        """
        
        # define param and header args for request
        url = BASE_URL + "/artists/" + artistId
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response

    def getSeveralArtists(self, artistIds: list) -> dict:
        """
        Get multiple artists with the given Spotify ids. Maximum of 50 ids.

        Args:
            artistIds (list): The list of Spotify artist ids.

        Returns:
            dict: response from Spotify Web API, a collection of artist objects in json format
        """
        
        # define param and header args for request
        url = BASE_URL + "/artists"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"ids": ",".join(artistIds)}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response

    def getAlbums(self, artistId: str, includeGroups: list = None, 
                  country: str = "US", limit: int = 20, offset: int = 0) -> dict:
        """
        Get the albums of the artist with the given artist id.

        Args:
            artistId (str): The Spotify id for the artist.
            includeGroups (list, optional): List of keywords to filter response. Choose from [album, single, appears_on, compilation]. Defaults to None.
            country (str, optional): The geographic market to get albums from. Defaults to "US".
            limit (int, optional): The maximum number of albums to return. Range from [1, 50]. Defaults to 20.
            offset (int, optional): The index of the first album to return. Defaults to 0.

        Returns:
            dict: response from Spotify Web API, a collection of album objects wrapped in a paging object in json format
        """
        pass

    def getTopTracks(self, artistId: str, country: str = "US") -> dict:
        """
        Get the top tracks of the artist with the given artist id.

        Args:
            artistId (str): The Spotify id for the artist.
            country (str, optional): The geographic market to get tracks from. Defaults to "US".

        Returns:
            dict: response from Spotify Web API, a collection of at most 10 track objects in json format
        """
        pass

    def getRelatedArtists(self, artistId: str) -> dict:
        """
        Get related artists of the artist with the given artist id.

        Args:
            artistId (str): The Spotify id for the artist.

        Returns:
            dict: response from Spotify Web API, a collection of at most 20 artist objects in json format
        """
        pass