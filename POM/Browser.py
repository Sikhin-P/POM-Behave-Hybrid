from selenium import webdriver


class MyBrowser:
    def __init__(self):
        self.driver = None

    def chrome(self):
        self.driver = webdriver.Chrome()
        return self.driver
