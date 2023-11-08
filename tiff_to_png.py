"""This script converts MAFAT's images which are in tiff format to 8 bit PNG which is upscayl's input format."""

import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser(description="Convert TIFF images to 8 bit PNG (upscayl's input format).")
    parser.add_argument("--tiff_images", help="Path to MAFAT's tiff images directory",
                        default=os.path.join('/home/adminubuntu/Downloads/',
                                             'MAFAT Satellite Vision Challenge - Public Set-20231101T195436Z-001',
                                             'MAFAT Satellite Vision Challenge - Public Set',
                                             'public-20231031T130717Z-001/public/images'))
    parser.add_argument("--png_images",
                        help="Path to PNG images root directory",
                        default='/home/adminubuntu/Desktop/test_aerial_images')

    args = parser.parse_args()
    return args


def convert_tiff_to_png(src_root, target_root):
    images_list = os.listdir(src_root)
    images_list = [img for img in images_list if img.endswith('.tiff')]
    images_list.sort()
    for imagename in tqdm(images_list):
        I = plt.imread(os.path.join(src_root, imagename))
        I_8_bit = (I.astype(np.float32) / 4096.0 * 255.0).astype(np.uint8)
        plt.imsave(os.path.join(target_root, imagename).replace('.tiff', '.png'), I_8_bit, cmap='gray')


def main():
    args = parse_args()
    convert_tiff_to_png(args.tiff_images, args.png_images)


if __name__ == '__main__':
    main()
