import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

import requests
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()


def search_weather_coordinates(lat: float, lon: float):

    api_key = 'b77e07f479efe92156376a8b07640ced'
    uri = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, api_key)

    result = requests.get(uri)
    result_json = result.json()

    return result_json


def search_weather_city(city: str):

    api_key = 'b77e07f479efe92156376a8b07640ced'
    uri = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)

    result = requests.get(uri)
    result_json = result.json()

    return result_json


def kelvin_x_celsius(kelvin_temp):

    # ºC = K - 273.
    celsius_temp = kelvin_temp - 273

    return celsius_temp


def auth():

    client_id = 'd1330b0db13e424caf21a9e986fae4ac'
    client_secret = '1241a6647bb94b3f9ed13daf002b223c'

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                          client_secret=client_secret)
    spot = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
    return spot



def get_playlists(celsius_temp):

    spot_auth = auth()

    # ~ lista de categorias ~ categories = spot_auth.categories(country=None, locale=None, limit=50, offset=1)
    
    category = ''

    if (celsius_temp > 30):
        category = 'party'
    elif (celsius_temp >= 15 and celsius_temp <= 30):
        category = 'pop'
    elif (celsius_temp >= 10 and celsius_temp <= 14):
        category = 'rock'
    else:
        category = 'classical'


    cat_playlists = spot_auth.category_playlists(category_id=category,
                                                country=None, limit=50, offset=1)
    arr_id_playlists = []

    for elem in cat_playlists['playlists']['items']:
        arr_id_playlists.append(elem['id'])
        

    return arr_id_playlists



def get_tracks(celsius_temp):

    arr_playlists = get_playlists(celsius_temp)
    spot_auth = auth()

    username = 'tarcisio.souto'

    tracks_playlist = spot_auth.user_playlist_tracks(username, playlist_id=arr_playlists[0])['items']
        
    dict_tracks = {}

    for track in tracks_playlist:
            
        dict_tracks[track["track"]["id"]] = track["track"]["name"]
    
    json_tracks = jsonable_encoder(dict_tracks)
    
    return json_tracks
  


@app.post('/longitudinal_coordinates/{lat},{lon}')
def callback_weather_coordinates(lat: float, lon: float):

    callback_swc = search_weather_coordinates(lat, lon)["main"]["temp"]
    celsius_temp = int(kelvin_x_celsius(callback_swc))
    list_tracks = get_tracks(celsius_temp)

    return list_tracks


@app.post('/city_name/{city}')
def callback_weather_city(city: str):

    callback_swc = search_weather_city(city)["main"]["temp"]
    celsius_temp = int(kelvin_x_celsius(callback_swc))
    list_tracks = get_tracks(celsius_temp)
    
    return list_tracks
    