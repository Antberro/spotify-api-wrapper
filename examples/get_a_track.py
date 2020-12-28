import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define track to get
trackId = "1LeWIs2hP2r5yOQnVuYoI5"

# get info from response
result = client.track.getTrack(trackId)
trackName = result["name"]
albumName = result["album"]["name"]
artistNames = [artist["name"] for artist in result["artists"]]

# display relevant info
print("Track: ", trackName)
print("Album: ", albumName)
print("Artists: ", ", ".join(artistNames))