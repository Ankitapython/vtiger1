from selenium import webdriver
from resources.data.constant_variables import *

class WebDriverFactory():
    def __init__(self,driver):
        self.driver=driver

    def getWebDriverInstance(self):
        if self.driver == 'firefox':
            driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
        else:
            driver=webdriver.Chrome(executable_path=CHROME_PATH)
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)
        return driver

