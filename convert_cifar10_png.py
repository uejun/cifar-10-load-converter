# coding: UTF-8

from __future__ import  absolute_import
from __future__ import division
from __future__ import print_function

import os
import argparse
import numpy as np
from PIL import Image

from reader import Cifar10Reader


def convert(datafile, basename, offset=0, count=1, save_dir='./data'):

    reader = Cifar10Reader(datafile)
    stop = offset + count

    for index in range(offset, stop):
        image = reader.read(index)

        im = Image.fromarray(image.byte_array.astype(np.uint8))


        file_name='%s-%02d-%d' % (basename, index, image.label)
        file_name = file_name + ".png"

        with open(save_dir+'/'+ file_name, mode='wb') as out:
            im.save(out, format='png')

    reader.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cifar-10 converter')
    parser.add_argument('--offset', type=int, default=None)
    parser.add_argument('--count', type=int, default=None)
    parser.add_argument('--data', type=str, default=None)
    parser.add_argument('--save_dir', type=str, default=None)
    args = parser.parse_args()

    basename = os.path.basename(args.data)
    convert(args.data, basename, args.offset, args.count, args.save_dir)
