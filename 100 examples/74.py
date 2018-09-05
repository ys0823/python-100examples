#---------------------------------------------------
#题目：给你两张同样尺寸的图片，如何使用python把两张图片合成一张。
#要求：一张图片做底色，一张不改变
#2018-8-28
#---------------------------------------------------
from PIL import Image
infile1 = 'C:\\Users\\admin\\Desktop\\1.jpg'
file1 = 'C:\\Users\\admin\\Desktop\\resize1.jpg'
infile2 = 'C:\\Users\\admin\\Desktop\\2.jpg'
file2 = 'C:\\Users\\admin\\Desktop\\resize2.jpg'

def Image_Resize(infile,outfile):
    '''
    先裁剪图像成同一个大小
    :param infile: 原始图像
    :param outfile: 裁剪后图像
    :return:None
    '''
    im = Image.open(infile)
    #(x,y) = im.size
    x_s = 2500
    y_s = 1800
    out = im.resize((x_s,y_s),Image.ANTIALIAS)
    out.save(outfile)

def blend_two_images(file1, file2):
    img1 = Image.open(file1)
    img2 = img1.convert('RGB')

    img2 = Image.open(file2)
    img2 = img2.convert('RGB')
    #两幅图像进行合并时，按公式：blended_img = img1 * (1 – alpha) + img2* alpha 进行
    imge = Image.blend(img1, img2, 0.5)
    imge.show()
    imge.save('121.JPG')
    return
Image_Resize(infile1, file1)
Image_Resize(infile2,file2)
blend_two_images(file1, file2)


