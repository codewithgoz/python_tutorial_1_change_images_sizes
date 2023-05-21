##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.1 - Script 2
##############################################################
# Description: Simple script for image's height resizing
# Dependencies:
# ----------------------------------------
# pip install Pillow
# pip install python-resize-image
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import os
from PIL import Image
from resizeimage import resizeimage

path = "/home/goz/youtube/python/video_1/images"
os.chdir(path)
images = os.listdir()

for image in images:
    try:
        image1 = Image.open(image)
        image1 = resizeimage.resize_height(image1, 200)
        image1.save('new_' + image)
        image1.close()
        print(f"Se cambió el tamaño de {image}")
    except:
        print(f"{image} no se puede modificar")