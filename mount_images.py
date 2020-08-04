import os, numpy, PIL
import math

from PIL import Image

allfiles = os.listdir("images_resized/")


print(allfiles)
imlist=[filename for filename in allfiles if  filename[-4:] in [".jpg",".JPG"]]

w, h = Image.open("images_resized/" + imlist[0]).size

skaits = len(imlist)
N = math.sqrt(skaits)
pirms, pecr = math.modf(N)
pec = int(pecr)

total_width = w * pec
total_height = h * pec

arr = numpy.zeros((h,w,3),numpy.float)
tot = 0
img_ind =[] 
for im in imlist:
    imarr=numpy.array(Image.open("images_resized/" + im))
    li = {'file':im, 'rgb': int(numpy.average(imarr))}
    #print(li)
    img_ind.append(li) 

for elem in img_ind:
    print(elem)

def takeSecond(e):
    return e['rgb']

img_ind.sort(reverse=True, key=takeSecond)
new_im = Image.new('RGB', (total_width, total_height))

z = 0 
g = 0
total = 0
while z < pec:
    while g < pec:
        open = "images_resized/" + img_ind[total].get('file')
        print(open)
        img = Image.open(open)
        #img = Image.open(imlist[total])
        new_im.paste(img, (w*g, h*z))
        g += 1
        total += 1
    z += 1
    g = 0

new_im.save('mount.jpg')
