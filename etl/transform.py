import numpy as np
import cv2

def convert_to_grayscale(images):
    def to_grayscale(image):
        if image.ndim == 3:
            return np.mean(image, axis=0)
        return image

    return [to_grayscale(img) for img in images]

def resize_images(images, target_shape=(512, 512)):
    resized_images = []
    for img in images:
        if img.ndim == 3:
            img = np.mean(img, axis=0)  # Convert to grayscale if necessary
        resized_img = cv2.resize(img, target_shape)
        resized_images.append(resized_img)
    return np.array(resized_images)

def calculate_statistics(images):
    mean = np.mean(images)
    median = np.median(images)
    std = np.std(images)
    return mean, median, std
