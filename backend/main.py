from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydicom import dcmread
import numpy as np
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()


origins = ["*"]  # Replace with the actual origin of your Vue.js frontend in production


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.post("/upload/")
async def upload_and_process_dicom(file: UploadFile, threshold: Optional[float] = 0.5):
    try:
        dicom_file = dcmread(file.file)
        volume = calculate_volume(dicom_file, threshold)
        return JSONResponse(content={"volume_mm3": volume})
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
