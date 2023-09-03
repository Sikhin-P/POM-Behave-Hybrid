from POM.Base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    account_dropdown = (By.XPATH, '//li/a/strong[contains(text(), "Account")]')
    login_option = (By.LINK_TEXT, 'Login')

    def move_to_login_page(self):
        self.wait_for_element(*self.account_dropdown)
        self.click_element(*self.account_dropdown)
        self.click_element(*self.login_option)

    def verify_home(self):
        element = self.wait_for_element(*self.account_dropdown)
        return element


