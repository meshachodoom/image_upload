from fastapi import UploadFile
from app.utils.validators import validate_image
from app.utils.file_handler import save_image

async def upload_image(image: UploadFile) -> dict:
   
    validate_image(image)
    
    file_content = await image.read()
    
    file_extension = image.filename.split(".")[-1].lower()
    
    image_id = save_image(file_content, file_extension)
    
    return {"image_id": image_id}