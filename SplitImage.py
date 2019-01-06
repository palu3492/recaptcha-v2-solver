from PIL import Image
import os

# class used to split images into parts based on a column and row grid
class SplitImage():
    def __init__(self):
        self.i = 0
        #self.image_parts = []

    def set_image_data(self, img, cols, rows):
        if cols<1 or rows<1:
            raise Exception('column and row need to be above 0')
        self.image = Image.open(img)
        image_width = self.image.size[0]
        image_height = self.image.size[1]
        self.cols=cols
        self.rows=rows
        self.square_width = image_width/cols
        self.square_height = image_height/rows

    def split_image(self, path):
        self.image_parts = []
        for row in range(self.rows):
            for col in range(self.cols):
                temp_img = self.image.crop(
                    (
                        (col) * self.square_width,
                        (row) * self.square_height,
                        (col+1)* self.square_width,
                        (row+1) * self.square_height
                    )
                )
                self.image_parts.append(temp_img)
        #self.clear_directory()
        for i in range(len(self.image_parts)):
            self.image_parts[i].save(path+str(i)+".jpg")

    def clear_directory(self):
        folder = 'image parts'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)