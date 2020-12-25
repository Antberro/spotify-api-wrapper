import requests
from spotify.constant import BASE_URL, CLIENT_ID, CLIENT_SECRET, STATUS_OK


class TrackManager(object):
    """
    Class responsible for managing requests about tracks to the Spotify Web API.
    """

    def __init__(self, client):
        """
        Creates an instance of TrackManager.

        Args:
            client (SpotifyClient): The client to send requests to.
        """
        self.client = client

    def getTrack(self, trackId: str, market: str = None) -> dict:
        """
        Get the track with the given Spotify id.

        Args:
            trackId (str): The Spotify id for the track.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a track object in json format
        """

        # define param and header args for request
        url = BASE_URL + "/tracks/" + trackId
        headers = {"Authorization": "Bearer " + self.client.token}
        params = {"market": market} if market else {}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response


    def getSeveralTracks(self) -> dict:
        pass


    def getAudioFeatures(self) -> dict:
        pass


    def getSeveralAudioFeatures(self) -> dict:
        pass


    def getAudioAnalysis(self) -> dict:
        pass