import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define album to get
albumId = "6cx4GVNs03Pu4ZczRnWiLd"

# get info from response
result = client.album.getAlbum(albumId)
albumName = result["name"]
artistNames = [artist["name"] for artist in result["artists"]]
releaseDate = result["release_date"]
totalTracks = result["total_tracks"]
popularity = result["popularity"]

# display relevant info
print("Album: ", albumName)
print("Artists: ", ", ".join(artistNames))
print("Release Date: ", releaseDate)
print("Number of Tracks: ", totalTracks)
print("Popularity: ", popularity)