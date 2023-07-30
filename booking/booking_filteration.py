from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_category_select(self):
        category_check_box = self.driver.find_element(By.NAME, 'ht_id=204')
        category_check_box.click()

    def apply_star_rating(self, *star_values):
        for star_value in star_values:
            xpath_expression = f'//div[@data-filters-item="class:class={star_value}"]//input'
            checkbox_element = self.driver.find_element(By.XPATH, xpath_expression)
            checkbox_element.click()

    def sort_price_lowest(self):
        button_element = self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
        button_element.click()

        price_button = self.driver.find_element(By.XPATH, '//button[contains(., "Price (lowest first)")]')
        price_button.click()

