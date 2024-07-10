import base64
import grpc
from concurrent import futures
import sys
import os
import requests
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)

# Asegurarse de que el directorio raíz esté en el PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import music_pb2
import music_pb2_grpc

# Spotify API credentials
CLIENT_ID = '9fac6d644cad40d49028c7df8d96ee36'
CLIENT_SECRET = 'fa2a1702f31840779cc667fae76421ce'

class MusicService(music_pb2_grpc.MusicServiceServicer):
    def __init__(self):
        logging.info("Inicializando el servicio de música")
        self.token = self.get_spotify_token()
    
    def get_spotify_token(self):
        logging.info("Obteniendo token de Spotify")
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_header = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
        response = requests.post(auth_url, data={'grant_type': 'client_credentials'}, headers={'Authorization': f'Basic {auth_header}'})
        response_data = response.json()
        token = response_data['access_token']
        logging.info("Token obtenido correctamente")
        return token
    
    def GetSong(self, request, context):
        logging.info(f"Buscando canción: {request.song_name}")
        song_name = request.song_name
        url = f"https://api.spotify.com/v1/search?q={song_name}&type=track&limit=1"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data['tracks']['items']:
            song_data = data['tracks']['items'][0]
            logging.info(f"Canción encontrada: {song_data['name']} de {song_data['artists'][0]['name']}")
            return music_pb2.SongResponse(
                song_name=song_data['name'],
                artist=song_data['artists'][0]['name'],
                album=song_data['album']['name'],
                album_image=song_data['album']['images'][0]['url'],
                url=song_data['preview_url'] or ''
            )
        logging.info("Canción no encontrada")
        return music_pb2.SongResponse()
    
    def GetFeaturedAlbums(self, request, context):
        logging.info("Obteniendo álbumes destacados")
        url = "https://api.spotify.com/v1/browse/new-releases?limit=10"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        albums = []
        
        for album in data['albums']['items']:
            albums.append(music_pb2.Album(
                album_name=album['name'],
                artist=album['artists'][0]['name'],
                album_image=album['images'][0]['url']
            ))
        logging.info(f"{len(albums)} álbumes destacados encontrados")
        return music_pb2.AlbumList(albums=albums)

def serve():
    logging.info("Iniciando el servidor gRPC")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    music_pb2_grpc.add_MusicServiceServicer_to_server(MusicService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Servidor gRPC iniciado y esperando conexiones en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
