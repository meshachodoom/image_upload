import os
from dotenv import load_dotenv
from fastapi import UploadFile, HTTPException

load_dotenv()

ALLOWED_EXTENSIONS = {"jpeg", "jpg", "png"}
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE_MB", 5)) * 1024 * 1024  # Convert MB to bytes


def validate_image(file: UploadFile) -> None:
    
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            message=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    if file.size and file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            message=f"File size exceeds maximum allowed size of 5MB"
        )