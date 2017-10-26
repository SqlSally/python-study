#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageFont, ImageDraw

image = Image.open("/Users/sally/Documents/python-study/python - practise/00/img1.png")
w, h = image.size
image.thumbnail((w//2, h//2))
font = ImageFont.truetype('Arial.ttf', 50)
draw = ImageDraw.Draw(image)
draw.text((4.5*w/10, 0), '100', fill=(200, 0, 0), font=font)
image.save('img2.png', 'png')





