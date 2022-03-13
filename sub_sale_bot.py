"""A program for tweeting when Harris Teeter subs are on sale.

    Author: Drew Hughlett
"""

import os
import sys
import tweepy
import platform
from dotenv import load_dotenv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
NORMAL_SUB_PRICE = 6.99
HT_URL = 'https://www.harristeeter.com/orderahead/selectstore/store/330/departmentsGroup/55fa9932ec2c944f582c2785/departments/55faa06f72e49e4958f6865c/categories/5608cffe87a5f77c3ff67592/products?activeTab=items'
CHROME_URL = 'chrome:4444/wd/hub'


def make_driver():
    """Returns a selenium webdriver.

    Returns:
        A webdriver for either a Windows Chrome install
        or a remote instance of Chrome on localhost:4444.
    """
    options = Options()
    options.headless = True
    os = platform.system()

    if os == 'Linux':
        return webdriver.Remote(CHROME_URL, DesiredCapabilities.CHROME, options=options)
    elif os == 'Windows':
        return webdriver.Chrome('./chromedriver', options=options)
    else:
        print(f'sub_sale_bot.py does not support {os}.')
        sys.exit()


def main():
    driver = make_driver()
    driver.get(HT_URL)
    driver.set_page_load_timeout(30)
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="tabs"]/div[3]/order-ahead-items-component/div/div/div/div/ul/li[2]/div/div[2]/div[2]/div[1]/span'))
    )
    current_price = float(element.text[1:5])
    driver.quit()

    if current_price < NORMAL_SUB_PRICE:
        load_dotenv(os.path.join(CURRENT_DIRECTORY, '.env'))
        auth = tweepy.OAuthHandler(os.environ['API'], os.environ['APISecret'])
        auth.set_access_token(
            os.environ['AccessToken'], os.environ['AccessTokenSecret'])
        api = tweepy.API(auth)

        # Include the date to avoid a duplicate tweet
        date = str(datetime.today().strftime('%x'))
        api.update_status(
            f'{date}\nHarris Teeter subs are on sale for ${current_price}')


if __name__ == "__main__":
    main()
