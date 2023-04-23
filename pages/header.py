from selenium.webdriver.common.by import By
from pages.base_page import Page



class Header(Page):
    SHOP_BY_CATEGORY = (By.CSS_SELECTOR, "li:nth-child(3) > menu-drawer > details > summary > span")
    CLICK_BODY = (By.CSS_SELECTOR, "li:nth-child(3) > menu-drawer > details > div > ul > li:nth-child(3) > list-menu-item > a > span")

    def click_shop_by_category(self):
        self.click(self.SHOP_BY_CATEGORY)

    def click_body(self):
        self.click(self.CLICK_BODY)

    def verify_body_in_url(self):
        actualText = self.get_url()
        print(actualText)
        assert "body" in actualText, f"body is not in url"