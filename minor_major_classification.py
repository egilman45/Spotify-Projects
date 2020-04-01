
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import pprint
import sys
import requests


################### Account Information ######################

cid =' ' # Client ID
secret = ' ' # Client Secret
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
username = ' ' #Enter Username

#############################################################


############ Gather Playlist Information ################

playlists = sp.user_playlists(username)

selected_playlist=input("Enter Playlist Name:")

while playlists:
    for i, playlist in enumerate(playlists['items']):
        if (playlist['name'])==selected_playlist:
            print("The playlist is:",selected_playlist)
            playlist_uri=playlist['uri']
            playlist_id=playlist['id']
        else:
            playlists = None

########################################################


############ Prepare Playlist Lists ###############

track_list=[]
id_list=[]
uri_list=[]

###################################################


############ Prepare Playlist Dictionary ##############

playlist_dict={}

#######################################################


################# Collect Playlist Information ##############

sp_playlist = sp.user_playlist_tracks(username, playlist_id,)
tracks = sp_playlist['items']

for i in range(len(tracks)):
    track = sp_playlist['items'][i]
    track_name = track['track']['name']
    track_list.append(track_name)

for i in range(len(track_list)):
    
    track = sp_playlist['items'][i]

    ###### Create Dictionary for Track By Name ######
    playlist_dict[track_list[i]]={}

    ###### Add Secetions to the Dictionary ######

    ### Song ID Script ###
    track_id = track['track']['id']
    playlist_dict[track_list[i]]["id"]=track_id
    id_list.append(track_id)

    ### Song URI Script ###
    track_uri = track['track']['uri']
    playlist_dict[track_list[i]]['uri']=track_uri
    uri_list.append(track_uri)

    ### Audio Features Script ###
    track_audio_feat = {}
    playlist_dict[track_list[i]]["audio features"]=track_audio_feat

#############################################################



################ Defining Audio Features of Album Track ###################

for j in range(len(playlist_dict)):

    #Add new key-values to store audio analysis
    playlist_dict[track_list[j]]["audio analysis"] = []
    
    analysis = sp.audio_analysis(id_list[j])

    playlist_dict[track_list[j]]["audio analysis"].append(analysis)
    


#################################################################


########## Requesting Track from User ############

user_track=input("Please Enter a Track Name:")

##################################################


########### Gather Mode Information #############

mode = playlist_dict[user_track]["audio analysis"][0]["track"]["mode"]

#################################################


###### Print Results #######

if mode == 0:
    print("This track is can be classified as a minor track")
elif mode == 1:
    print("This track is can be classified as a major track")
else:
    print("This can not be classified as minor or major")

#############################