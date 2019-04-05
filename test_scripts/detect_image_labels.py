from ImageLabeling import *

labeling = ImageLabeling()

print('bus')
labels = [label.lower() for label in labeling.detect_labels("./test_label_images/bus.jpg")]
print(labels)
print('bus' in labels)
