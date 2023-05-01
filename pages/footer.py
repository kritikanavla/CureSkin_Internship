from selenium.webdriver.common.by import By
from pages.base_page import Page


class Footer(Page):

    LINKS_LOCATORS = ['terms-of-service', 'refund-policy', 'privacy-policy', 'shipping-policy']
    LINKS_TEXT = ['Terms of Service', 'Refund policy', 'Privacy Policy', 'Shipping Policy' ]

    def search_footer_links(self):
        index = 0
        for link_locator in self.LINKS_LOCATORS:
            link_text = self.get_text((By.CSS_SELECTOR, f'ul li a[href*="/{link_locator}"'))
            assert link_text == self.LINKS_TEXT[index], f"expected '{self.LINKS_TEXT[index]}' but got {link_text}."
            index = index + 1

    def click_on_links_verify_page(self):
        for link_locator in self.LINKS_LOCATORS:
            self.click((By.CSS_SELECTOR, f'ul li a[href*="/{link_locator}"'))
            actualText = self.get_url()
            print(actualText)
            assert link_locator in actualText, f"{link_locator} is not in url"
        # self.click(self.REFUND_POLICY)
        # actualText = self.get_url()
        # print(actualText)
        # assert "refund-policy" in actualText, f"refund-policy is not in url"
        # self.click(self.PRIVACY_POLICY)
        # actualText = self.get_url()
        # print(actualText)
        # assert "privacy-policy" in actualText, f"privacy-policy is not in url"
        # self.click(self.SHIPPING_POLICY)
        # actualText = self.get_url()
        # print(actualText)
        # assert "shipping-policy" in actualText, f"shipping-policy is not in url"
        #


