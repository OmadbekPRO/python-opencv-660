# -*- coding: utf-8 -*-
"""cars.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QlvCICMRR2n4Llz-i3aCYI12U1w4kCZ-
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread('joker.jpg')
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

rasm1=cv2.imread('pexels-alexgtacar-745150-1592384.jpg')
cv2_imshow(rasm1)

oqqora=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

rasm2=cv2.imread('pexels-mikebirdy-112460.jpg')
cv2_imshow(rasm2)

oqqora=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

rasm3=cv2.imread('pexels-mikebirdy-170811.jpg')
cv2_imshow(rasm3)

oqqora=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

rasm4=cv2.imread('pexels-pixabay-210019.jpg')
cv2_imshow(rasm4)

oqqora=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)