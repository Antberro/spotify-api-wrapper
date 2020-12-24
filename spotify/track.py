from spotify.constant import BASE_URL
from spotify.clientCredentialFlow import ClientCredentialFlow

def getTrack(id: str, market: str = None) -> dict:
    """
    Get the track with the given Spotify id.

    Args:
        id (str): The Spotify id for the track.
        market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

    Returns:
        dict: response from Spotify Web API, a track object in json format
    """
    pass

def getSeveralTracks() -> dict:
    pass

def getAudioFeatures() -> dict:
    pass

def getSeveralAudioFeatures() -> dict:
    pass

def getAudioAnalysis() -> dict:
    pass