import cv2
import numpy as np

#--- Bit plane slicing for gray images ---------
src = 'C:/Users/Desktop/Plant/'

img = cv2.imread(src + 'Charlock/0a7e1ca41.png', 0)
img_resized = cv2.resize(img, (300, 300))
cv2.imshow("Image", img)
cv2.imshow("Image resized", img_resized)

image = np.zeros((img_resized.shape[0], img_resized.shape[1]), np.uint8)

for i in range(0, img_resized.shape[0]):
    for j in range(0, img_resized.shape[1]):
        pixel = img_resized[i][j]
        pixel_binary = '{0:08b}'.format(pixel)
        pixel_binary = pixel_binary[:4] + '0000'
        new_pixel = int(pixel_binary, 2)
        image[i][j] = new_pixel

cv2.imshow ('sliced image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()










