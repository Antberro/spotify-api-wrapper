import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define artist to get
artistId = "73sIBHcqh3Z3NyqHKZ7FOL"

# get info from response
result = client.artist.getArtist(artistId)
name = result["name"]
genres = result["genres"]
popularity = result["popularity"]

# display relevant info
print("Artist: ", name)
print("Genres: ", ", ".join(genres))
print("Popularity: ", popularity)
