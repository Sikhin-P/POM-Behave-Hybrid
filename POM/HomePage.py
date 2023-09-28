from POM.Base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    account_dropdown = (By.XPATH, '//li/a/strong[contains(text(), "Account")]')
    login_option = (By.LINK_TEXT, 'Login')
    logout_option = (By.LINK_TEXT, 'Logout')
    logout_success = (By.CSS_SELECTOR, 'div[class *="success"]')
    login_fail = (By.CSS_SELECTOR, 'div[class *= "error"]')

    def move_to_login_page(self):
        self.wait_for_element(*self.account_dropdown)
        self.click_element(*self.account_dropdown)
        self.click_element(*self.login_option)

    def verify_home(self):
        element = self.wait_for_element(*self.account_dropdown)
        return element

    def logout(self):
        self.wait_for_element(*self.account_dropdown)
        self.click_element(*self.account_dropdown)
        self.click_element(*self.logout_option)

    def verify_logout(self):
        element = self.wait_for_element(*self.logout_success)
        if element is None:
            return False
        else:
            return True

    def invalid_login(self):
        element = self.wait_for_element(*self.login_fail)
        if element is None:
            return False
        else:
            return True
