import unittest
from requests import HTTPError
from spotify.clientCredentialFlow import ClientCredentialFlow
from spotify.constant import CLIENT_ID, CLIENT_SECRET


class TestClientCredentialFlow(unittest.TestCase):
    """
    Testing Strategy

    Partition on response:
        - response is valid
        - response is invalid
    """

    def test_valid_response(self):
        client = ClientCredentialFlow(CLIENT_ID, CLIENT_SECRET)
        token = client.getToken()
        self.assertTrue(isinstance(token, str), "expected token to be of type string")

    def test_invalid_response(self):
        clientId = "invalid id"
        clientSecret = "invalid secret"
        client = ClientCredentialFlow(clientId, clientSecret)
        with self.assertRaises(HTTPError): 
            client.getToken()


class TestAuthorizationCredentialFlow(unittest.TestCase):
    pass