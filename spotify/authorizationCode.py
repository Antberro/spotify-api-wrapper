from spotify.spotifyClient import SpotifyClient

class AuthorizationCodeFlow(SpotifyClient):
    """
    Represents a SpotifyClient that uses the Authorization Code Flow for authorization.
    Can access endpoints that access user information.

    More info at: https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow
    """

    def __init__(self, 
                 clientId: str, 
                 clientSecret: str, 
                 redirectURI: str, 
                 scope: str = None, 
                 state: str = None, 
                 showDialog: bool = False):
        """
        [summary]

        Args:
            clientId (str): The client id.
            clientSecret (str): The client secret key.
            redirectURI (str): The URI to redirect to after the user grants or denies permission.
            scope (str, optional): A space-separated list of scopes. Defaults to None.
            state (str, optional): Provides protection against attacks such as cross-site request forgery. Defaults to None.
            showDialog (bool, optional): Whether or not to force the user to approve the app again if they’ve already done so. Defaults to False.
        """
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.redirectURI = redirectURI
        self.scope = scope
        self.state = state
        self.showDialog = showDialog
        self.grantType = "authorization_code"
        self.responseType = "code"

    def getToken(self) -> str:
        """
        Gets an authorization token.

        Returns:
            str: A valid authorization token.
        """
        pass