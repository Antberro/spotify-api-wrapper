import requests
from spotify.spotifyClient import SpotifyClient
from spotify.constant import TOKEN_URL, STATUS_OK

class ClientCredentialFlow(SpotifyClient):
    """
    Represents a SpotifyClient that uses the Client Credential Flow for authorization.
    Can only access endpoints that do not access user information.

    More info at: https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
    """

    def __init__(self, clientId: str, clientSecret: str):
        """
        Creates an instance of a ClientCredentialFlow SpotifyClient.

        Args:
            clientId (str): The client id.
            clientSecret (str): The client secret key.
        """
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.grantType = "client_credentials"

    def getToken(self) -> str:
        """
        Gets an authorization token.

        Raises:
            response.raise_for_status: If the request gives an unsuccessful response.

        Returns:
            str: A valid authorization token.
        """
        # send POST request
        response = requests.post(
            TOKEN_URL, {
            "grant_type": self.grantType,
            "client_id": self.clientId,
            "client_secret": self.clientSecret
        })

        # handle response
        if response.status_code == STATUS_OK:
            responseData = response.json()
            token = responseData["access_token"]
            return token
        else:
            raise response.raise_for_status()
        