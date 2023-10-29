from PIL import Image, ImageDraw
from opensimplex import OpenSimplex
from math import cos,sin,pi

width = 300
height = 300 
img  = Image.new( mode = "RGB", size = (width, height) )
draw = ImageDraw.Draw(img)

radius = 140 
center_x = int(width/2)
center_y = int(height/2)
prev_x = int(center_x + radius * cos(0))
prev_y = int(center_y + radius * sin(0))

samples = 4*radius 
for sample in range(1, samples):
    angle = (2* sample * pi) / (samples - 1)  

    x = int(center_x + radius * cos(angle))
    y = int(center_y + radius * sin(angle))
    draw.line((prev_x, prev_y, x, y), fill=(200, 100, 50))

    prev_x = x
    prev_y = y
img.show()