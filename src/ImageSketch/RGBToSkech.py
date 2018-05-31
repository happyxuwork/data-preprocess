from PIL import Image, ImageFilter, ImageOps
from scipy import misc
import numpy as np
img = Image.open('../data/demo4.jpg')
def dodge(a, b, alpha):
    return min(int(a*255/(256-b*alpha)), 255)

def draw(img, blur=25, alpha=1.0):
    img1 = img.convert('L')        #图片转换成灰色
    lena_L_rgb = img1.convert("RGB")
    # img1 = np.array(img1)
    # finalimg = np.array([img1,img1,img1])
    # finalimg = np.reshape(finalimg,[256,256,3])
    # print(lena_L_rgb.shape)
    # img2 = img1.copy()
    # img2 = ImageOps.invert(img2)
    # for i in range(blur):          #模糊度
    #     img2 = img2.filter(ImageFilter.BLUR)
    # width, height = img1.size
    # for x in range(width):
    #     for y in range(height):
    #         a = img1.getpixel((x, y))
    #         b = img2.getpixel((x, y))
    #         img1.putpixel((x, y), dodge(a, b, alpha))
    # img1.show()
    # misc.imsave("33.jpg",lena_L_rgb)
    misc.imsave("4.jpg",lena_L_rgb)
    #img1.save('C:\\Users\\hengli\\Pictures\\CameraMan\\照片1.png')
draw(img)