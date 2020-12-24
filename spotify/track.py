import requests
from spotify.constant import BASE_URL, CLIENT_ID, CLIENT_SECRET, STATUS_OK
from spotify.clientCredentialFlow import ClientCredentialFlow


def getTrack(trackId: str, market: str = None) -> dict:
    """
    Get the track with the given Spotify id.

    Args:
        trackId (str): The Spotify id for the track.
        market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

    Returns:
        dict: response from Spotify Web API, a track object in json format
    """
    # create Spotify client to send request
    client = ClientCredentialFlow(CLIENT_ID, CLIENT_SECRET)

    # define param and header args for request
    headers = {"Authorization": "Bearer " + client.getToken()}
    params = {"market": market} if market else {}
    
    # send request
    response = requests.get(
        BASE_URL + "/tracks/" + trackId,
        params=params,
        headers=headers
    )

    # handle response
    if response.status_code == STATUS_OK:
        responseData = response.json()
        return responseData
    else:
        raise response.raise_for_status()


def getSeveralTracks() -> dict:
    pass


def getAudioFeatures() -> dict:
    pass


def getSeveralAudioFeatures() -> dict:
    pass


def getAudioAnalysis() -> dict:
    pass