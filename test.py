import cv2
import numpy as np

# Load the images
img1 = cv2.imread('E:/laq/openCV/sample.jpg')
img2 = cv2.imread('E:/laq/openCV/dif.jpg')

# Check if the images are loaded correctly
if img1 is None:
    print("Error: Could not load 'sample.jpg'. Check the file path.")
    exit()
if img2 is None:
    print("Error: Could not load 'dif.jpg'. Check the file path.")
    exit()

# Resize images to the same dimensions (optional)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Check if the images are identical
if np.array_equal(img1, img2):
    print("The images are exactly the same.")
else:
    print("The images are different.")

