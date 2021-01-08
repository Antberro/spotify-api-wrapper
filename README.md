# SPOTIFY-API-WRAPPER

An API wrapper of the Spotify Web API. It currently covers a subset of the available topics in the API. The follwing topics have full or partial support.

* Track
* Artist
* Album
* Playlist
* Library

## Creating a SpotifyClient

The wrapper consists of the SpotifyClient object. A client can be created using various authentication flows. Currently implements the Client Credential Flow and Authorization Code Flow.

### Client Credential Flow

The client credential flow is used to access non-user information, such as data from the Spotify catalog.

```python
from spotify.spotifyClient import SpotifyClient

CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Client Secret"

client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)
```

### Authorization Code Flow

The authorization code flow is used to access user information, requiring a user to login to their Spotify account.

```python
from spotify.spotifyClient import SpotifyClient

CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Client Secret"
REDIRECT_URI = "Your Redirect URI"
SCOPE = "user-library-read"

client = SpotifyClient.usingAuthorizationCode(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE)
```
