import os
import numpy as np
import shutil
import random
 

src = 'C:/Users/524316/Desktop/Caltech_101/'
dest = 'C:/Users/524316/Desktop/Caltech_101_validation/'

val_perc = 0.25 

for folder in os.listdir(src): 
    print (folder)
    
    if os.path.isdir(src + folder):
#        print ('True')
        num_of_files = os.listdir(src + folder)
#        print(len(num_of_files))
        num_of_val_imgs = int(0.25 * len(num_of_files)) + 1
#        print(num_of_val_imgs)
        
        files = os.listdir(src + folder)
        nfiles = []
        for j in files:
            if j.endswith('.jpg'):
                nfiles.append(j)
        choices = random.sample(nfiles, num_of_val_imgs) 
        for f in choices:
            shutil.move(os.path.join(src + folder + '/' + f), os.path.join(dest + folder))