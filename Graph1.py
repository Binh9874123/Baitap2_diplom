import os 
import cv2
from matplotlib import image

def Process_Image(image1):
    img1 = cv2.imread("C1.tif")
    cv2.imshow("DI_Input" , img1)

    os.system('prostak.exe -o getp C1.tif getp1.tif')
    img2= cv2.imread("getp1.tif")
    cv2.imshow("getp1" , img2)
    
    '''os.system('prostak.exe -o getp -r 4 C1.tif getp2.tif')
    img3= cv2.imread("getp2.tif")
    cv2.imshow("getp1" , img3)

    os.system('prostak.exe -o getp -r 4 C1.tif getp2.tif')
    img4= cv2.imread("getp3.tif")
    cv2.imshow("getp1" , img4)


    os.system('prostak.exe -o getp -r 4 C1.tif getp2.tif')
    img5= cv2.imread("getp4.tif")
    cv2.imshow("getp1" , img5)'''
    cv2.waitKey()




Process_Image("C1.tif")





















