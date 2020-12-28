import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define artist to get
artistId = "73sIBHcqh3Z3NyqHKZ7FOL"

# get info from response
result = client.artist.getAlbums(artistId)
albumNames = []
offset = result["offset"]
nextURI = result["next"]
loop = True
while loop:
    if not nextURI: loop = False
    newAlbums= [album["name"] for album in result["items"]]
    albumNames += newAlbums
    offset += len(newAlbums)
    result = client.artist.getAlbums(artistId, offset=offset)
    nextURI = result["next"]

# display relevant info
print("#### Total Albums: {} ####".format(result["total"]))
for i in albumNames:
    print(i)