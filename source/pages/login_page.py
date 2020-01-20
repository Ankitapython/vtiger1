'''
@author: Ankita M
@date:9/01/2020
'''

import time

import logging

from source.utilities.generic_methods import GenericMethods
from source.utilities import custom_logger as cv

class Login_Page(GenericMethods):
    log = cv.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.btn="//input[@id='submitButton']"

    def login(self,user,passwd):
        self.sendkeys(user,"user_name","name")
        self.sendkeys(passwd,"user_password","name")

    def click(self):
        self.elementClick(self.btn,"xpath")












