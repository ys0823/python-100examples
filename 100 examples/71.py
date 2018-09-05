#--------------------------------------------------
#使用pillow模块生成字母验证码图片
#结合pillow的用法:https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
#2018-8-26
#--------------------------------------------------
#coding:utf-8
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色1,背景色
def rndColor():
    return (random.randint(200, 255),random.randint(200,255), random.randint(200,255))
#随机颜色2,字体色
def rndColor2():
    return (random.randint(32, 127),random.randint(32,127), random.randint(32,127))

#240 x 60
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
#创建Font对象,加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。
#这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。
font = ImageFont.truetype('fangsong_GB2312.ttf', 36)
#创建Draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndColor())

#输出文字
for t in range(4):
    draw.text((60 * t +10, 10),rndChar(), font = font, fill = rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save('E:\\叶盛\\研究生学习\\python\\100 例\\71\\code.jpg','jpeg')

