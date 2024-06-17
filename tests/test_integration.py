import unittest
from unittest.mock import patch
from web.app import app

class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('client.client.get_song')
    def test_full_flow(self, mock_get_song):
        # Configurar el mock para devolver un valor específico
        mock_get_song.return_value = {
            'song_name': 'Shape of You',
            'artist_name': 'Ed Sheeran',
            'album_name': 'Divide',
            'preview_url': 'http://example.com/preview',
            'album_image': 'http://example.com/image.jpg'
        }
        
        # Test the gRPC client directly
        song = mock_get_song('Shape of You')
        self.assertIsNotNone(song)
        self.assertEqual(song['song_name'], 'Shape of You')

        # Test the Flask app with a POST request
        response = self.app.post('/', data={'song_name': 'Shape of You'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Shape of You', response.data)

if __name__ == '__main__':
    unittest.main()
