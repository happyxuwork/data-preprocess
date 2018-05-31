from skimage import img_as_float
import matplotlib.pyplot as plt
from skimage import io
from skimage.filters._gaussian import gaussian
import os

file_name='../data/test.jpg'
img=io.imread(file_name)

img = img_as_float(img)

I_out = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3.0

I_invert = 1.0 - I_out

I_gauss = gaussian(I_invert, sigma=5)

delta = 0.0001
I_dodge = (I_out + delta) / (1 + delta - I_gauss)

th = 0.92
mask = I_dodge > th
max_val = I_dodge.max()
I_dodge = I_dodge * (1-mask) + (th + I_dodge / max_val * (1 - th)) * mask

img_out = I_dodge.copy()

import scipy.misc
scipy.misc.toimage(img_out).save(os.path.splitext(file_name)[0]+'copy.jpg')
# lena_L_rgb = img_out.convert("RGB")
# img_out.save(os.path.splitext(path)[0] + '.sk.jpg')

# plt.figure(1)
# plt.imshow(img)
# plt.axis('off')
#
# plt.figure(2)
# plt.imshow(img_out, plt.cm.gray)
# plt.axis('off')
#
# plt.show()