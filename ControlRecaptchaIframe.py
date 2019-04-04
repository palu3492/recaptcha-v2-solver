
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ControlRecaptchaIframe:

    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.recaptcha_iframe = None

    def find_recaptcha_iframe(self):
        # Wait until recaptcha iframe opens
        wait = WebDriverWait(self.web_driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
        # Find recpatcha iframe
        try:
            self.recaptcha_iframe = self.web_driver.find_element_by_css_selector("iframe[title='recaptcha challenge']")
            self.web_driver.switch_to.frame(self.recaptcha_iframe)
            return True
        except:
            return False

    def find_skip_button(self):
        pass

    def find_next_button(self):
        pass

    def start(self):
        if not self.find_recaptcha_iframe():
            print("Could not find reCAPTCHA image selection menu after clicking 'I'm not a robot' button")
            return
        self.web_driver.switch_to.default_content()

