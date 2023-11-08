from PIL import Image
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Convert patches dir to image.")
    parser.add_argument("--augmented_patches_dir",
                        help="Path patches directory.")
    parser.add_argument("--original_patches_dir",
                        help="Path patches directory.")
    parser.add_argument("--image_path", help="Path to image.")
    args = parser.parse_args()
    return args


def reassemble_patches(augmented_patch_dir, original_patch_dir, output_path):
    # Get a list of all patch files in the patch directory
    augmented_patch_files = [f for f in os.listdir(augmented_patch_dir) if os.path.isfile(os.path.join(augmented_patch_dir, f))]

    if not augmented_patch_files:
        print("No patch files found in the specified directory.")
        return

    # Create a dictionary to store patches and their corresponding indices (i, j)
    patch_dict = {}
    for patch_file in augmented_patch_files:
        i = int(patch_file.split('_')[-2])
        try:
            j  = int(patch_file.split('_')[-1].split('.png')[0])
        except:
            j = int(patch_file.split('_')[-1].split('-found.png')[0])
        # i, j = map(int, patch_file.split('_')[1:3])
        patch = Image.open(os.path.join(augmented_patch_dir, patch_file))
        original_patch = Image.open(os.path.join(original_patch_dir, patch_file.split('-found')[0] + '.png'))
        # import ipdb; ipdb.set_trace()
        patch = patch.resize(original_patch.size)
        patch_dict[(i, j)] = patch

    # Determine the dimensions of the reassembled image
    max_i = max([i for i, _ in patch_dict.keys()])
    max_j = max([j for _, j in patch_dict.keys()])
    min_i = min([i for i, _ in patch_dict.keys()])
    min_j = min([j for _, j in patch_dict.keys()])

    total_width = 0
    total_height = 0

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if (i, j) in patch_dict:
                patch = patch_dict[(i, j)]
                width, height = patch.size
                if i == 0:
                    total_height += height
                if j == 0:
                    total_width += width

    # Create an empty image to build the reassembled image
    # print(total_height, total_width)
    reassembled_image = Image.new("RGB", (total_width, total_height))



    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if (i, j) in patch_dict:
                current_x = 0
                current_y = 0
                for k in range(min_i, max_i + 1):
                    if (k, j) in patch_dict and k < i:
                        patch = patch_dict[(k, j)]
                        width, height = patch.size
                        current_x += width
                for m in range(min_j, max_j + 1):
                    if (i, m) in patch_dict and m < j:
                        patch = patch_dict[(i, m)]
                        width, height = patch.size
                        current_y += height
                current_patch = patch_dict[(i, j)]
                # print(f"{i, j} pasted in {current_y, current_x}")
                reassembled_image.paste(current_patch, (current_x, current_y))

    # Save the reassembled image
    reassembled_image.save(output_path)





if __name__ == "__main__":
    args = parse_args()
    augmented_patches_dir = args.augmented_patches_dir  # Replace with the directory containing patch files
    original_patches_dir = args.original_patches_dir  # Replace with the directory containing patch files
    output_path = args.image_path  # Output path for the reassembled image

    reassemble_patches(augmented_patches_dir, original_patches_dir, output_path)
    print(f"Reassembled image saved to {output_path}")
