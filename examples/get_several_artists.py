import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define artists to get
artistId1 = "73sIBHcqh3Z3NyqHKZ7FOL"
artistId2 = "2YZyLoL8N0Wb9xBt1NhZWg"
artistId3 = "711MCceyCBcFnzjGY4Q7Un"

# get info from response
result = client.artist.getSeveralArtists([artistId1, artistId2, artistId3])
names = [artist["name"] for artist in result["artists"]]
genres = [artist["genres"] for artist in result["artists"]]
popularities = [artist["popularity"] for artist in result["artists"]]

# display relevant info
for i in range(len(names)):
    print("\n#### Artist {} ####".format(i+1))
    print("Name: ", names[i])
    print("Genres: ", ", ".join(genres[i]))
    print("Popularity: ", popularities[i])