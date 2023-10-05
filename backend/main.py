from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydicom import dcmread
from fastapi.responses import JSONResponse
from settings import Settings

from src.volume_computation import calculate_volume


settings = Settings()
app = FastAPI()


origins = ["*"]  # Replace with the actual origin of your Vue.js frontend in production


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/")
async def upload_and_process_dicom(file: UploadFile):
    try:
        dicom_file = dcmread(file.file)
        volume = calculate_volume(dicom_file, settings.threshold)
        return JSONResponse(content={"volume_mm3": volume})
    except Exception as e:
        # Future work: Specify Exception and specific errors: validity, missing metadata, correct file format etc ...
        # Specify message for each error
        return JSONResponse(content={"error": str(e)})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
