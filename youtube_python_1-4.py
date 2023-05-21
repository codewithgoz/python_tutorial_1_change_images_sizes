##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.1 - Script 4
##############################################################
# Description: Simple script for image's custom resizing
# Dependencies:
# ----------------------------------------
# pip install Pillow
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import os
from PIL import Image

path = "/home/goz/youtube/python/video_1/images"
os.chdir(path)
images = os.listdir()

for image in images:
    try:
        image1 = Image.open(image)
        image1 = image1.resize((1900, 300))
        image1.save('new_' + image)
        image1.close()
        print(f"Se cambió el tamaño de {image}")
    except:
        print(f"{image} no se puede modificar")