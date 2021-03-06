#%%
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import pprint
import sys

################### Account Information ######################

cid =' ' # Enter Client ID
secret = ' ' # Enter Client Secret
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
username = ' ' #Enter Username

#############################################################


############### Get Playlist Information ###############

playlists = sp.user_playlists(username)
selected_playlist=input("Enter Playlist Name:")

while playlists:
    for i, playlist in enumerate(playlists['items']):
        if (playlist['name'])==selected_playlist:
            print("The playlist is:",selected_playlist)
            playlist_uri=playlist['uri']
            playlist_id=playlist['id']
            print("The playlist URI is:",playlist_uri)
        else:
            playlists = None

#######################################################


############ Prepare Playlist Lists ###############

track_list=[]
track_id_list=[]
artist_name_list=[]
album_name_list=[]

###################################################


############ Prepare Playlist Dictionary ##############

playlist_dict={}
playlist_dict["artist"]=artist_name_list
playlist_dict["album"]=album_name_list
playlist_dict["name"]=track_list
playlist_dict["id"]=track_id_list

#######################################################


################# Collect Track Information ##############

sp_playlist = sp.user_playlist_tracks(username, playlist_id,)
tracks = sp_playlist['items']
for i in range(len(tracks)):
    track = sp_playlist['items'][i]
    track_album = track['track']['album']['name']
    album_name_list.append(track_album)
    track_artist = track['track']['artists'][0]
    track_artist_name = track_artist['name']
    artist_name_list.append(track_artist_name)
    track_name = track['track']['name']
    track_list.append(track_name)
    track_id = track['track']['id']
    track_id_list.append(track_id)

#############################################################


###### Print Results #######

print(playlist_dict)

###########################


# %%
