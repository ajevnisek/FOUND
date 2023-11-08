import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon


def parse_args():
    parser = argparse.ArgumentParser(description="Display results.")
    parser.add_argument("--original_path", help="Path to the original PNG image.")
    parser.add_argument("--augmented_path", help="Path to the FOUND result image.")
    parser.add_argument("--annfile_path", help="Path to ground truth annotations file.")
    parser.add_argument("--result_path", help="Path to result image.")

    args = parser.parse_args()
    return args


def load_annotations(annfile_path):
    with open(annfile_path, 'r') as f:
        rawdata = f.read()

    coords_list = []
    for line in rawdata.splitlines():
        coords = np.array([float(x) for x in line.split(' ')[:-1]])
        coords = np.array([[x, y] for x, y in zip(coords[::2], coords[1::2])])
        coords_list.append(coords)
    return coords_list


def main():
    args = parse_args()
    original = plt.imread(args.original_path)
    augmented = plt.imread(args.augmented_path)
    coords_list = load_annotations(args.annfile_path)
    len(coords_list)
    plt.subplot(2, 2, 1)
    plt.imshow(original)
    plt.title('original')
    plt.subplot(2, 2, 2)
    plt.imshow(original)
    ax = plt.gca()
    for coords in coords_list:
        p = Polygon(coords, facecolor='m')
        ax.add_patch(p)
    plt.title('ground truth')
    plt.subplot(2, 2, 3)
    plt.title('FOUND result')
    plt.imshow(augmented)
    plt.subplot(2, 2, 4)
    plt.title('FOUND result with GT overlaid on it')
    plt.imshow(augmented)
    ax = plt.gca()
    for coords in coords_list:
        p = Polygon(coords, facecolor='m')
        ax.add_patch(p)
    fig = plt.gcf()
    fig.set_size_inches((15, 15))
    plt.tight_layout()
    plt.savefig(args.result_path)
    print(f"Writing result image to: {args.result_path}")

if __name__ == '__main__':
    main()
