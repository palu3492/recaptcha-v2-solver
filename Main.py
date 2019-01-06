from selenium import webdriver
from SplitImage import *
from ImageLabeling import *
import urllib.request
import time

split = SplitImage()
labeling = ImageLabeling()

def press_recaptcha_button(driver):
    # find the iframe that is the recpatcha interface
    captcha_iframe = driver.find_element_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/']")
    # swtich to captcha iframe
    driver.switch_to.frame(captcha_iframe)
    # find the check box of the captcha interface
    check_box = driver.find_element_by_class_name('recaptcha-checkbox-checkmark')
    # click the check box and open image selection menu
    check_box.click()

def get_image_boxes(driver):
    return driver.find_elements_by_css_selector("td[class='rc-imageselect-tile']")

def download_captcha_image(driver, number, i):
    img_element = driver.find_elements_by_css_selector("img[class^='rc-image-tile-']")[i]
    urllib.request.urlretrieve(img_element.get_attribute('src'), "images/captcha image" + number + ".jpg")

def split_image(number, cols, rows):
    split.set_image_data("images/captcha image"+number+".jpg", cols, rows)
    split.split_image("images/captcha image part")

def check_image(captcha_text_parts, number):
    labels = labeling.detect_labels("images/captcha image part" + str(number) + ".jpg")
    print(labels)
    for text_part in captcha_text_parts:
        for label in labels:
            if text_part in label:
                return True

def is_captcha_iframe_open(driver):
    # switch back to the starting frame
    driver.switch_to.default_content()
    visibility_elem = driver.find_element_by_css_selector("div[style*='2000000000']")
    visibility=visibility_elem.is_displayed()
    if visibility:
        return True

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://www.google.com/recaptcha/api2/demo' #"https://patrickhlauke.github.io/recaptcha/"
driver.get(url)
press_recaptcha_button(driver)
# switch back to the starting frame
driver.switch_to.default_content()

time.sleep(3)

# check each new captcha challenge
while is_captcha_iframe_open(driver):
    # switch to captcha image selection iframe
    image_selection_iframe = driver.find_element_by_css_selector("iframe[title='recaptcha challenge']")
    driver.switch_to.frame(image_selection_iframe)

    if "Select all images with" in driver.find_element_by_css_selector("div[class*='rc-imageselect-desc']").get_attribute('innerHTML'):
        print("TRUE")
        # find all the image boxes to click
        captcha_image_boxes = get_image_boxes(driver)
        captcha_image_parts = []
        rows = len(driver.find_elements_by_css_selector("#rc-imageselect-target > table > tbody > tr"))
        cols = int(len(driver.find_elements_by_css_selector("td[class='rc-imageselect-tile']")) / rows)

        captcha_text = driver.find_element_by_css_selector("div[class^='rc-imageselect-desc'] strong").get_attribute('innerHTML').rstrip("s")
        captcha_text_parts = []
        for part in captcha_text.split(" "):
            captcha_text_parts.append(part)
        print (captcha_text_parts)
        download_captcha_image(driver, "1",  0)
        for i in range (len(captcha_image_boxes)):
            split_image("1", cols, rows)

        #split the image once
        #save each part as part1 - part8.. (ex)
        #when new image for type1 captcha overwrite previous image part

        for i in range(len(captcha_image_boxes)):
            if check_image(captcha_text_parts, i):
                captcha_image_boxes[i].click()
                time.sleep(.5)
                # att = captcha_image_boxes[i].get_attribute("class")
                # if not "tileselected" in att:
                go = True
                while go:
                    time.sleep(4)
                    #wait till animation class is removed
                    download_captcha_image(driver, "1", i)
                    split_image("1", 1, 1)
                    if check_image(captcha_text_parts, 0):
                        captcha_image_boxes[i].click()
                    else:
                        go = False
        driver.find_element_by_css_selector("button[class^='rc-button-default']").click()
    else:
        # Click skip if selection type is all images of bigger image
        driver.find_element_by_css_selector("button[class^='rc-button-default']").click()