from POM.Base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    username = (By.NAME, 'email')
    password = (By.NAME, 'password')
    login_button = (By.ID, 'submitBTN')

    def verify_login_page(self):
        element = self.wait_for_element(*self.login_button)
        return element

    def login(self, user_name, user_pass):
        self.wait_for_element(*self.login_button)
        self.type_in(*self.username, value=user_name)
        self.type_in(*self.password, value=user_pass)
        self.click_element(*self.login_button)
