
This is to undistort fisheye images to a normal image (pin hole model)

*Prepare By: Shivani Baldwa & Raghav Jethliya*

In this go to directory undistort_fisheye_images ----->Intel T265.

## Step 1:
**Calibrate your camera**

Run calibrate.py :
```
python calibrate.py
```
RESULT:
<p align="center">
  <img src="https://github.com/Shivani1796/Undistort_Fisheye_Images/blob/master/undistort_fisheye_images/intel%20t265/calibratefile.png">
</p>

NOTE:
Here you need to correct you image folder path.In this program we have kept image folder, calibrate.py and undistort.py files at the same place.

## Step 2:
**Undistort your images**

Undistort all images together
compile : python undistort.py

Run undistort.py
```
python undistort.py input_img_foldername output_img_foldername (Fpor Example: python undistort.py input output)
```
RESULT:
<p align="center">
  <img src="https://github.com/Shivani1796/Undistort_Fisheye_Images/blob/master/undistort_fisheye_images/intel%20t265/undistortfile.png">
</p>

NOTE:
1) Here you need to check the calibration parameter must be same as result obtained from calibrate.py.

2) Make sure that all parameters are correct.

3) Check the input and output foldername while you compile and run program.
