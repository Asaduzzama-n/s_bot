from selenium.webdriver.common.by import By
import time
import booking.constants as const
import os
from selenium import webdriver

from booking.booking_filteration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"E:\Python_project\drivers", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
                                             'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        usd_btn = self.find_element(By.CSS_SELECTOR,
                                    'button[data-testid="selection-item"]')
        usd_btn.click()

    time.sleep(2)

    def select_place_to_go(self, place_to_go):
        search_field_place = self.find_element(By.NAME, 'ss')
        search_field_place.clear()
        search_field_place.send_keys(place_to_go)
        time.sleep(1)
        # Find all the list items with class "a80e7dc237" under the unordered list
        list_items = self.find_elements(By.CSS_SELECTOR,
                                        'ul[data-testid="autocomplete-results"] li.a80e7dc237')
        # Choose and click on the second list item (index 1)
        first_list_item = list_items[0]
        first_list_item.click()

    def select_date(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR,
                                             f'[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR,
                                              f'[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_element.click()

        adult_plus_btn = self.find_element(By.CSS_SELECTOR, '#group_adults + div + div button:last-child')
        adult_minus_btn = self.find_element(By.CSS_SELECTOR, '#group_adults + div + div button:first-child')

        while True:
            adult_minus_btn.click()
            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute('value')
            print(adults_value)
            if int(adults_value) == 1:
                print('breaking')
                break

        for i in range(count - 1):
            print(i)
            adult_plus_btn.click()

    def click_search(self):
        self.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        time.sleep(3)
        filtration.apply_category_select()
        filtration.apply_star_rating(5, 4, 3)
        time.sleep(2)
        filtration.sort_price_lowest()
