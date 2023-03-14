import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# read image
image_path = '/content/img_1.png'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)
print(text_[0][1])
threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (255,255,0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (0, 245, 12), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
