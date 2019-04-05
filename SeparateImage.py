from PIL import Image

# Class used to separate images into parts based on a column and row grid
class SeparateImage():
    def __init__(self, rows, columns):
        self.image = None
        self.number_of_rows = rows
        self.number_of_columns = columns
        self.square_width = 0
        self.square_height = 0

    def set_image_data(self, download_number):
        self.image = Image.open("downloaded_recaptcha_images/captcha_image" + str(download_number) + ".jpg")
        image_width, image_height = self.image.size
        self.square_width = image_width/self.number_of_columns
        self.square_height = image_height/self.number_of_rows

    def split_image(self, save_all, tile_index):
        index = 0
        for row in range(self.number_of_rows):
            for col in range(self.number_of_columns):
                temp_img = self.image.crop(
                    (
                        (col) * self.square_width,
                        (row) * self.square_height,
                        (col+1)* self.square_width,
                        (row+1) * self.square_height
                    )
                )
                index += 1
                if save_all or index == tile_index:
                    temp_img.save("recaptcha_image_parts/part" + str(index) + ".jpg")