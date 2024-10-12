from PIL import Image
import piexif



def extract_date_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Extract the EXIF data
        exif_data = piexif.load(img.info['exif'])
        
        # Get the date the image was originally taken (DateTimeOriginal)
        date_taken = exif_data['Exif'][piexif.ExifIFD.DateTimeOriginal].decode('utf-8')
        
        print(f"Date the image was taken: {date_taken}")
        return date_taken
    except KeyError:
        print("No EXIF date data found in this image.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
image_path = r"C:\Users\lachl\McIntosh-Sydney Capital Holdings Group\Personal - Documents\Travelling\2024 7 China & Thailand\Media\100CANON\IMG_0121 - Copy.JPG"
extract_date_from_image(image_path)
