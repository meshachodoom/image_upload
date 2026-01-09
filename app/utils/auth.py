from fastapi import HTTPException, Depends, Header
from typing import Optional
import os
from dotenv import load_dotenv
from app.utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)

VALID_API_KEYS = {}

for key, value in os.environ.items():
    if key.startswith("API_KEY_") and not key.endswith("_USER"):
        user_key = key + "_USER"
        user_name = os.getenv(user_key, "Unknown User")
        VALID_API_KEYS[value] = user_name

def verify_api_key(x_api_key: Optional[str] = Header(None)) -> str:
   
    if not x_api_key:
        logger.warning("API request without API key header")
        raise HTTPException(
            status_code=401,
            detail="Missing API key. Include 'X-API-Key' header in your request."
        )
    
    if x_api_key not in VALID_API_KEYS:
        logger.warning(f"API request with invalid API key: {x_api_key[:8]}...")
        raise HTTPException(
            status_code=403,
            detail="Invalid API key."
        )
    
    user = VALID_API_KEYS[x_api_key]
    logger.info(f"API key verified for user: {user}")
    return user