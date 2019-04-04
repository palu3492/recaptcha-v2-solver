from selenium import webdriver
from SplitImage import *
from ImageLabeling import *
from ControlRecaptchaIframe import *
import urllib.request
import time

class NewMain:

    def __init__(self):
        self.url = 'https://www.mozilla.org/' #input('Enter website url:\n') #'https://www.google.com/recaptcha/api2/demo' 'https://patrickhlauke.github.io/recaptcha/'
        self.web_driver = webdriver.Chrome('files/chromedriver.exe')
        self.control_recaptcha = ControlRecaptchaIframe(self.web_driver)

    def check_website(self):
        # Navigate web driver to url
        self.web_driver.get(self.url)
        # Look for recaptcha iframe on website
        try:
            self.web_driver.find_element_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/']")
            return True
        except:
            return False

    def open_recaptcha_iframe(self):
        # Find recaptcha button iframe
        captcha_iframe = self.web_driver.find_element_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/']")
        # Switch to recaptcha button iframe
        self.web_driver.switch_to.frame(captcha_iframe)
        check_box = self.web_driver.find_element_by_class_name('recaptcha-checkbox-checkmark')
        # Click recaptcha button
        check_box.click()
        self.web_driver.switch_to.default_content()

    def start(self):
        # Ask for website through console
        # self.url = input('Enter website url:\n')
        # Check if website has supported recaptcha
        if not self.check_website():
            print("reCAPTCHA not present or not supported on '%s'" % self.url)
            return
        self.open_recaptcha_iframe()
        self.control_recaptcha.start()

        self.web_driver.close()



main = NewMain()
main.start()