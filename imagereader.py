from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def exif_extract(image_name):
	image = Image.open(image_name)
	return image._getexif()

def non_exif_extract(image_name):
	image = Image.open(image_name)
	return image.info



