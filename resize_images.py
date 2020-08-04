from PIL import Image
import os, sys

path = "images/"
path2 = "images_resized/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im_in = Image.open(path+item)
            im = im_in.convert('RGB')
            f, e = os.path.splitext(path+item)
            imResize = im.resize((900,900), Image.ANTIALIAS)
            imResize.save(path2+ item, 'JPEG', quality=90)

resize()
