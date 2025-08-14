import os
from PIL import Image

# ==============================
# Configuration
# ==============================
INPUT_FOLDER = "input_images"      # Folder containing original images
OUTPUT_FOLDER = "output_images"    # Folder where resized images will be saved
NEW_SIZE = (800, 800)              # Resize dimensions (width, height)
OUTPUT_FORMAT = "PNG"              # Desired output format ("PNG", "JPEG", etc.)

# ==============================
# Ensure Output Directory Exists
# ==============================
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# ==============================
# Function to Resize & Convert Images
# ==============================
def resize_and_convert_images(input_folder, output_folder, size, output_format):
    """
    Resizes and converts all images in the input folder and saves them to the output folder.
    """
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        try:
            with Image.open(file_path) as img:
                # Resize image
                img_resized = img.resize(size)

                # Remove extension & save in new format
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

                img_resized.save(output_path, output_format.upper())
                print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

# ==============================
# Run the Script
# ==============================
if __name__ == "__main__":
    resize_and_convert_images(INPUT_FOLDER, OUTPUT_FOLDER, NEW_SIZE, OUTPUT_FORMAT)
    print("🎯 Image resizing and conversion complete!")
