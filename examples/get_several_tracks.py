import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define tracks to get
trackId1 = "1LeWIs2hP2r5yOQnVuYoI5"
trackId2 = "0qdQUeKVyevrbKhAo0ibxS"
trackId3 = "6Ac4NVYYl2U73QiTt11ZKd"

# get info from response
result = client.track.getSeveralTracks([trackId1, trackId2, trackId3])
trackNames = [track["name"] for track in result["tracks"]]
albumNames = [track["album"]["name"] for track in result["tracks"]]
artistNames = list(map(
    lambda artists: [artist["name"] for artist in artists],  # get list of artists in an artist object
    [track["artists"] for track in result["tracks"]]  # list of artist objects
))

# display relevant info
for i in range(len(trackNames)):
    print("\n#### Track {} ####".format(i+1))
    print("Track: ", trackNames[i])
    print("Album: ", albumNames[i])
    print("Artists: ", ", ".join(artistNames[i]))