from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import cloudinary
import cloudinary.uploader

# Cloudinary Configuration
cloudinary.config(
    cloud_name="dys8zymcx",
    api_key="754948374267897",
    api_secret="rgvtpvNivIVWoBB7Od2_lE7VzLI"
)

# FastAPI App
app = FastAPI()

# CORS Middleware (Agar frontend se requests allow karna hai)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Saare origins allow karein (production mein specific origins use karein)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Image Upload Endpoint
@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # File ko Cloudinary par upload karein
        result = cloudinary.uploader.upload(file.file, folder="user_images")
        return {"message": "Image uploaded successfully!", "url": result["secure_url"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}