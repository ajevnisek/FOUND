from PIL import Image
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Convert image to patches.")
    parser.add_argument("--image_path", help="Path to image to split")
    parser.add_argument("--output_dir",
                        help="Path patches out directory.")
    parser.add_argument('--patch_size', type=int, default=512)

    args = parser.parse_args()
    return args


def split_image_to_patches(image_path, output_dir, max_patch_size=512):
    # Open the image
    original_image = Image.open(image_path)

    # Get the dimensions of the original image
    width, height = original_image.size

    from math import ceil
    # Calculate the number of patches in the x and y directions
    num_patches_x = ceil(1.0 * width / max_patch_size)
    num_patches_y = ceil(1.0 * height / max_patch_size)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    image_name = os.path.basename(image_path)
    for i in range(num_patches_x):
        for j in range(num_patches_y):
            # Calculate the coordinates for cropping the patch
            left = i * max_patch_size
            upper = j * max_patch_size
            right = min((i + 1) * max_patch_size, width)
            lower = min((j + 1) * max_patch_size, height)

            # Crop the patch from the original image
            patch = original_image.crop((left, upper, right, lower))

            # Save the patch to a file in the output directory
            patch.save(os.path.join(output_dir, f'{image_name[:-len(".png")]}_patch_{i}_{j}.png'))

if __name__ == "__main__":
    args = parse_args()

    image_path = args.image_path
    output_dir = args.output_dir
    patch_size = args.patch_size

    split_image_to_patches(image_path, output_dir, patch_size)
    print(f"Image patches saved to {output_dir}")
