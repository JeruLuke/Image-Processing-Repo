import cv2
import os
import numpy as np
import shutil
import random

 

src = 'C:/Users/524316/Desktop/Caltech_101/'
dest = 'C:/Users/524316/Desktop/Caltech_101_padded/'

for folder in os.listdir(src): 
    print (folder)
    
    if os.path.isdir(src + folder):
##        print ('True')
#        num_of_files = os.listdir(src + folder)
##        print(len(num_of_files))
#        num_of_val_imgs = int(0.25 * len(num_of_files)) + 1
##        print(num_of_val_imgs)
#        
#        files = os.listdir(src + folder)
#        nfiles = []
#        for j in files:
#            if j.endswith('.jpg'):
#                nfiles.append(j)
#        choices = random.sample(nfiles, num_of_val_imgs) 
#        for f in choices:
#            shutil.move(os.path.join(src + folder + '/' + f), os.path.join(dest + folder))
        
        
        
        
        if not os.path.exists(dest + folder):
            os.makedirs(dest + folder)
            
            contents = os.listdir(os.path.join(src, folder)) 
            ll = os.path.join(src, folder)
#            print(contents)
            #file_count = 0
            if os.path.isdir(src + folder): 
                
                
                
                for f in contents:
#                    print(f)
                    if f.endswith ('.jpg'):
#                        print (f)
                
#                        print (f)
                
                        img = cv2.imread(os.path.join(ll, f))
#                        print(img.shape)
                        h, w, _ = img.shape
                        black_pixels = [0, 0, 0] 
                        
                        if h % 2 != 0:
                            h = h + 1
                        elif w % 2 != 0:
                            w = w + 1

#                   --- first level of padding to make the image square ---   

                        if(h > w):  #--- pad along the sides of the image---
                           a = int((h - w)/2)
#                           print(a)
                           pad_img = cv2.copyMakeBorder(img, 0, 0, a, a, cv2.BORDER_CONSTANT, value = black_pixels)
                           img = pad_img.copy()
                           cv2.imwrite(dest + folder + '/' + f, img)

                        elif (w > h):       #--- pad along the top and bottom of the image---
                           a = int((w - h)/2)
#                           print(a)
                           pad_img = cv2.copyMakeBorder(img, a, a, 0, 0, cv2.BORDER_CONSTANT, value = black_pixels)
                           img = pad_img.copy()
                           cv2.imwrite(dest + folder + '/' + f, img)