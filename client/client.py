import grpc
import music_pb2
import music_pb2_grpc

def get_song(song_name):
    channel = grpc.insecure_channel('localhost:50051')
    stub = music_pb2_grpc.MusicServiceStub(channel)
    request = music_pb2.SongRequest(song_name=song_name)
    response = stub.GetSong(request)
    if response.song_name:
        return {
            'song_name': response.song_name,
            'artist': response.artist,
            'album': response.album,
            'album_image': response.album_image,
            'url': response.url
        }
    return None

if __name__ == '__main__':
    song_name = 'Shape of You'
    song = get_song(song_name)
    if song:
        print(f"Song: {song['song_name']}, Artist: {song['artist']}, Album: {song['album']}, URL: {song['url']}, Album Image: {song['album_image']}")
    else:
        print("Song not found.")
