#Undistort all images together
#compile : python undistort.py
#run :python undistort.py input_img_foldername output_img_foldername (python undistort.py input output)

import cv2
import numpy as np
import sys
import uuid
import glob

DIM=(848, 800)

K=np.array([[286.221588134766, 0.0,  419.467010498047], [0.0, 287.480102539062, 386.97509765625], [0.0, 0.0, 1.0]])

D=np.array([[-0.0043481751345098], [0.037125650793314], [-0.0355393998324871], [0.00577297387644649 ]])

def undistort(img_path, output_path):  
 

    images = glob.glob(img_path+'/*.png') 
    print("images : ",images)
    for img_path in images:
	    print("img_path: ", img_path)
            img_path_array=img_path.split('/')
	    img_output_path=img_path_array[1]
	    
	    img = cv2.imread(img_path)
            print("print images",img)
    	    h,w = img.shape[:2]  
            map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
            undistorted_img = cv2.remap(img, map1, map2,interpolation=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)   
 	    cv2.imshow("undistorted", undistorted_img)
    	    cv2.imwrite(output_path+"/result_img"+img_output_path,undistorted_img)
    	    #cv2.waitKey(0)
    	    #cv2.destroyAllWindows()

if __name__ == '__main__':
     #for p in sys.argv[1:]:
	input_image_folder_name = sys.argv[1]
	output_image_folder_name = sys.argv[2]
	undistort(input_image_folder_name , output_image_folder_name)    
   #print(p)
    #     undistort(p)
