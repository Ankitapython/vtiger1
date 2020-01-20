from telnetlib import EC
from traceback import print_stack

from selenium.common.exceptions import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import source.utilities.custom_logger as cl
import logging
import time,os

class GenericMethods():
    log= cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    def screenshots(self,resultMessage):
        fileName= resultMessage+"."+str(round(time.time() * 1000))+ ".png"
        screenshotDirectory="../screenshots/"
        relativeFileName=screenshotDirectory+fileName
        currentDirectory=os.path.dirname(__file__)
        destinationFile=os.path.join(currentDirectory,relativeFileName)
        destinationDirectory=os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory:"+ destinationFile)
        except:
            self.log.error("###  Expection occured")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("locator type"+ locatorType+ "not correct/supported")

    def getElement(self,locator,locatorType="id"):
        element=None
        try:
            locatorType = locatorType.lower()
            byType =self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element found with locator:"+ locator +"and locator Type" + locatorType)
        except:
            self.log.info("Element not found with locator" + locator +"and locator Type" + locatorType)
        return element

    def clearText(self,locator,locatorType="id"):
        try:
            self.getElement(locator,locatorType).clear()
            self.log.info("The text field is clear with locator:"+ locator +"and locator Type" + locatorType)
        except:
            self.log.info("##not  able to clear ##")
            print_stack()

    def elementClick(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on element with locator:" + locator + "and locator Type" + locatorType)
        except:
            self.log.info("## cannot click on the element"+ locator + "and locator Type" + locatorType)
            print_stack()

    def iselementPresent(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            print_stack()

    def switch_to_child_window(self,driver):
        child_window=None
        parent_window=driver.current_window_handle
        windows_ids= driver.window_handles
        try:
            for windows_id in windows_ids:
                if windows_id != parent_window:
                    child_window = windows_id
                    break
            driver.switch_to.window(child_window)
        except Exception:
            self.log.info("Unale to change focus to the child window")
            print_stack()

    def timeSleep(self):
        time.sleep(3)

    def elementPresenceCheck(self, locator, byType):
        try:
            elementlist= self.find_elements(byType,locator)
            if len(elementlist)>0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self,locator,locatorType="id",timeout=10,pollFrequency=0.5):
        element=None
        try:
            byType=self.getByType(locatorType)
            self.log.info("waiting for maximum ::" + str(timeout)+"::scondsnfor elemnt to be clickable")
            wait = WebDriverWait(self.driver,timeout,poll_frequency=pollFrequency,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
            element=wait.until(EC.element_to_be_clickable((byType,locator)))
            self.log.info("Element appeared on to web page")
        except:
            self.log.info("Element not appeared on to web page")
            print_stack()
        return element

    def sendkeys(self,data,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator:"+locator+"locator Type"+locatorType)
        except:
            self.log.info("Cannot send data on element with locator:" + locator + "locator Type" + locatorType)
            print_stack()

    def isElementPresent(self,locator,locatorType):
        try:
            element=self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("element found")
                return True
            else:
                self.log.info("element  not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def get_Text(self,locator,locatorType="id"):
        text=None
        try:
            element=self.getElement(locator,locatorType)
            text=element.text
            self.log.info("Able to fetch the text")
        except:
            self.log.info("Cannot able to get the text")
        return text

























