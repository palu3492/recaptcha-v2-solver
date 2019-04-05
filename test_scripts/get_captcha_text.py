from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com/recaptcha/api2/demo')

captcha_iframe = driver.find_element_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/']")
print(captcha_iframe)
# switch to captcha iframe
driver.switch_to.frame(captcha_iframe)

# this is specific to a recaptcha iframe
check_box = driver.find_element_by_class_name('recaptcha-checkbox-checkmark')

#opens image selection menu
check_box.click()

driver.switch_to.default_content()

# wait until image selection menu is open
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))

# switch to image selection menu
captcha_images_frame = driver.find_element_by_css_selector("iframe[title='recaptcha challenge']")
driver.switch_to.frame(captcha_images_frame)

# get image label
text = driver.find_element_by_css_selector("div[class^='rc-imageselect-desc'] strong")
print(text)
# <div class="rc-imageselect-desc-no-canonical" style="width: 352px; font-size: 12px;">
#   Select all squares with <strong style="font-size: 28px;">traffic lights</strong>
#   <span class="rc-imageselect-carousel-instructions" style="font-size: 14px;">
#     If there are none, click skip
#   </span>
# </div>