from skimage import transform,data,io
import scipy
from PIL import Image

path = "E:\programdate\python-all-in-for-happyxuwork\data-preprocess\src\data\demo4.jpg"
im = Image.open(path)
width,height = im.size
out = im.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
out.save("./1.jpg")
# img = im.camera()
# print(type(data))
# print(img.shape)
# new_img=transform.rescale(img, [0.5,0.5])
# print(new_img.shape)
# io.imshow(new_img)
# io.show()