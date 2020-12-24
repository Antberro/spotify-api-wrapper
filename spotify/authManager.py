import requests
from spotify.constant import TOKEN_URL, STATUS_OK


class AuthManager(object):
    """
    Base class that represents an AuthManager that handles authorization 
    using a particular authorization flow.
    """

    def getToken(self) -> str:
        """
        Gets an authorization token.

        Returns:
            str: A valid authorization token.
        """
        pass


class ClientCredentialFlow(AuthManager):
    """
    Represents an AuthManager that uses the Client Credential Flow for authorization.
    Can only access endpoints that do not access user information.

    More info at: https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
    """

    def __init__(self, clientId: str, clientSecret: str):
        """
        Creates an instance of a ClientCredentialFlow AuthManager.

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


class AuthorizationCodeFlow(AuthManager):
    """
    Represents an AuthManager that uses the Authorization Code Flow for authorization.
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
        Creates an instance of an AuthorizationCodeFlow AuthManager.

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