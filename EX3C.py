#Apply average or mean filter on an Image 

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r"E:\images\istockphoto-1364371014-1024x1024.jpg")
blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()