#Q-1 : Obtain two blank images. First draw a circle and then draw a rectangle. Fill these shapes with white colour.

# circle
import cv2
import numpy as np
import matplotlib.pyplot as plt
whiteblankimage = 0 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
cv2.circle(whiteblankimage, center=(250,250), radius=100,
color=(255,255,255), thickness= -1)
plt.imshow(whiteblankimage)
plt.show()

# rectangle
import cv2
import numpy as np
import matplotlib.pyplot as plt
whiteblankimage = 0 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
cv2.rectangle(whiteblankimage, pt1=(100,200), pt2=(400,300),
color=(255,255,255), thickness=-1)
plt.imshow(whiteblankimage)
plt.show()