from spotify.constant import BASE_URL


class PlaylistManager(object):
    """
    Class responsible for managing requests about playlists to the Spotify Web API.
    """

    def __init__(self, client):
        """
        Creates an instance of PlaylistManager.

        Args:
            client (SpotifyClient): The client to send requests to.
        """
        self.client = client

    def getMyPlaylists(self, limit: int = 20, offset: int = 0) -> dict:
        """
        Get all the playlists owned or followed by current Spotify user.

        Requires scope: "playlist-read-private" or "playlist-read-collaborative"

        Args:
            limit (int, optional): The maximum number of tracks to return. Range from [1, 50]. Defaults to 20.
            offset (int, optional): The index of the first track to return. Maximum of 100. Defaults to 0.

        Returns:
            dict: response from Spotify Web API, a collection of playlist objects wrapped in a paging object in json format
        """
        
        # define param and header args for request
        url = BASE_URL + "/me/playlists"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"limit": limit, "offset": offset}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response

    def getPlaylistsOfUser(self, userId: str, limit: int = 20, offset: int = 0) -> dict:
        """
        Get all the playlists owned or followed by the given Spotify user.

        Requires scope: "playlist-read-private" or "playlist-read-collaborative"

        Args:
            userId (str): The Spotify id for the user.
            limit (int, optional): The maximum number of tracks to return. Range from [1, 50]. Defaults to 20.
            offset (int, optional): The index of the first track to return. Maximum of 100. Defaults to 0.

        Returns:
            dict: response from Spotify Web API, a collection of playlist objects wrapped in a paging object in json format
        """

        # define param and header args for request
        url = BASE_URL + "/users/" + userId + "/playlists"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {"limit": limit, "offset": offset}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response

    def getCoverImage(self, playlistId: str) -> dict:
        """
        Get the current cover image for the given playlistId.

        Requires scope: "playlist-read-private" or "playlist-read-collaborative"

        Args:
            playlistId (str): The Spotify id for the playlist.

        Returns:
            dict: response from Spotify Web API, a collection of image objects in json format
        """
        
        # define param and header args for request
        url = BASE_URL + "/playlists/" + playlistId + "/images"
        headers = {"Authorization": "Bearer " + self.client.getCurrentToken()}
        params = {}

        # send request
        response = self.client._sendHTTPRequest("GET", url, params, headers)
        return response

    # Get a Playlist
    def getPlaylist(self, playlistId: str, fields: str = None, market: str = None) -> dict:
        """
        Get a playlist with the given playlistId owned by a Spotify user.

        Args:
            playlistId (str): The Spotify id for the playlist.
            fields (str, optional): Filters for the query. A comma-separated list of fields to return. If omitted, all fields are returned. Defaults to None.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a playlist object in json format
        """
        pass

    # Get a Playlist's Items
    def getPlaylistTracks(self, playlistId: str, fields: str = None, 
                          limit: int = 100, offset: int = 0, market: str = None) -> dict:
        """
        Get full details of the tracks or episodes of the given playlist owned by a Spotify user.

        Args:
            playlistId (str): The Spotify id for the playlist.
            fields (str, optional): Filters for the query. A comma-separated list of fields to return. If omitted, all fields are returned. Defaults to None.
            limit (int, optional): The maximum number of tracks to return. Range from [1, 100]. Defaults to 100.
            offset (int, optional): The index of the first track to return. Defaults to 0.
            market (str, optional): A country code or "from_token"; used for Track Relinking. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a collection of track objects wrapped in a paging object in json format
        """
        pass

    # Create a Playlist
    def createPlaylist(self, userId: str, name: str, public: bool = True, 
                       collaborative: bool = False, description: str = None) -> dict:
        """
        Create a new playlist for the given Spotify user. Playlist is initially empty.

        Args:
            userId (str): The Spotify id for the user.
            name (str): The name for the new playlist.
            public (bool, optional): True if the playlist is public. False if private. Defaults to True.
            collaborative (bool, optional): True if the playlist is collaborative. False, otherwise. Defaults to False.
            description (str, optional): Description of the playlist. Defaults to None.

        Returns:
            dict: response from Spotify Web API, the newly created playlist object in json format
        """
        pass

     # Add Items to a Playlist
    def addTrack(self, playlistId: str, uris: list, position: int = None) -> dict:
        """
        Add one or more tracks to a Spotify user's playlist.

        Args:
            playlistId (str): The Spotify id for the playlist.
            uris (list): List of Spotify uris to add. Maximum of 100.
            position (int, optional): The position to insert the items. If not specified, items are appended to the end. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a snapshot id in json format; used to identify the playlist version in future requests
        """
        pass

    # Remove Items from a Playlist
    def removeTrack(self, playlistId: str, tracks: list, positions: list = None , snapshotId: str = None) -> dict:
        """
        Remove one or more tracks from a Spotify user's playlist.

        Args:
            playlistId (str): The Spotify id for the playlist.
            tracks (list): List of Spotify uris to remove. Maximum of 100.
            positions (list, optional): List of lists of position indexes to remove. Corresponds with tracks. Defaults to None.
            snapshotId (str, optional): The snapshot id of the playlist to make changes to. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a snapshot id in json format; used to identify the playlist version in future requests
        """
        pass

    # Change a Playlist's Details
    def changeDetails(self, playlistId: str, name: str, public: bool, collaborative: bool, description: str):
        """
        Change a playlist's name and public/private state. The playlist must be owned by the Spotify user.

        Args:
            playlistId (str): The Spotify id for the playlist.
            name (str): The name for the new playlist.
            public (bool): True if the playlist is public. False if private.
            collaborative (bool): True if the playlist is collaborative. False, otherwise.
            description (str): Description of the playlist.
        """
        pass

    # Reorder a Playlist's Items
    def reorderPlaylist(self, playlistId: str, rangeStart: int, insertBefore: int, rangeLength: int = 1, snapshotId: str = None) -> dict:
        """
        Reorder a track or group of tracks in a playlist.

        Args:
            playlistId (str): The Spotify id for the playlist.
            rangeStart (int): The position of the first item to be reordered.
            insertBefore (int): The position where the items should be inserted.
            rangeLength (int, optional): The amount of items to be reordered. Defaults to 1.
            snapshotId (str, optional): The snapshot id of the playlist to make changes to. Defaults to None.

        Returns:
            dict: response from Spotify Web API, a snapshot id in json format; used to identify the playlist version in future requests
        """
        pass

    # Replace a Playlist's Items
    def replaceTracks(self, playlistId: str, uris: list):
        """
        Replace all the items in a playlist, overwriting its existing items.

        Args:
            playlistId (str): The Spotify id for the playlist.
            uris (list): List of uris to replace.
        """
        pass

    # Upload a Custom Playlist Cover Image
    def uploadCoverImage(self, playlistId: str, image: str):
        """
        Replace the cover image for the given playlistId.

        Args:
            playlistId (str): The Spotify id for the playlist.
            image (str): Base64 encoded JPEG image data. Maximum payload size is 256 KB.
        """
        pass