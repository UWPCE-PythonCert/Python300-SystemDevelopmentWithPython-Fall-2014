#!/usr/bin/env python

import numpy as np
from PIL import Image

# add black bands to image, for fun
image = Image.open('test_image.jpg')
image_array = np.asarray(image)
image_array.setflags(write=True)
# glitch data
image_array -= 200
w,h,channels = image_array.shape
for x in xrange(0,w,2):
    image_array[:][x][:] = 0

image2 = Image.fromarray(image_array)
image2.save('out.png')
