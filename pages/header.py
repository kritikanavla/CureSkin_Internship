from selenium.webdriver.common.by import By
from pages.base_page import Page



class Header(Page):
    SHOP_BY_CATEGORY = (By.CSS_SELECTOR, "li:nth-child(3) details summary span")
    CLICK_BODY = (By.CSS_SELECTOR, "li:nth-child(3) details div div ul li:nth-child(3) a")
    HAMBURGER_MENU = (By.CSS_SELECTOR, "header-drawer span.header__icon")


    def click_shop_by_category(self):
        self.click(self.SHOP_BY_CATEGORY)

    def click_hamburger_menu(self):
        self.click(self.HAMBURGER_MENU)

    def click_body(self):
        self.click(self.CLICK_BODY)

    def verify_body_in_url(self):
        actualText = self.get_url()
        print(actualText)
        assert "body" in actualText, f"body is not in url"

