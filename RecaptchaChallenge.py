import urllib.request

class RecaptchaChallenge():

    def __init__(self, web_driver, tiles, rows, cols, separate_image, image_labeling):
        self.web_driver = web_driver
        self.tiles = []
        self.label_parts = []
        self.number_of_tiles = tiles
        self.number_of_rows = rows
        self.number_of_columns = cols
        self.separate_image = separate_image
        self.image_labeling = image_labeling

    def find_image_selection_tiles(self):
        # self.tiles = self.web_driver.find_elements_by_css_selector("td[class='rc-imageselect-tile']")
        tiles = self.web_driver.find_element_by_id("rc-imageselect-target")
        self.tiles = tiles.find_elements_by_tag_name("td")

    def find_label(self):
        label = self.web_driver.find_element_by_css_selector("div[class^='rc-imageselect-desc'] strong").text
        self.label_parts = label.split(' ') + [label]

    def download_captcha_image(self, tile_index):
        img_element = self.web_driver.find_elements_by_css_selector("img[class^='rc-image-tile-']")[tile_index-1]
        urllib.request.urlretrieve(img_element.get_attribute('src'), "downloaded_recaptcha_images/captcha_image" + str(tile_index) + ".jpg")

    def separate_image_function(self, save_all, download_number):
        self.separate_image.set_image_data(download_number)
        self.separate_image.separate(save_all, download_number)

    def does_label_match_image(self, tile_index):
        labels = self.image_labeling.detect_labels("recaptcha_image_parts/part" + str(tile_index) + ".jpg")
        for label in self.label_parts:
            if label in labels:
                return True
        return False

    def click_tiles_that_match_label(self):
        for i in range(self.number_of_tiles):
            if self.does_label_match_image(i+1):
                self.tiles[i].click()

    def complete_challenge(self):
        self.find_image_selection_tiles()
        self.find_label()
        self.download_captcha_image(1)
        self.separate_image_function(True, 1)
        for i in range(1, self.number_of_tiles+1):
            self.does_label_match_image(i)







