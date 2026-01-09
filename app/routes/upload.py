from fastapi import APIRouter, UploadFile, File, Depends
from app.services.image_service import upload_image
from app.utils.auth import verify_api_key
from app.utils.logger import get_logger

router = APIRouter(prefix="/api/v1", tags=["upload"])
logger = get_logger(__name__)

@router.post("/upload")
async def upload_endpoint(
    image: UploadFile = File(...),
    user: str = Depends(verify_api_key)
    ):
    """
    Upload an image file.
    
    - Accepts JPEG or PNG files
    - Maximum file size: 5MB
    - Returns: image_id
    """
    logger.info(f"Upload request from user: {user}, filename: {image.filename}")
    try:
        result = await upload_image(image)
        logger.info(f"Image uploaded successfully. Image ID: {result['image_id']}")
        return result
    except Exception as e:
        logger.error(f"Upload failed for user {user}: {str(e)}")
        raise 