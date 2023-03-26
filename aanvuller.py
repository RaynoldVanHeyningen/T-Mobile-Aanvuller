from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime
import psutil

opts = Options()
opts.add_experimental_option("detach", True)
opts.add_argument('--headless')

browser = webdriver.Chrome(options=opts)

# Get the process ID of the current script
pid = psutil.Process()


def aanvuller():
    try:
        # print(datetime.datetime.now().strftime(
        #     "%Y-%m-%d %H:%M:%S") + ' - Checking aanvuller')
        start_bytes_sent = psutil.net_io_counters().bytes_sent

        # Wait for aanvuller available
        refreshButton = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@data-interaction-id='aanvullers_pricebundle']"))
        )  # wait for page to load, so element with ID 'username' is visible

        # print(datetime.datetime.now().strftime(
        #     "%Y-%m-%d %H:%M:%S") + ' - Aanvuller available')
        refreshButton.click()

        # Wait for aanvuller to be loaded
        aanvullerPopup = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@data-action='BuyRoamingBundle']"))
        )

        aanvullerPopup.click()
        end_bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_sent_by_script = end_bytes_sent - start_bytes_sent
        kilobytes_sent_by_script = bytes_sent_by_script / 1024
        print(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") + ' - Aanvuller paid [' + str(kilobytes_sent_by_script) + ' KB]')
        # aanvuller()
    except:

        # Get the network usage statistics for the script's process ID
        end_bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_sent_by_script = end_bytes_sent - start_bytes_sent
        kilobytes_sent_by_script = bytes_sent_by_script / 1024
        print(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") + ' - Aanvuller not available [' + str(kilobytes_sent_by_script) + ' KB]')
        # time.sleep(5)
        # browser.refresh()
        # aanvuller()


try:
    url = 'https://www.t-mobile.nl/aanvuller'
    browser.get(url)

    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, "Row1_Column1_Cell1_CookieSettings_AdvancedSaveAccept"))
    )  # wait for page to load, so element with ID 'username' is visible

    # Accept cookies
    cookieAccept = browser.find_element(By.ID,
                                        'Row1_Column1_Cell1_CookieSettings_AdvancedSaveAccept')
    cookieAccept.click()

    # Run aanvuller function
    aanvuller()
except:
    print(datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S") + ' - Error')
    browser.quit()
