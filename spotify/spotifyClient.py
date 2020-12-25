import requests
from spotify.authManager import AuthManager, ClientCredentialFlow, AuthorizationCodeFlow
from spotify.trackManager import TrackManager
from spotify.constant import BASE_URL, STATUS_OK


class SpotifyClient(object):
    """
    Base class that represents a SpotifyClient that sends HTTP requests to
    the Spotify Web API.
    """
    
    def __init__(self, authManager: AuthManager):
        """
        Creates new instance of SpotifyClient.

        Args:
            authManager (AuthManager): The authManager used by the client.
        """
        self.authManager = authManager
        self.token = self.authManager.getToken()

        self.track = TrackManager(self)

    @classmethod
    def usingClientCredential(cls, clientId: str, clientSecret: str):
        """
        Creates an instance of SpotiftyClient that uses the Client Credentials Flow for authorization.

        Args:
            clientId (str): The client id.
            clientSecret (str): The client secret key.

        Returns:
            SpotifyClient: An instance of SpotifyClient.
        """
        authFlow = ClientCredentialFlow(clientId, clientSecret)
        return cls(authFlow)

    @classmethod
    def usingAuthorizationCode(cls,
                               clientId: str, 
                               clientSecret: str, 
                               redirectURI: str, 
                               scope: str = None, 
                               state: str = None, 
                               showDialog: bool = False):
        """
        Creates an instance of SpotifyClient that uses the Authorization Code Flow for authorization.

        Args:
            clientId (str): The client id.
            clientSecret (str): The client secret key.
            redirectURI (str): The URI to redirect to after the user grants or denies permission.
            scope (str, optional): A space-separated list of scopes. Defaults to None.
            state (str, optional): Provides protection against attacks such as cross-site request forgery. Defaults to None.
            showDialog (bool, optional): Whether or not to force the user to approve the app again if they’ve already done so. Defaults to False.

        Returns:
            SpotifyClient: An instance of SpotifyClient.
        """
        authFlow = AuthorizationCodeFlow(clientId,
                                         clientSecret,
                                         redirectURI,
                                         scope,
                                         state,
                                         showDialog)
        return cls(authFlow)

    def _sendHTTPRequest(self, method: str, url: str, params: dict = {}, headers: dict = {}) -> dict:
        """
        Sends an HTTP request to the given url with the given param and header arguments.

        Args:
            method (str): One of GET, POST, PUT, or DELETE.
            url (str): The endpoint url.
            params (dict, optional): The parameters of the HTTP request. Defaults to {}.
            headers (dict, optional): The headers of the HTTP request. Defaults to {}.

        Raises:
            response.raise_for_status: If request or response is invalid.

        Returns:
            dict: response from the HTTP request as json data
        """
        # send request
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)

        # handle response
        if response.status_code == STATUS_OK:
            responseData = response.json()
            return responseData
        else:
            raise response.raise_for_status()
