from pages.header import Header
from pages.main_page import MainPage
from pages.footer import Footer


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.footer = Footer(self.driver)
