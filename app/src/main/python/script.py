from skimage.color import rgb2lab, rgb2gray, lab2rgb
from skimage.io import imread, imshow
import cv2

def calculate_mean_values(image):
    return cv2.mean(image)

def calculate_LAB(image_uri):
    image_rgb = cv2.imread(image_uri)
    image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)
    image_lab = rgb2lab(image_rgb / 255)
    lab = calculate_mean_values(image_lab)
    return f'L: {lab[0]} \nA: {lab[1]} \nB: {lab[2]}'
