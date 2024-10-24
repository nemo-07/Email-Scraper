import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up undetected-chromedriver
def set_up_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    
    # Initialize undetected chromedriver
    driver = uc.Chrome(options=options)
    return driver

def get__caption(driver, short_url):
    driver.get(short_url)
    
    # Wait for the page to load and captions to appear
    try:
        time.sleep(5)  # Give time for the page to load

        # Locate the caption and hashtags
        caption_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            # (By.XPATH, '//h2[contains(@class, "YtShortsVideoTitleViewModelShortsVideoTitle")]') #for youtube captions
            # (By.XPATH, '//*[@id="metapanel"]/yt-reel-metapanel-view-model/div[1]/yt-reel-channel-bar-view-model/span/a') #for youtube user names
            # (By.XPATH, '//*[@slot="title"]') #Reddit Title
            # (By.XPATH, '//*[@id="t3_1e8lb4n"]/div[1]/span[1]/div/div/span[1]/div/faceplate-hovercard/faceplate-tracker/a') #reddit user name
            
        ))

        # Get the text content of the caption
        caption_text = caption_element.text
        print(caption_text)

    except Exception as e:
        print("    ")
    finally:
        driver.quit()

# Main function
def main():
    Links =['','',''] #list of links
    for link in Links:
            driver = set_up_driver()
            short_url = link  
            get__caption(driver, short_url)

if __name__ == '__main__':
    main()