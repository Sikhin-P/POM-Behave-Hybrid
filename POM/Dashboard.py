from POM.Base import Base
from selenium.webdriver.common.by import By


class DashBoard(Base):
    logout_button = (By.PARTIAL_LINK_TEXT, 'Logout')

    def verify_dashboard(self):
        element = self.wait_for_element(*self.logout_button)
        return element
