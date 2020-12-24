class SpotifyClient(object):
    """
    Base class that represents a SpotifyClient that sends HTTP requests to
    the Spotify Web API.
    """

    def sendGetRequest(self, headers: dict, params: dict) -> dict:
        """
        Send a GET request to the Spotify Web API.

        Args:
            headers (dict): Header parameters for GET request.
            params (dict): Query parameters for GET request.

        Returns:
            dict: The HTTP response as json data.
        """
        pass

    def sendPostRequest(self, headers: dict, params: dict) -> dict:
        """
        Send a POST request to the Spotify Web API.

        Args:
            headers (dict): Header parameters for POST request.
            params (dict): Query parameters for POST request.

        Returns:
            dict: The HTTP response as json data.
        """
        pass

    def sendPutRequest(self, headers: dict, params: dict) -> dict:
        """
        Send a PUT request to the Spotify Web API.

        Args:
            headers (dict): Header parameters for PUT request.
            params (dict): Query parameters for PUT request.

        Returns:
            dict: The HTTP response as json data.
        """
        pass

    def sendDeleteRequest(self, headers: dict, params: dict) -> dict:
        """
        Send a DELETE request to the Spotify Web API.

        Args:
            headers (dict): Header parameters for DELETE request.
            params (dict): Query parameters for DELETE request.

        Returns:
            dict: The HTTP response as json data.
        """
        pass