import grpc
from concurrent import futures
import time
import sys
import os

# Asegúrate de que el directorio raíz esté en el PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import music_pb2
import music_pb2_grpc

class MusicService(music_pb2_grpc.MusicServiceServicer):
    def GetSong(self, request, context):
        # Implementación de la lógica para obtener la canción
        song_data = {
            'song_name': request.song_name,
            'artist': 'Unknown Artist',
            'album': 'Unknown Album',
            'url': 'http://example.com/song.mp3'
        }
        return music_pb2.SongResponse(**song_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    music_pb2_grpc.add_MusicServiceServicer_to_server(MusicService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
