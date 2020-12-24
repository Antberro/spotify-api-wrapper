import os

# define endpoint urls
TOKEN_URL = "https://accounts.spotify.com/api/token"

# define response status codes
STATUS_OK = 200
STATUS_CREATED = 201

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")