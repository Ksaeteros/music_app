import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestMusicSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:5000/login')
        cls.driver.find_element_by_name('username').send_keys('valid_user')
        cls.driver.find_element_by_name('password').send_keys('valid_password')
        cls.driver.find_element_by_name('login').click()
        cls.driver.get('http://localhost:5000/search')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_song(self):
        search_box = self.driver.find_element_by_name('song_name')
        search_box.send_keys('Shape of You')
        search_box.send_keys(Keys.RETURN)
        song_result = self.driver.find_element_by_class_name('song-result')
        self.assertTrue(song_result.is_displayed())

if __name__ == '__main__':
    unittest.main()
