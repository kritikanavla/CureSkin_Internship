import allure
import self as self
from allure_commons.types import AttachmentType
from selenium.webdriver.firefox.options import Options

from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from support.logger import logger, MyListener


# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    print('before drive extraction')

    #service = Service(r"C:\Users\virat\source\chromedriver\chromedriver.exe")
    service = Service(r"C:\Users\virat\source\geckodriver\geckodriver.exe")
    options = Options()
    #options.headless = True
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Chrome(service=service, chrome_options=options)
    # context.driver = webdriver.Chrome(service=service)
    #context.driver = webdriver.Firefox( service=service, options=options)

    context.driver = EventFiringWebDriver(
        webdriver.Firefox(service=service, options=options),
        MyListener()
        )

    # desrired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "11",
    #     },
    #     'name': test_name
    # }

    # bs_user = 'kritikanavla_y0rCWl'
    # bs_key = 'LNhSDjgYxa3NTJwv91b9'
    # url = f"https://{bs_user}:{bs_key}@hub.browserstack.com/wd/hub"
    # context.driver = webdriver.Remote(url, desired_capabilities=desrired_cap)
    # context.browser = webdriver.Safari()
    print('Browser driver extracted')

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    print('before app init')
    context.app = Application(driver=context.driver)




def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    #print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Started step: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
