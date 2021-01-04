from spotify.constant import BASE_URL

class LibraryManager(object):
    """
    Class responsible for managing requests about user's library to the Spotify Web API.
    """

    def __init__(self, client):
        """
        Creates an instance of PlaylistManager.

        Args:
            client (SpotifyClient): The client to send requests to.
        """
        self.client = client

    def getSavedTracks(self, limit: int = 20, offset: int = 0, market: str = None) -> dict:
        """
        Get a list of songs saved by current Spotify user.

        Requires scope: "user-library-read"

        Args:
            limit (int, optional): The maximum number of tracks to return. Range from [1, 50]. Defaults to 20.
            offset (int, optional): The index of the first track to return. Defaults to 0.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a collection of track objects wrapped in a paging object in json format
        """
        
        # define param and header args for request
        url = BASE_URL + "/me/tracks"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"limit": limit, "offset": offset}
        if market:
            params["market"] = market

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response

    def getSavedAlbums(self):
        pass

