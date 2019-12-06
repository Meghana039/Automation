from idlelib import browser
import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
# import radiobutton.py

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _practice_button = "//a[contains(text(),'Practice')]"

    _radio_id = "bmwradio"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    time.sleep(10)
    def enterEmail(self, email):
        self.sendKeys(email, locator=self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, locator=self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def clickPracticeButton(self):
        self.elementClick(self._practice_button, locatorType="xpath")

    """ def radioClick(self):
       # _val = self.elementClick(self._radio_id, locatorType="id")
        _val = browser.find_elements_by_xpath("//input[@type='radio']")
        print(_val) """

    def login_link(self):
        self.clickLoginLink()

    def login(self,email="", password=""):
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        #self.clickPracticeButton()
        # self.radioClick()

    def verifyLoginSucceeful(self):
        result = self.isElementPresent("//img[@class='gravatar']",
                                       locatorType="xpath")
        return result
    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']",
                                       locatorType="xpath")
        return result




