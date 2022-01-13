import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
from get_link import *
import os

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))



def create_albums():
	results = sp.current_user_saved_albums(limit=50)
	albums=[]
	for idx, item in enumerate(results['items']):
		id=results["items"][idx]["album"]["id"]
		
		tempDict={
			"name":results["items"][idx]["album"]["name"],
			"id":id
		}
		albums.append(tempDict)

	main_list=[]

	for value in albums:
		tracks=sp.album_tracks(value["id"])
		songs=[]
		for element in tracks["items"]:
			songs.append(element["name"])
		
		
		tempDict={
			"album":value["name"],
			"id":value["id"],
			"songs":songs
		}
		main_list.append(tempDict)
	return main_list


def create_playlists():
	results=sp.current_user_playlists(limit=50)
	playlists=[]
	for idx, item in enumerate(results['items']):
		id=results["items"][idx]["id"]
		tempDict={
			"name":results["items"][idx]["name"],
			"id":id
		}
		playlists.append(tempDict)
	
	main_list=[]
	for value in playlists:
		tracks=sp.playlist_tracks(value["id"])
		songs=[]
		for element in tracks["items"]:
			songs.append(element["track"]["name"])
		
		tempDict={
			"playlist":value["name"],
			"id":value["id"],
			"songs":songs
		}
		main_list.append(tempDict)
	return main_list



#main_list=create_albums(results)





def download_albums(main_list):
	for value in main_list:
		album_name=value["album"]
		os.mkdir(album_name)
		os.chdir(album_name)
		for song in value["songs"]:
			url=get_song(f"{song} {album_name}")
			download(url)
		
def download_playlists(main_list):
	for value in main_list:
		playlist_name=value["playlist"]
		os.mkdir(playlist_name)
		os.chdir(playlist_name)
		for song in value["songs"]:
			url=get_song(f"{song} {playlist_name}")
			download(url)




download_playlists(create_playlists())