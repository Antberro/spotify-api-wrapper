import os

# define endpoint urls
TOKEN_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1"

# define response status codes
STATUS_OK = 200
STATUS_CREATED = 201

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")