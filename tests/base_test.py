import unittest
import logging

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    base_url = "https://www.abuseipdb.com/check/40.77.190.141"
    wait_time = 5

    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.wait = WebDriverWait(self.driver, self.wait_time)
        self.driver.implicitly_wait(self.wait_time)
        self.logger = logging.getLogger()

    def tearDown(self):
        self.driver.close()
