from PIL import Image, ImageDraw
import random

def draw_grid(draw, grid_size, width, height,radius):
    for row in range(0, height, grid_size):
        for col in range(0, width, grid_size):
            draw.ellipse([row-radius, col-radius, row+radius, col+radius], fill=(121, 103, 130))

def draw_weave(draw, grid_size, width, height):
    for row in range(0, height, grid_size):
        for col in range(0, width, grid_size):
            if random.choice([0, 1]):  
                line = [row, col, row+grid_size, col+grid_size] 
            else: 
                line = [row, col+grid_size, row+grid_size, col] 
            offset = int((row+col)/5)
            draw.line(xy=line, fill=(255-offset, 162-offset, 0-offset))

def draw_patches(draw,row,col,sizes,patch_size):
    size = int(120/(random.randrange(sizes) + 1))
    for row2 in range(row,row+patch_size,size):
        for col2 in range(col,col+patch_size,size):
            offset = int((row2+col2)/5) - int(random.random()*100)
            draw.rectangle([row2, col2, row2+size, col2+size], fill=(255-offset, 162-offset, 0-offset))

def draw_quilt(draw, width, height, sizes):
    patch_size = int(height/4)
    for row in range(0, height, patch_size):
        for col in range(0, width, patch_size):
            draw_patches(draw,row,col,sizes,patch_size)
            
            
if __name__ == "__main__":
    width = 480
    height = 480 
    #i chose 480 because its divisible by 1-6, otherwise some patches look slightly out of place 
    #also hi mr.bach

    img  = Image.new("RGB", (width, height),color=(47, 40, 44))
    draw = ImageDraw.Draw(img)

    #draw_quilt(draw,width,height,5)
    #draw_grid(draw, 20, width, height,4)
    draw_weave(draw, 20, width, height)
    img.show()