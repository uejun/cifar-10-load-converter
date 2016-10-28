# cifar10 png converter

## Usage

Download the data "CIFAR-10 binary version" from [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)

```
$ python convert_cifar10_png.py \
    --offset 0 \
    --count 3 \
    --data /YOUR_PATTH_TO/test_batch.bin
    --save_dir PATH_TO_PNG_SAVE_DIR
```