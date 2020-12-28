import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define track to get audio features of
trackId = "1LeWIs2hP2r5yOQnVuYoI5"

# get info from response
result = client.track.getAudioFeatures(trackId)

# display relevant info
for feature in result.keys():
    print("{} : {}".format(feature, result[feature]))