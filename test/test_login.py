import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000/login')

    def tearDown(self):
        self.driver.quit()

    def test_login_valid_credentials(self):
        self.driver.get('http://localhost:5000/login')
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys('ksaeteros')
        password.send_keys('123')
        submit_button.click()

        WebDriverWait(self.driver, 20).until(EC.url_matches('http://localhost:5000/index'))

        # Verifica que la URL sea la correcta después del inicio de sesión
        self.assertEqual(self.driver.current_url, 'http://localhost:5000/index')

if __name__ == "__main__":
    unittest.main()