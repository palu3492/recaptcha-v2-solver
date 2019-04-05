from selenium import webdriver
import urllib.request
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/recaptcha/api2/demo')

captcha_iframe = driver.find_element_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/']")

#swtich to captcha iframe
driver.switch_to.frame(captcha_iframe)

#this is specific to a recaptcha iframe
check_box = driver.find_element_by_class_name('recaptcha-checkbox-checkmark')

#opens image selection menu
check_box.click()

#switch to parent frame so that the image selction frame can be located
driver.switch_to.default_content()

image_selection_iframe = driver.find_element_by_css_selector("iframe[title='recaptcha challenge']")

driver.switch_to.frame(image_selection_iframe)

time.sleep(2)

image_squares = driver.find_elements_by_css_selector("td[class='rc-imageselect-tile']")

img_elements = driver.find_elements_by_css_selector("img[class^='rc-image-tile-']")

images=[]

i=0
for img in img_elements:
    i+=1
    images.append(urllib.request.urlretrieve(img.get_attribute('src'), "test1/test"+str(i)+".jpg"))

print (images[0][0])

# urllib.request.urlretrieve(image_url, "test23.jpg")