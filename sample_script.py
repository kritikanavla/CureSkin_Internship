from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

#driver.implicitly_wait(5)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
#sleep(4)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# click search
driver.find_element(By.NAME, 'btnK').click()

#driver.implicitly_wait(0)
# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
