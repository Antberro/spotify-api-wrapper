from spotify.spotifyClient import SpotifyClient

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

        Returns:
            str: A valid authorization token.
        """
        pass
