'''
Email Content Reader 
'''
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

# Set Arguments
def set_args():
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
    return options

# Undectectable Driver
def create_driver(options):
    driver = uc.Chrome(options=options)
    driver.get('https://mail.google.com')
    return driver

#Scrape info and print
def get_info(driver):
    main = {} 
    Ds = {}

    table = driver.find_element(By.XPATH, '//table[@id=":28"]')  # Adjust the XPath as necessary //*[@id=":4v"] //table[@id=":28"]
    rows = table.find_elements(By.XPATH, './/tr')

    for index, row in enumerate(rows):
        try:
            row.click()
            time.sleep(3) 

            sender_email = driver.find_element(By.XPATH, '//span[@class="go"]')

            subject = driver.find_element(By.XPATH, '//h2[@class="hP"]')

            email_content = driver.find_element(By.XPATH, '//div[@class="ii gt"]')
            
            Ds["Address"] = sender_email.text
            Ds["Subject"] = subject.text
            Ds["Content"] = email_content.text
            
            main[index] = Ds
            
            driver.back()
            time.sleep(3) 
            
            table = driver.find_element(By.XPATH, '//table')
            rows = table.find_elements(By.XPATH, './/tr')

        except Exception as e:
            print(f"An error occurred for row {index + 1}: {e}")
            
    print(main)
    time.sleep(10)
    driver.quit()

def main():
    options = set_args()
    driver = create_driver(options)
    get_info(driver)
    
if __name__ == '__main__':
    main()