# -*- coding: utf-8 -*-
"""Session_3_1_Object_Detection_YOLO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12YWKYVz-Q93WSaCsOTGyEhNqJGCeMrfj
"""

!pip install ultralytics

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

"""## Load the YOLOv8 model"""

model = YOLO("yolov8n.pt")

"""## Read and display the input image"""

image = cv2.imread('/car_person.jpg')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)

"""# Apply YOLO model and print the results"""

results = model(image)
results[0].boxes

"""## Draw bounding box around objects and display class label over them"""

rgb_copy = rgb_image.copy()
for i, box in enumerate(results[0].boxes.xyxy): # Get bounding boxes
        x1, y1, x2, y2 = map(int, box)  # Convert to integer coordinates
        confidence = results[0].boxes.conf[i].item()  # Confidence score
        class_id = int(results[0].boxes.cls[i].item())  # Class index
        label = f"{results[0].names[class_id]}: {confidence:.2f}"  # Label text
        # Draw bounding box
        cv2.rectangle(rgb_copy, (x1, y1), (x2, y2), (255,0,0), 2)

        # Put label text
        cv2.putText(rgb_copy, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
plt.imshow(rgb_copy)