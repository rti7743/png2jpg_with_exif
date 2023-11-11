import sys
import os
import piexif
import pickle
from PIL import Image
from PIL.PngImagePlugin import PngInfo

def convert_png_to_jpg(png_filename):
    # Check if the input file exists
    if not os.path.exists(png_filename):
        print(f"Error: File '{png_filename}' does not exist.")
        return

    # Save as JPEG image with maximum quality (100)
    jpg_filename = png_filename.replace(".png", ".jpg")

    # Copy Exif data from PNG to JPEG
    img = Image.open(png_filename)

    data = pickle.dumps(img.text)
    exif_ifd = {piexif.ExifIFD.MakerNote: data}
    exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {},
                 "thumbnail": None, "GPS": {}}
    exif_bytes = piexif.dump(exif_dict)
    img.save(jpg_filename, exif=exif_bytes)

    #print(f"{png_filename} converted to {jpg_filename} with preserved Exif data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python png2jpg_with_exif.py <png_filename>")
    else:
        png_filename = sys.argv[1]
        convert_png_to_jpg(png_filename)

