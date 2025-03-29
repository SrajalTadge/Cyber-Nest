from PIL import Image, ExifTags

def extract_exif(image_file):
    """
    Extracts EXIF data from an image file (supports JPEG and other formats).
    Returns a dictionary of EXIF tags and their values.
    """
    try:
        # Reset file pointer to the beginning
        image_file.seek(0)
        
        image = Image.open(image_file)
        exif_data = {}

        # Try to use getexif() (recommended for Pillow >= 6.0)
        if hasattr(image, 'getexif'):
            exif_raw = image.getexif()
            if exif_raw:
                for tag, value in exif_raw.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    exif_data[tag_name] = value
        # Fallback for older versions of Pillow
        elif hasattr(image, '_getexif'):
            exif_raw = image._getexif()
            if exif_raw:
                for tag, value in exif_raw.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    exif_data[tag_name] = value

        return exif_data
    except Exception as e:
        raise ValueError("Error extracting EXIF data: " + str(e))
