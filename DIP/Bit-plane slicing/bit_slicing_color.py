import cv2
import numpy as np

#--- Bit plane slicing for 3-channel images ------
src = 'C:/Users/Desktop/Plant/'

img = cv2.imread(src + 'Charlock/0a7e1ca41.png')
img_resized = cv2.resize(img, (300, 300))
cv2.imshow("Image", img)
cv2.imshow("Image resized", img_resized)

image = np.zeros((img_resized.shape[0], img_resized.shape[1], 3), np.uint8)
#image[:] = (0, 0, 0)
#image = 0

#def bit_slice(img):
#    for i in range(0, img.shape[2] + 1):
#        im = img[:,:,i]

def bit_wise_slicing(image):
   img1 = image[:,:,0] 
   img2 = image[:,:,1] 
   img3 = image[:,:,2] 
   
   channel_list = [img1, img2, img3]
   new_channel_list = []
   
   
   
   for channel in channel_list:
       image = np.zeros((img_resized.shape[0], img_resized.shape[1]), np.uint8)
       for i in range(0, channel.shape[1]):
           for j in range(0, channel.shape[0]):
                pixel = channel[i][j]
                pixel_binary = '{0:08b}'.format(pixel)
                pixel_binary = pixel_binary[:4] + '0000'
                new_pixel = int(pixel_binary, 2)
                image[i][j] = new_pixel
       new_channel_list.append(image)
   return new_channel_list    

l_list = bit_wise_slicing(img_resized)

final_image = cv2.merge((l_list[0], l_list[1], l_list[2]))
cv2.imshow("Final_image", final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
