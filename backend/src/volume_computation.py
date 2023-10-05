import numpy as np


def calculate_volume(dicom_file, threshold):
    # Extract pixel data as a NumPy array and convert to float
    pixel_data = dicom_file.pixel_array.astype(float)

    # Extract physical spacing information (in millimeters)
    spacing_x, spacing_y = float(dicom_file.PixelSpacing[0]), float(
        dicom_file.PixelSpacing[1]
    )
    slice_thickness = (
        float(dicom_file.SliceThickness)
        if hasattr(dicom_file, "SliceThickness")
        else 1.0
    )

    # Calculate the volume scaling factor based on pixel size and slice thickness
    voxel_volume = spacing_x * spacing_y * slice_thickness

    # Normalize pixel data to [0, 1] range
    min_value = np.min(pixel_data)
    max_value = np.max(pixel_data)
    normalized_pixel_data = (pixel_data - min_value) / (max_value - min_value)

    # Define the threshold (e.g., 0.5)
    threshold = 0.5

    # Threshold the normalized pixel data
    thresholded_pixels = np.where(normalized_pixel_data > threshold, 1, 0)

    # Calculate the volume (in mm^3) based on thresholded voxel counts
    volume_mm3 = np.sum(thresholded_pixels) * voxel_volume
    return round(volume_mm3, 2)
