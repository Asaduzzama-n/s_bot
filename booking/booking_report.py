# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# class BookingReport:
#     def __init__(self, boxes_section_element: WebElement):
#         self.boxes_section_element = boxes_section_element
#         self.deal_boxes = self.pull_deal_boxes()
#
#     def pull_deal_boxes(self):
#         return self.boxes_section_element.find_elements(By.CLASS_NAME,
#                                                         'd20f4628d0'
#                                                         )
#
#     def pull_titles(self):
#         for deal_box in self.deal_boxes:
#             hotel_name_element = deal_box.find_element(By.CLASS_NAME, "fcab3ed991")
#             hotel_name = hotel_name_element.text
#             print("Hotel Name:", hotel_name)

class BookingReport:
    def __init__(self, hotel_boxes: List[WebElement]):
        self.hotel_boxes = hotel_boxes
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return [box.find_elements(By.CLASS_NAME, 'd20f4628d0') for box in self.hotel_boxes]

    def pull_titles(self):
        for deal_boxes in self.deal_boxes:
            for deal_box in deal_boxes:
                hotel_name_element = deal_box.find_element(By.CLASS_NAME, "fcab3ed991")
                hotel_name = hotel_name_element.text
                print("Hotel Name:", hotel_name)

