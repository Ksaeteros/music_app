import unittest
from web.app import app

class MusicAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Music App', response.data)

    def test_search_song(self):
        response = self.app.post('/', data={'song_name': 'Shape of You'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Shape of You', response.data)

if __name__ == '__main__':
    unittest.main()
