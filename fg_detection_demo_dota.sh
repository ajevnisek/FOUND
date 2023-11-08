PATCH_SIZE=300
ORIGINAL_IMAGE_PATH=data/examples/P0000.png
ORIGINAL_PATCH_DIR=outputs/P0000_original_image_patches/
AUGMENTED_PATCH_DIR=outputs/P0000_patches_with_found_segmentation/
RESULT_IMAGE_WITH_SEGMENTATION=outputs/P0000_found_result.png
ANNOTATIONS_FILE=data/examples/P0000.txt
ALL_IMAGES_RESULT=outputs/P0000_all_images.png


rm -rf ${ORIGINAL_PATCH_DIR}
rm -rf ${AUGMENTED_PATCH_DIR}

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
   --result_path ${ALL_IMAGES_RESULT} --is_dota
