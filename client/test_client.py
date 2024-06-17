import unittest
from unittest.mock import patch
from client.client import get_song

class ClientTestCase(unittest.TestCase):

    @patch('client.client.MusicServiceStub')
    def test_get_song(self, mock_stub):
        # Crear un mock del método GetSong
        mock_stub.return_value.GetSong.return_value = {
            'song_name': 'Shape of You',
            'artist_name': 'Ed Sheeran',
            'album_name': 'Divide',
            'preview_url': 'http://example.com/preview',
            'album_image': 'http://example.com/image.jpg'
        }

        song = get_song('Shape of You')
        self.assertIsNotNone(song)
        self.assertEqual(song['song_name'], 'Shape of You')

if __name__ == '__main__':
    unittest.main()
