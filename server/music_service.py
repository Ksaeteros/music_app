import base64
import grpc
from concurrent import futures
import time
import sys
import os
import requests

# Asegúrarse de que el directorio raíz esté en el PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import music_pb2
import music_pb2_grpc

# Spotify API credentials
CLIENT_ID = '9fac6d644cad40d49028c7df8d96ee36'
CLIENT_SECRET = 'fa2a1702f31840779cc667fae76421ce'


class MusicService(music_pb2_grpc.MusicServiceServicer):
    def __init__(self):
        self.token = self.get_spotify_token()
    
    def get_spotify_token(self):
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_header = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
        response = requests.post(auth_url, data={'grant_type': 'client_credentials'}, headers={'Authorization': f'Basic {auth_header}'})
        response_data = response.json()
        return response_data['access_token']
    
    def GetSong(self, request, context):
        song_name = request.song_name
        url = f"https://api.spotify.com/v1/search?q={song_name}&type=track&limit=1"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data['tracks']['items']:
            song_data = data['tracks']['items'][0]
            return music_pb2.SongResponse(
                song_name=song_data['name'],
                artist=song_data['artists'][0]['name'],
                album=song_data['album']['name'],
                album_image=song_data['album']['images'][0]['url'],
                url=song_data['preview_url'] or ''
            )
        return music_pb2.SongResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    music_pb2_grpc.add_MusicServiceServicer_to_server(MusicService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()