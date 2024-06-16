import grpc
from concurrent import futures
import time
import sys
import os
import requests

# Asegúrate de que el directorio raíz esté en el PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import music_pb2
import music_pb2_grpc

class MusicService(music_pb2_grpc.MusicServiceServicer):
    def GetSong(self, request, context):
        song_name = request.song_name
        url = f"https://itunes.apple.com/search?term={song_name}&limit=1"
        response = requests.get(url)
        data = response.json()
        if data['results']:
            song_data = data['results'][0]
            return music_pb2.SongResponse(
                song_name=song_data.get('trackName', 'Unknown'),
                artist=song_data.get('artistName', 'Unknown'),
                album=song_data.get('collectionName', 'Unknown'),
                album_image=song_data.get('artworkUrl100', ''),
                url=song_data.get('previewUrl', '')
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
