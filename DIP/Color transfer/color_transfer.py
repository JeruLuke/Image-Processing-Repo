import numpy as np
import cv2

def image_stats(image):
	# compute the mean and standard deviation of each channel
	(l, a, b) = cv2.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())
 
	# return the color statistics
	return (lMean, lStd, aMean, aStd, bMean, bStd)



def color_transfer(source, target):
	
	source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
	target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")
 
	# compute color statistics for the source and target images
	(lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
	(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)
 
	# subtract the means from the target image
	(l, a, b) = cv2.split(target)
	l -= lMeanTar
	a -= aMeanTar
	b -= bMeanTar
 
	# scale by the standard deviations
	l = (lStdTar / lStdSrc) * l
	a = (aStdTar / aStdSrc) * a
	b = (bStdTar / bStdSrc) * b
 
	# add in the source mean
	l += lMeanSrc
	a += aMeanSrc
	b += bMeanSrc
 
	# clip the pixel intensities to [0, 255] if they fall outside
	# this range
	l = np.clip(l, 0, 255)
	a = np.clip(a, 0, 255)
	b = np.clip(b, 0, 255)
 
	# merge the channels together and convert back to the RGB color
	# space, being sure to utilize the 8-bit unsigned integer data
	# type
	transfer = cv2.merge([l, a, b])
	transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
	#cv2.imshow('Transfer', transfer)

	# return the color transferred image
	return transfer

target = 'C:/Users/selwyn77/Desktop/plant/charlock/0a7e1ca41.png'
source = 'C:/Users/selwyn77/Desktop/rough_dog_512/bulldog/american_bulldog_5.jpg' 


source = cv2.imread(source, 1)
target = cv2.imread(target, 1)

cv2.imshow('Source', source)
cv2.imshow('Target', target)

cv2.imshow('After source transfer', color_transfer(source, target))
#t = color_transfer(source, target)

cv2.waitKey()
cv2.destroyAllWindows()


