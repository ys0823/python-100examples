#---------------------------------------------------------
#题目：使用python给一个彩色图片去色。
#要求：利用python的PIL模块的convert方法给彩色的图片转换一下颜色。
#2018-8-30
#---------------------------------------------------------
from PIL import Image
image_file = Image.open('C:\\Users\\admin\\Desktop\\test.JPG')
image_file = image_file.convert('1')
image_file.save('C:\\Users\\admin\\Desktop\\test1.JPG')

