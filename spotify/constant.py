import os

# define endpoint urls
AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1"

# define response status codes
STATUS_OK = 200
STATUS_CREATED = 201

# define other constants
REFRESH_BUFFER = 120  # in seconds

# FOR DEVELOPMENT
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"
CACHE_PATH = "C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper\\spotify\\cache.json"