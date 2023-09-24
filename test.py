import cv2
import numpy as np

# Load an image
img = cv2.imread('results/denoised_image_230501162904_.png')

# Define a sharpening kernel
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

# Apply the kernel to the image
sharp_img = cv2.filter2D(img, -1, kernel)

# Display the original and sharpened images side by side
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
