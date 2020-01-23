import cv2
import numpy as np
import sys

DIM=(2784, 1848)
K=np.array([[1246.6820425247993, 0.0, 1400.1685302458284], [0.0, 1252.0473487934153, 917.5894992461792], [0.0, 0.0, 1.0]])
D=np.array([[-0.01854245519936255], [-0.07220977744019902], [0.12903582735344143], [-0.0934927236525165]])


def undistort(img_path):    

     img = cv2.imread('/home/shivani/Documents/checkeerboardimg/old/2new.JPG')
     print("124",img_path)
     h,w = img.shape[:2]   
    
     map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
     undistorted_img = cv2.remap(img, map1, map2, 
 interpolation=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)   
     
     cv2.imshow("undistorted", undistorted_img)
     cv2.imwrite('2new_output.jpg',undistorted_img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

if __name__ == '__main__':
     for p in sys.argv[1:]:
        undistort(p)
