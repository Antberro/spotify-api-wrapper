import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define tracks to get
trackId = "1LeWIs2hP2r5yOQnVuYoI5"

# get info from response
result = client.track.getAudioAnalysis(trackId)

# display relevant info
for key in result.keys():
    print("\n{}".format(key))
    print(result[key])