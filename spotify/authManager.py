import requests
import webbrowser
from spotify.constant import AUTHORIZE_URL, TOKEN_URL, STATUS_OK
from spotify.cacheHandler import CacheHandler


class AuthManager(object):
    """
    Base class that represents an AuthManager that handles authorization 
    using a particular authorization flow.
    """

    def authorize(self, refresh: bool = False) -> dict:
        """
        Gets an authorization token.

        Args:
            refresh (bool, optional): True if refresh token is to be used. Defaults to False.

        Returns:
            dict: Response from Spotify API in json format.
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

    def authorize(self, refresh: bool = False) -> dict:
        """
        Authorizes with Spotify API.

        Args:
            refresh (bool, optional): True if refresh token is to be used. Defaults to False.

        Raises:
            response.raise_for_status: If the request gives an unsuccessful response.

        Returns:
            dict: Response from Spotify API in json format
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
            return responseData
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
        self.cache = CacheHandler()
        self.code = None

        self.clientId = clientId
        self.clientSecret = clientSecret
        self.redirectURI = redirectURI
        self.scope = scope
        self.state = state
        self.showDialog = showDialog
        self.grantType = "authorization_code"
        self.responseType = "code"

    def _useRefreshToken(self) -> dict:
        """
        Uses refresh token to get a new access token.

        Raises:
            response.raise_for_status: If the request gives an unsuccessful response.

        Returns:
            dict: Response from Spotify API in json format
        """

        refreshToken = self.cache.loadData("refresh_token")

        # construct POST request
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refreshToken,
            "client_id": self.clientId,
            "client_secret": self.clientSecret
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # send POST request
        response = requests.post(
            TOKEN_URL,
            data=payload,
            headers=headers
        )

        # handle response
        if response.status_code == STATUS_OK:
            responseData = response.json()

            # get date from response
            accessToken = responseData["access_token"]
            expiresIn = responseData["expires_in"]

            # save data in cache
            self.cache.saveData("access_token", accessToken)
            self.cache.saveData("expires_in", expiresIn)

            return {"access_token": accessToken, "expires_in": expiresIn}

        else:
            raise response.raise_for_status()

    def _promptUserAuthorization(self):
        """
        Opens external webpage to allow user to login with Spotify account.
        """

        # construct GET request
        url = "{}?client_id={}&response_type={}&redirect_uri={}&scope={}&show_dialog={}".format(
            AUTHORIZE_URL,
            self.clientId,
            self.responseType,
            self.redirectURI,
            self.scope,
            self.showDialog
        )

        if self.state:
            url += "&state={}".format(self.state)
        
        # prompt user to login to Spotify account
        webbrowser.open(url)

        # load data from cache
        self.code = self.cache.loadData("code")
        error = self.cache.loadData("error")

        # handle error
        if error:
            print(error)

    def _getAccessToken(self) -> dict:
        """
        Get new access token.

        Raises:
            response.raise_for_status: If the request gives an unsuccessful response.

        Returns:
            dict: Response from Spotify API in json format
        """

        # construct POST request
        payload = {
            "grant_type": self.grantType,
            "code": self.code,
            "redirect_uri": self.redirectURI,
            "client_id": self.clientId,
            "client_secret": self.clientSecret
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # send POST request
        response = requests.post(
            TOKEN_URL,
            data=payload,
            headers=headers
        )

        # handler response
        if response.status_code == STATUS_OK:
            responseData = response.json()

            # get data from response
            accessToken = responseData["access_token"]
            expiresIn = responseData["expires_in"]
            refreshToken = responseData["refresh_token"]

            # save data to cache
            self.cache.saveData("access_token", accessToken)
            self.cache.saveData("expires_in", expiresIn)
            self.cache.saveData("refresh_token", refreshToken)

            return {"access_token": accessToken, "expires_in": expiresIn}

        else:
            raise response.raise_for_status()

    def authorize(self, refresh: bool = False) -> str:
        """
        Authorizes with Spotify API.
    
        Args:
            refresh (bool, optional): True if refresh token is to be used. Defaults to False.

        Raises:
            response.raise_for_status: If the request gives an unsuccessful response.

        Returns:
            dict: Response from Spotify API in json format
        """

        # if needed, use refresh token
        if refresh:
            return self._useRefreshToken()

        # otherwise, get new access token
        else:
            self._promptUserAuthorization()
            return self._getAccessToken()
