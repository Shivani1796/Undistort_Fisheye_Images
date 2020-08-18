
This is to undistort fisheye images to a normal image (pin hole model)

*Prepare By: Shivani Baldwa & Raghav Jethliya*

In this go to directory undistort_fisheye_images ----->Intel T265.

## Step 1:
**Calibrate your camera**

Run calibrate.py :
```
python calibrate.py
```

## Step 2:
**Undistort your images**

Undistort all images together
compile : python undistort.py

Run undistort.py
```
python undistort.py input_img_foldername output_img_foldername (python undistort.py input output)
```

