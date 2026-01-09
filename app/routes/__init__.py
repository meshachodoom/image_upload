from fastapi import APIRouter
from app.routes.upload import router as upload_router
from app.routes.analysis import router as analysis_router

router = APIRouter()
router.include_router(upload_router)
router.include_router(analysis_router)