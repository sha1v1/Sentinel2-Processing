from radiometric import process_radiometric_correction

def main():
    image_path = "p016r37_1m19730918_01.tif"
    output_path = "corrected.tif"

    
    gain = 0.368  
    offset = 1  

    # Call the processing function to perform the workflow
    process_radiometric_correction(image_path, gain, offset, output_path)

if __name__ == "__main__":
    main()