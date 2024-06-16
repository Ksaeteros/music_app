import requests

def get_song(song_name):
    url = f"https://itunes.apple.com/search?term={song_name}&limit=1"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        song_data = data['results'][0]
        return {
            'song_name': song_data.get('trackName', 'Unknown'),
            'artist': song_data.get('artistName', 'Unknown'),
            'album': song_data.get('collectionName', 'Unknown'),
            'url': song_data.get('previewUrl', '')
        }
    return None

if __name__ == '__main__':
    song_name = 'Shape of You'
    song = get_song(song_name)
    if song:
        print(f"Song: {song['song_name']}, Artist: {song['artist']}, Album: {song['album']}, URL: {song['url']}")
    else:
        print("Song not found.")
