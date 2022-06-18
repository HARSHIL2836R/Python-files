from PIL import Image
import pytesseract
import argparse
import cv2
import os
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="C:\Users\91878\Pictures\KV_2020\Sarthak.png" )
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="blur")
args = vars(ap.parse_args())
