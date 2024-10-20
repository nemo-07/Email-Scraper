'''
Extract Mail Content Of An Email
'''
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = uc.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/niharikarana/Library/Application Support/Google/Chrome/Profile 1")  # Update with the actual path
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = uc.Chrome(options=options)

#Open gmail; make sure you're logged in your desired chrome profile
driver.get('https://mail.google.com')

time.sleep(10)

# Select an unread email
first_email = driver.find_element(By.XPATH, '//tr[@class="zA yO"]') 
first_email.click()

time.sleep(3)

#Extract mail contents
sender_email = driver.find_element(By.XPATH, '//span[@class="go"]')

subject = driver.find_element(By.XPATH, '//h2[@class="hP"]')

email_content = driver.find_element(By.XPATH, '//div[@class="ii gt"]')

#Print contents
print("Sender's Email:", sender_email.text)
print("Subject:", subject.text)
print("Content:", email_content.text)

time.sleep(10)
driver.quit()