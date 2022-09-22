import time

import pandas as pd
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.base_test import BaseTest


class BotDetector(BaseTest):
    SEARCH_BOX = (By.CSS_SELECTOR, 'input:not([id]).form-control')
    CHECK_BUTTON = (By.CLASS_NAME, 'input-group-btn')
    RESULT_TABLE = (By.CSS_SELECTOR, 'td:not([data-title]):not([class])')

    input_file = "files/demo_bot.xlsx"
    output_file = "files/output.xlsx"
    search_keys = ["bot", "crawler", "Search Engine Spider"]
    result_text = []
    ip_addresses = []
    bot_addresses = []

    def read_excel(self):
        self.ip_addresses = pd.read_excel(self.input_file, sheet_name='Sheet1', na_values="ip").ip

    def write_excel(self, datas):
        df = pd.DataFrame({'Bot': datas})
        writer = pd.ExcelWriter(self.output_file, engine='openpyxl')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()

    def find_element(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def get_table_texts(self):
        time.sleep(1)
        elements = self.wait.until(ec.presence_of_all_elements_located(self.RESULT_TABLE))
        for element in elements:
            self.result_text.append(element.accessible_name)

    def test_bot_detector(self):
        self.read_excel()
        for ip_address in self.ip_addresses:
            self.find_element(self.SEARCH_BOX).send_keys(ip_address)
            self.find_element(self.CHECK_BUTTON).click()
            try:
                self.get_table_texts()
            except TimeoutException:
                self.bot_addresses.append(ip_address + " tekrar kontrol etmelisin!")
            for search in self.search_keys:
                for result in self.result_text:
                    if search.lower() in result.lower():
                        self.bot_addresses.append(ip_address)
            self.result_text.clear()

    def tearDown(self):
        self.write_excel(self.bot_addresses)
