PATCH_SIZE=200
TIFF_IMAGE_PATH=data/examples/9835_3840_6400.tiff
ORIGINAL_IMAGE_PATH=data/examples/9835_3840_6400.png
ORIGINAL_PATCH_DIR=data/examples/9835_3840_6400/
AUGMENTED_PATCH_DIR=outputs/9835_3840_6400/
RESULT_IMAGE_WITH_SEGMENTATION=outputs/result.png


python tiff_to_png.py --tiff_images $(dirname ${TIFF_IMAGE_PATH}) --png_images $(dirname ${ORIGINAL_IMAGE_PATH})
python image_to_patches.py --image_path ${ORIGINAL_IMAGE_PATH} \
   --output_dir ${ORIGINAL_PATCH_DIR} --patch_size ${PATCH_SIZE}
for FILE in ${ORIGINAL_PATCH_DIR}*
do
  python main_visualize.py --img-path ${FILE} --output-dir ${AUGMENTED_PATCH_DIR}
done

python patches_to_image.py --augmented_patches_dir ${AUGMENTED_PATCH_DIR}  \
   --image_path ${RESULT_IMAGE_WITH_SEGMENTATION} --original_patches_dir ${ORIGINAL_PATCH_DIR}