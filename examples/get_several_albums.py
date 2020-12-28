import sys
sys.path.append("C:\\aberr\\projects\\code\\projects\\spotify-api-wrapper")
from spotify.constant import CLIENT_ID, CLIENT_SECRET
from spotify.spotifyClient import SpotifyClient

# create a SpotifyClient
client = SpotifyClient.usingClientCredential(CLIENT_ID, CLIENT_SECRET)

# define albums to get
albumId1 = "6cx4GVNs03Pu4ZczRnWiLd"
albumId2 = "5z090LQztiqh13wYspQvKQ"
albumId3 = "0BwWUstDMUbgq2NYONRqlu"

# get info from response
result = client.album.getSeveralAlbums([albumId1, albumId2, albumId3])
albumNames = [album["name"] for album in result["albums"]]
artistNames = list(map(
    lambda artists: [artist["name"] for artist in artists],  # get list of artists in an artist object
    [album["artists"] for album in result["albums"]]  # list of album objects
))
releaseDates = [album["release_date"] for album in result["albums"]]
totalTracks = [album["total_tracks"] for album in result["albums"]]
popularities = [album["popularity"] for album in result["albums"]]

# display relevant info
for i in range(len(albumNames)):
    print("\n#### Album {} ####".format(i+1))
    print("Album: ", albumNames[i])
    print("Artists: ", ", ".join(artistNames[i]))
    print("Release Date: ", releaseDates[i])
    print("Number of Tracks: ", totalTracks[i])
    print("Popularity: ", popularities[i])