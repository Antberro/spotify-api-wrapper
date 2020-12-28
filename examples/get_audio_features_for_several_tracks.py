import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define tracks to get audio features of
trackId1 = "1LeWIs2hP2r5yOQnVuYoI5"
trackId2 = "0qdQUeKVyevrbKhAo0ibxS"
trackId3 = "6Ac4NVYYl2U73QiTt11ZKd"

# get info from response
result = client.track.getSeveralAudioFeatures([trackId1, trackId2, trackId3])

# display relevant info
for i, trackInfo in enumerate(result["audio_features"]):
    print("\n#### Track {} ####".format(i+1))
    for feature in trackInfo:
        print("{} : {}".format(feature, trackInfo[feature]))
