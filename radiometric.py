import rasterio 
import numpy as np
import matplotlib.pyplot as plt

def read_image(image_path):
    """Read the raw image using rasterio."""
    with rasterio.open(image_path) as src:
        image = src.read(1)  # Read the first band
        profile = src.profile
    return image, profile



def save_image(output_path, data, profile):
    """Save the radiance-corrected image using rasterio."""
    profile.update(dtype=rasterio.float32)
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(data.astype(rasterio.float32), 1)


def radiometric_calibration(image, gain, offset):
    """Convert DN to radiance."""
    radiance = gain * image + offset
    return radiance