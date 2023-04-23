class Page:
    def __init__(self, driver):
        self.driver = driver



    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_url(self):
        return self.driver.current_url


    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_unit_element_visibility(self, visibility, message):
        self.driver.wait.until(visibility, message)
