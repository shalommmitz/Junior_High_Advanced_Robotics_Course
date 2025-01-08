import cv2
import numpy as np

#Read image
img = cv2.imread("image.png")
#See shape
print(img.shape)    # Y then x
# New image, same size as img
new = np.zeros(img.shape, np.uint8)
#print all values of img
h = img.shape[0]
w = img.shape[1]
for y in range(h):
    for x in range(w):
        print(img[y][x])
#Replace all white pixels with red (pixels values are BGR)
for y in range(h):
    for x in range(w):
       if list(img[y][x])==[255,255,255]:
           new[y][x] = [0,0,255]
       else:
           new[y][x] = img[y][x]
# Write image
cv2.imwrite("new.png", new)
           
