# This file currently DOES NOT run correctly. You WILL get an error somewhere


# Using pyautogui to take the screenshot, ImageGrab to check the for the special things (yellow for explode, red for healthy, and  for rampage), pytesseract to find out what the word is and type it at blistering speed
from pyautogui import screenshot
import ImageGrab
import pytesseract
import numpy as np

# Funcs
def scrnshot(top=0, left=0, width=0, height=0):
	if top == 0 and left == 0 and width == 0 and height == 0:
		screenshot()
	else:
		screenshot(region = (top, left, width, height))

# Testing
def test():
	screenshot(region = ())
	
# dw about this, this is something else.
red_image = PIL.Image.open("red_image.png")
Create a PIL.Image object


red_image_rgb = red_image.convert("RGB")
Convert to RGB colorspace


rgb_pixel_value = red_image_rgb.getpixel((10,15))

# or this
pim = Image.open('image.png').convert('RGB')
im  = np.array(pim)

blue = [0,0,255]

Y, X = np.where(np.all(im==blue,axis=2))

print(X,Y)

# or this
https://www.codegrepper.com/code-examples/python/get+color+of+pixel+on+screen+python
