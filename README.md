# Object_Height_Detection


📏 Object Height Detection – Prototype Version

Overview

This project is a prototype computer vision system designed to simulate object height measurement using a fixed camera and predefined object sizes. The system detects when an object enters a specific detection zone and displays its estimated height with a visual scanning and loading effect.

⚠️ Important Note:
This implementation is an initial proof-of-concept version. For higher accuracy, scalability, and real-world deployment, this project can be extended using advanced deep learning models such as:
	•	YOLO (e.g., YOLOv8 / YOLO-Light)
	•	EfficientDet
	•	Detectron2
	•	MediaPipe Vision models

These models can improve object detection reliability, classification accuracy, and robustness under different lighting, angles, and background conditions.



Project Goal

The main goal of this project is to demonstrate a simplified approach to height estimation by:
	•	Detecting when an object enters a predefined zone
	•	Simulating an object scanning process
	•	Displaying the object’s predefined height after analysis
	•	Creating a visually interactive and user-friendly detection interface



How It Works

1. Fixed Detection Zone

The system defines a rectangular Zone on the right side of the camera frame.
Object analysis only starts when an object enters this zone.

2. Edge-Based Object Detection

Instead of using machine learning models, this prototype uses:
	•	Grayscale conversion
	•	Gaussian blur
	•	Canny edge detection
	•	Contour detection

This approach allows simple and fast object presence detection.


3. Scanning Simulation

When an object enters the detection zone:
	•	A scanning bar moves vertically through the zone
	•	A Loading animation is displayed
	•	After scanning completes, the object’s height appears



4. Height Display Logic

Each supported object has a predefined height value.
When detected, the system displays:
	•	Object height in centimeters
	•	Display duration timer
	•	Automatic clearing after a few seconds



Supported Objects

The prototype currently supports the following objects:

Object	Approximate Height
Water Bottle (1.5L)	30 – 33 cm
Mobile Phone	14.67 cm
Tissue Box	19 – 21 cm
Book	17 cm

The system selects the most representative height value for display.



Visual Output Features

The system provides an interactive user interface including:
	•	Semi-transparent detection zone
	•	Animated scanning bar
	•	Loading animation
	•	Timed height display
	•	Real-time camera feed processing



Limitations of Current Prototype

Since this version does not use trained AI models, it has some limitations:
	•	Cannot distinguish object categories automatically
	•	Sensitive to lighting changes
	•	Depends on object placement inside the detection zone
	•	Uses approximate predefined object sizes
	•	Accuracy depends on contour detection quality



Future Improvements

This project can be significantly improved by integrating:

🔹 Deep Learning Detection

Using models like YOLO or Detectron2 to:
	•	Detect objects automatically
	•	Recognize object categories
	•	Improve detection reliability

🔹 Real Measurement Scaling

Using reference calibration objects or depth estimation to:
	•	Measure objects dynamically
	•	Remove dependency on predefined heights

🔹 Multi-Object Tracking

Allow simultaneous detection and measurement of multiple objects.

🔹 Performance Optimization

Improve processing speed for real-time applications.



Technologies Used
	•	Python
	•	OpenCV
	•	NumPy
	•	Real-time video processing



Use Cases

This prototype demonstrates concepts that can be expanded into:
	•	Smart retail measurement systems
	•	Industrial object inspection
	•	Educational computer vision demonstrations
	•	Automated packaging size estimation



Conclusion

This project provides a visual and functional introduction to object height detection using classical computer vision techniques. While it is not intended to replace professional measurement systems, it serves as a strong foundation for future AI-based object measurement solutions.



Author Note

This project is designed as an experimental and educational prototype. Contributions, improvements, and model integrations are highly encouraged.
