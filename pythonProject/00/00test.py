from PIL import Image

image = Image.open("/Users/sally/Documents/python-study/pythonProject/00/logo.png")
w, h = image.size
image.thumbnail((w*200, h*200))
image.save('logo1.png', 'png')