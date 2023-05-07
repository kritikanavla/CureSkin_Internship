from pages.base_page import Page
from support.logger import logger

class MainPage(Page):
    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        logger.info(f'Opening url: https://shop.cureskin.com/')

