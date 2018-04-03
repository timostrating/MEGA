from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

username = "______"
password = "______"  

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.hanze.nl")

# the page is ajaxy so the title is originally this:
print " -- " + driver.title

login_button = driver.find_element_by_css_selector('a.ng-binding')
login_button.click()

print " -- " + driver.title


username_field = driver.find_element_by_id('input_1')
username_field.clear()
username_field.send_keys(username)

password_field = driver.find_element_by_id('input_2')
password_field.clear()
password_field.send_keys(password)

submit_button = driver.find_element_by_css_selector('input.credentials_input_submit')
submit_button.click()

print driver.get_cookies()


try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()




