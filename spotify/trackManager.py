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
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"market": market} if market else {}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response


    def getSeveralTracks(self, trackIds: list, market: str = None) -> dict:
        """
        Get multiple tracks with the given Spotify ids. Maximum of 50 ids.

        Args:
            trackIds (list): The list of Spotify track ids.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, collection of track objects in json format
        """
        assert len(trackIds) <= 50, "expected len(trackIds) <= 50"

        # define param and header args for request
        url = BASE_URL + "/tracks"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"ids": ",".join(trackIds)}
        if market:
            params["market"] = market
        
        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response


    def getAudioFeatures(self, trackId: str) -> dict:
        """
        Get audio features for the track with the given Spotify id.

        Args:
            trackId (str): The Spotify id for the track.

        Returns:
            dict: response from Spotify Web API, an audio feature object in json format
        """
        
        # define param and header args for request
        url = BASE_URL + "/audio-features/" + trackId
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}  
        params = {}  

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response


    def getSeveralAudioFeatures(self, trackIds: list) -> dict:
        """
        Get audio features for multiple tracks with the given Spotify ids.
        Maximum of 100 ids.

        Args:
            trackIds (list): The list of Spotify track ids.

        Returns:
            dict: response from Spotify Web API, collection of audio features objects in json format
        """
        assert len(trackIds) <= 100, "expected len(trackIds) <= 100"

        # define param and header args for request
        url = BASE_URL + "/audio-features"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"ids": ",".join(trackIds)}
        
        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response


    def getAudioAnalysis(self) -> dict:
        pass