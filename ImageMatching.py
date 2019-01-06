from PIL import Image
import io
import os
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Test-0442790e64ab.json"

def detect_labels(path, num):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    #all = ""
    for label in labels:
        print (label.description)


def break_up_image(path):
    img = Image.open(path)

    width = img.size[0]
    height = img.size[1]

    widthOfBox = int(width / 3)
    heightOfBox = int(height / 3)

    numberOfRows = 3
    numberOfColumns = 3

    imageParts = []

    boxNum = 0

    for row in range(numberOfRows):
        for col in range(numberOfColumns):
            tempImg = img.crop(
                (
                    (col) * widthOfBox,
                    (row) * heightOfBox,
                    (col + 1) * widthOfBox,
                    (row + 1) * heightOfBox
                )
            )
            imageParts.append(tempImg)
            boxNum += 1

    i = 0
    for image in imageParts:
        image.save("new/img" + str(i) + ".jpg")
        i += 1


break_up_image("break.jpg")
i=0
for i in range(9):
    print("\nPart "+str(i+1)+":")
    detect_labels("new/img" + str(i) + ".jpg", i)
    i+=1