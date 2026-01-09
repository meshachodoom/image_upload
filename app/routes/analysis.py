from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.analysis_service import analyze_image
from app.utils.auth import verify_api_key
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(prefix="/api/v1", tags=["analysis"])

class AnalyzeRequest(BaseModel):
    image_id: str

class AnalyzeResponse(BaseModel):
    image_id: str
    skin_type: str
    issues: list[str]
    confidence: float

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_endpoint(
    request: AnalyzeRequest,
    user: str = Depends(verify_api_key)
):
    """
    Analyze an image by image_id.
    
    - Accepts an image_id from a previous upload
    - Performs mock analysis
    - Returns: skin type, detected issues, and confidence score
    """
    logger.info(f"Analysis request from user: {user}, image_id: {request.image_id}")
    try:
        result = await analyze_image(request.image_id)
        logger.info(f"Analysis completed for image_id: {request.image_id}")
        return result
    except ValueError as e:
        logger.warning(f"Analysis failed - Image not found: {request.image_id}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error during analysis: {str(e)}")
        raise