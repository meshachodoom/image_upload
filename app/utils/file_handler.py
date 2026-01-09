import os
import uuid
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "./uploads"))

def create_upload_directory() -> None:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def save_image(file_content: bytes, file_extension: str) -> str:
    
    create_upload_directory()
    
    image_id = str(uuid.uuid4())
    
    file_path = UPLOAD_DIR / f"{image_id}.{file_extension}"
    
    with open(file_path, "wb") as f:
        f.write(file_content)
    
    return image_id