##############################################################
# GozDeveloper Youtube Channel - Python Video No.1 - Script 1
##############################################################
# Description: Simple script for image's width resizing
# Dependencies:
# ----------------------------------------
# pip install Pillow
# pip install python-resize-image
# ----------------------------------------
# Author: Goz
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
        image1 = resizeimage.resize_width(image1, 150)
        image1.save('new_' + image)
        image1.close()
        print(f"Se cambió el tamaño de {image}")
    except:
        print(f"{image} no se puede modificar")






