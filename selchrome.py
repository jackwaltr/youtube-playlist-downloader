from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def downloadYoutube(file):
    options = Options()
    prefs = {'profile.default_content_setting_values.notifications' : 2,
             'download.default_directory' : '/your/path/to/downloads'}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(options=options, executable_path='/your/path/to/chromedriver')

    browser.get('https://ytmp3.cc/')
    f = open(file,'r')
    f1 = f.readlines()

    for link in f1:
        browser.get('https://ytmp3.cc/')
        browser.switch_to.window(browser.window_handles[0])
        inp = browser.find_element(By.ID, "input")
        browser.switch_to.window(browser.window_handles[0])
        inp.send_keys(link)
        browser.switch_to.window(browser.window_handles[0])
        elem = None
        try:
            elem = WebDriverWait(browser, 180).until(EC.element_to_be_clickable((By.ID, "download")))
        except:
            browser.quit()
        elem.click()
        time.sleep(2)
    time.sleep(5)
