PATCH_SIZE=300
TIFF_IMAGE_PATH=data/examples/12308_3840_3840.tiff
ORIGINAL_IMAGE_PATH=data/examples/12308_3840_3840.png
ORIGINAL_PATCH_DIR=outputs/12308_3840_3840_original_image_patches/
AUGMENTED_PATCH_DIR=outputs/12308_3840_3840_patches_with_found_segmentation/
RESULT_IMAGE_WITH_SEGMENTATION=outputs/found_result.png
ANNOTATIONS_FILE=data/examples/12308_3840_3840.txt
ALL_IMAGES_RESULT=outputs/all_images.png


rm -rf ${ORIGINAL_PATCH_DIR}
rm -rf ${AUGMENTED_PATCH_DIR}

python tiff_to_png.py --tiff_images $(dirname ${TIFF_IMAGE_PATH}) \
   --png_images $(dirname ${ORIGINAL_IMAGE_PATH})
python image_to_patches.py --image_path ${ORIGINAL_IMAGE_PATH} \
   --output_dir ${ORIGINAL_PATCH_DIR} --patch_size ${PATCH_SIZE}
for FILE in ${ORIGINAL_PATCH_DIR}*
do
  python main_visualize.py --img-path ${FILE} --output-dir ${AUGMENTED_PATCH_DIR}
done

python patches_to_image.py --augmented_patches_dir ${AUGMENTED_PATCH_DIR}  \
   --image_path ${RESULT_IMAGE_WITH_SEGMENTATION} --original_patches_dir ${ORIGINAL_PATCH_DIR}

python display_results.py --original_path ${ORIGINAL_IMAGE_PATH} \
   --augmented_path ${RESULT_IMAGE_WITH_SEGMENTATION} \
   --annfile_path ${ANNOTATIONS_FILE} \
   --result_path ${ALL_IMAGES_RESULT}
