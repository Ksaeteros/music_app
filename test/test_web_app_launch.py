import unittest
from selenium import webdriver

class TestWebAppLaunch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:5000')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_load(self):
        self.assertIn("Login", self.driver.title)
        login_button = self.driver.find_element_by_name('login')
        self.assertTrue(login_button.is_displayed())

if __name__ == '__main__':
    unittest.main()
