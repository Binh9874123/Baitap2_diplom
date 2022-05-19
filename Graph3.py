import os 
import cv2
from matplotlib import image

def Process(image1):
    img1 = cv2.imread(image1)
    cv2.imshow("cHH_Input" , img1)

    os.system('prostak.exe -o turn3d '+image1+',rotate.txt turn3d1.tif')
    img2= cv2.imread("turn3d1.tif")
    cv2.imshow("turn3d1",img2)

    os.system('prostak.exe -o apee3d turn3d1.tif,rotate.txt apee3d1.tif')
    img3= cv2.imread("apee3d1.tif")
    cv2.imshow("apee3d1",img3)

    os.system('prostak.exe -o apee3d apee3d1.tif,rotate.txt geometry3d1.tif')
    img4= cv2.imread("geometry3d1.tif")
    cv2.imshow("geometry3d1",img4)

    os.system('prostak.exe -o strel -s 23,23,square strel1.txt')























    cv2.waitKey()


Process("cHH.tif")