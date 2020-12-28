import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define artist to get
artistId = "73sIBHcqh3Z3NyqHKZ7FOL"

# get info from response
result = client.artist.getRelatedArtists(artistId)
artistNames = [artist["name"] for artist in result["artists"]]

# display relevant info
print("#### Related Artists ####")
for name in artistNames:
    print(name)