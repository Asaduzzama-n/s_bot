from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_category_select(self):
        hotel_check_box = self.driver.find_element(By.NAME, 'ht_id=204')
        hotel_check_box.click()
