import cv2
import sys
import numpy as np

def Add_salt_pepper_Noise(srcArr,pa,pb):
	amount1 = srcArr.shape[0] * srcArr.shape[1] * pa
	amount2 = srcArr.shape[0] * srcArr.shape[1] * pb
	for i in range(int(amount1)):
		srcArr[np.random.randint(0, srcArr.shape[0]), np.random.randint(0, srcArr.shape[1])] = 0
	for i in range(int(amount2)):
		srcArr[np.random.randint(0, srcArr.shape[0]), np.random.randint(0, srcArr.shape[1])] = 255
		
def Add_gaussian_Noise(srcArr, mean, sigma):
	Noiseimg = srcArr.copy()
	cv2.randn(Noiseimg,mean,sigma)
	cv2.add(srcArr, Noiseimg, srcArr)
	
image = cv2.imread(sys.argv[1])
meanValue = [0, 5, 10, 20]	
sigmaValue = [0, 20, 50, 100]
kernelValue = [3, 5, 7]
paValue = [0.01, 0.03, 0.05, 0.4]
pbValue = [0.01, 0.03, 0.05, 0.4]
dir = "NoiseOutputImage/"
for kernel in kernelValue:
	for mean in meanValue:
		for sigma in sigmaValue:
			gnoise = image.copy()
			Add_gaussian_Noise(gnoise, mean, sigma)
			cv2.imwrite(dir+"GaussNoise"+"_Mean="+str(mean)+"_Sigma="+str(sigma)+".png",gnoise)
			
			noisebf = gnoise.copy()
			cv2.blur(noisebf, (kernel,kernel))
			cv2.imwrite(dir+"BoxFilter"+"_Mean="+str(mean)+"_Sigma="+str(sigma)+"_Kernel="+str(kernel)+".png",noisebf)
			
			noisegf = gnoise.copy()
			cv2.GaussianBlur(noisegf, (kernel,kernel), 1.5)
			cv2.imwrite(dir+"GaussianFilter"+"_Mean="+str(mean)+"_Sigma="+str(sigma)+"_Kernel="+str(kernel)+".png",noisegf)
			
			noisemf = gnoise.copy()
			cv2.medianBlur(noisemf, kernel)
			cv2.imwrite(dir+"MedianFilter"+"_Mean="+str(mean)+"_Sigma="+str(sigma)+"_Kernel="+str(kernel)+".png",noisemf)
	
	for pa in paValue:
		for pb in pbValue:
			spnoise = image.copy()
			Add_salt_pepper_Noise(spnoise, pa, pb)
			cv2.imwrite(dir+"SPNoise"+"_pa="+str(pa)+"_pb="+str(pb)+".png",spnoise)
			
			noisebff = spnoise.copy()
			cv2.blur(spnoise, (kernel,kernel))
			cv2.imwrite(dir+"BoxFilter_SP"+"_pa="+str(pa)+"_pb="+str(pb)+"_Kernel="+str(kernel)+".png",noisebff)
			
			noisegff = spnoise.copy()
			cv2.GaussianBlur(noisegff, (kernel,kernel), 1.5)
			cv2.imwrite(dir+"GaussianFilter_SP"+"_pa="+str(pa)+"_pb="+str(pb)+"_Kernel="+str(kernel)+".png",noisegff)
			
			noisemff = spnoise.copy()
			cv2.medianBlur(noisemff, kernel)
			cv2.imwrite(dir+"MedianFilter_SP"+"_pa="+str(pa)+"_pb="+str(pb)+"_Kernel="+str(kernel)+".png",noisemff)
			
cv2.waitKey(0)