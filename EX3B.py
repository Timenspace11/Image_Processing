#Q2. On these above images, perform following bitwise operation.
#i. OR
#ii. AND
#iii. NOT
#iv. EXOR
#

import cv2
import numpy as np
img1 = cv2.imread(r"E:\images\download.png")
img2 = cv2.imread(r"E:\images\download (1).png")
dest_and = cv2.bitwise_and(img2, img1, mask = None)
dest_or = cv2.bitwise_or(img2, img1, mask = None)
dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
dest_not1 = cv2.bitwise_not(img1, mask = None)
dest_not2 = cv2.bitwise_not(img2, mask = None)
cv2.imshow('Bitwise And', dest_and)
cv2.imshow('Bitwise OR', dest_or)
cv2.imshow('Bitwise XOR', dest_xor)
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)
if cv2.waitKey(0) & 0xff == 27:
cv2.destroyAllWindows()