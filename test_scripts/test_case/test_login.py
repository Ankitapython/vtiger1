from resources.data.constant_variables import *
from source.pages.login_page import Login_Page
from source.utilities.webdriver_factory import WebDriverFactory

class Login(WebDriverFactory):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def home(self):
        Login_Page(self.driver).login(USER,PASS)
        Login_Page(self.driver).click()