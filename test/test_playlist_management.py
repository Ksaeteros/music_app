import unittest
from selenium import webdriver

class TestPlaylistManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:5000/login')
        cls.driver.find_element_by_name('username').send_keys('saeteros')
        cls.driver.find_element_by_name('password').send_keys('619295')
        cls.driver.find_element_by_name('login').click()
        cls.driver.get('http://localhost:5000/playlist')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_delete_song_from_playlist(self):
        delete_button = self.driver.find_element_by_name('delete_song')
        delete_button.click()
        success_message = self.driver.find_element_by_class_name('flash-message')
        self.assertTrue(success_message.is_displayed())

if __name__ == '__main__':
    unittest.main()
