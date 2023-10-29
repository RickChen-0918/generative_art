from PIL import Image, ImageDraw

width = 300
height = 300


imgs = []
for x in range(100):
    img = Image.new(mode='RGB', size=(width, height))
    draw = ImageDraw.Draw(img)
    draw.ellipse(xy=[(100+x,100), (200+x,200)], fill=(0,255,0), width=30)
    imgs.append(img)

imgs[0].save('test.gif', save_all=True, append_images=imgs[1:], loop=0)

