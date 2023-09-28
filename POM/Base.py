import time

from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    # function to get single element present in the DOM
    def find_element(self, locator, element):
        try:
            item = self.driver.find_element(locator, element)
            return item
        except NoSuchElementException:
            return None

    def find_elements(self, locator, element):
        try:
            item = self.driver.find_elements((locator, element))
            return item
        except NoSuchElementException:
            return None

    def wait_for_element(self, locator, element):
        try:
            item = WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located((locator, element)))
            return item
        except TimeoutException:
            return None

    def type_in(self, locator, element, value):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, element)))
            item.send_keys(value)
        except ElementNotInteractableException:
            return ElementNotInteractableException

    def click_element(self, locator, element):
        item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, element)))
        time.sleep(1)
        try:
            item.click()
        except ElementNotInteractableException:
            ActionChains(self.driver).move_to_element(item).click(item).perform()

    def hover_on(self, element):
        ActionChains(self.driver).move_to_element(element).perform()