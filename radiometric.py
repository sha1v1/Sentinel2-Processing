import rasterio 
import numpy as np
import matplotlib.pyplot as plt

def read_image(image_path):
    """
    Read the raw image using rasterio.
    
    Parameters:
        image_path (str): Path to the input image.
    
    Returns:
        image (numpy array): Image array of the first band.
        profile (dict): Metadata profile for the image.
    """
    with rasterio.open(image_path) as src:
        image = src.read(1)  # Read the first band
        profile = src.profile
    return image, profile



def save_image(output_path, data, profile):
    """
    Save the radiance-corrected image using rasterio.
    
    Parameters:
        output_path (str): Path to save the output image.
        data (numpy array): Radiance-corrected image data.
        profile (dict): Updated metadata profile for saving.
    """
    profile.update(dtype=rasterio.float32)
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(data.astype(rasterio.float32), 1)


def radiometric_calibration(image, gain, offset):
    """
    Convert Digital Numbers (DN) to radiance using the gain and offset values.
    
    Parameters:
        image (numpy array): Raw image (DN values).
        gain (float): Gain value for radiometric calibration.
        offset (float): Offset value for radiometric calibration.
    
    Returns:
        radiance (numpy array): Image after applying radiometric correction.
    """
    radiance = gain * image + offset
    return radiance

def visualize_images(original, calibrated):
    """
    Visualize the original and radiance-corrected images side by side.
    
    Parameters:
    original (numpy array): The original raw image.
    calibrated (numpy array): The radiance-corrected image.
    """
    plt.figure(figsize=(10, 5))
    
    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image (DN)')
    plt.colorbar()

    # Radiance-corrected image
    plt.subplot(1, 2, 2)
    plt.imshow(calibrated, cmap='gray')
    plt.title('Radiance-Corrected Image')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

def process_radiometric_correction(image_path, gain, offset, output_path):
    """
        Complete workflow for reading, calibrating, and saving an image.
    
    Parameters:
        image_path (str): Path to the input raw image.
        gain (float): Gain value for calibration.
        offset (float): Offset value for calibration.
        output_path (str): Path to save the corrected image.
    """
    # Step 1: Read the raw image
    image, profile = read_image(image_path)

    # Step 2: Perform radiometric correction
    radiance_corrected_image = radiometric_calibration(image, gain, offset)

    # Step 3: Save the corrected image
    save_image(output_path, radiance_corrected_image, profile)

    # Step 4: Visualize the original and corrected images
    visualize_images(image, radiance_corrected_image)