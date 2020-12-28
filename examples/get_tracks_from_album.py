import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define album to get
albumId = "6cx4GVNs03Pu4ZczRnWiLd"

# get info from response
result = client.album.getTracks(albumId)
trackNames = [track["name"] for track in result["items"]]
artistNames = list(map(
    lambda artists: [artist["name"] for artist in artists],  # get list of artists in an artist object
    [track["artists"] for track in result["items"]]  # list of artist objects
))

# display relevant info
for i in range(len(trackNames)):
    print("\n#### Track {} ####".format(i+1))
    print("{} - {}".format(trackNames[i], ", ".join(artistNames[i])))