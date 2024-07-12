import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestAddMusic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:5000/login')
        cls.driver.find_element_by_name('username').send_keys('ksaeteros')
        cls.driver.find_element_by_name('password').send_keys('123')
        cls.driver.find_element_by_name('login').click()
        cls.driver.get('http://localhost:5000/search')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_song_to_playlist(self):
        search_box = self.driver.find_element_by_name('song_name')
        search_box.send_keys('Shape of You')
        search_box.send_keys(Keys.RETURN)
        add_button = self.driver.find_element_by_name('add_to_playlist')
        add_button.click()
        success_message = self.driver.find_element_by_class_name('flash-message')
        self.assertTrue(success_message.is_displayed())

if __name__ == '__main__':
    unittest.main()
