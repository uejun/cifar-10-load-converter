# coding: UTF-8

from __future__ import  absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
from PIL import Image

from reader import Cifar10Reader
import sys

basename = os.path.basename(sys.argv[1])
print(basename)
path = os.path.dirname(sys.argv[1])

reader = Cifar10Reader(sys.argv[1])

stop = 0 + 1000
for index in range(1000, 10000):
    image = reader.read(index)

    print('label: %d' % image.label)
    imageshow = Image.fromarray(image.byte_array.astype(np.uint8))

    file_name='%s-%02d-%d.png' % (basename, index, image.label)

    with open('./data/'+ file_name, mode='wb') as out:
        imageshow.save(out, format='png')


reader.close()
