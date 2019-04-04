from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/recaptcha/api2/demo')

captcha_iframe = driver.find_element_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/']")

# swtich to captcha iframe
driver.switch_to.frame(captcha_iframe)

# this is specific to a recaptcha iframe
check_box = driver.find_element_by_class_name('recaptcha-checkbox-checkmark')

# opens image selection menu
check_box.click()

#"Select all squares with a sidewalk, If there are none, click skip"

#"Select all images with roads, Click verify once there are none left."

#"Select all images with a store front"
