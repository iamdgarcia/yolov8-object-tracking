# yolov8-object-tracking 


### Features
- Object Tracks
- Different Color for every class
- Video/Image Supported


### Steps to run Code

- Clone the repository
```
https://github.com/danigarci1/yolov8-object-tracking.git
```

- Goto cloned folder
```
cd yolov8-object-tracking
```

- Install requirements
```
pip install -r requirements.txt
```

- Run tracking script
```
#video file
python python run.py model=yolov8x.pt source="test.mp4" show=True

#External Camera
python python run.py model=yolov8x.pt source=1 show=True

#imagefile
python python run.py model=yolov8x.pt source="image.png" show=True
```

- Output file will be created in the working-dir/runs/detect/train with original filename


### Results
![yolov8s tracking example](assets/results/street_s.gif)

![yolov8x tracking example](assets/results/street_x.gif)

For more details, you can connect with me on [LinkedIn](https://www.linkedin.com/in/danigarciape/)
