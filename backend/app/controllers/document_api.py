#app/controllers/document_api.py
import logging
from fastapi import APIRouter, UploadFile, File
from services.document_classify_service import DocumentClassifierService

router = APIRouter(prefix="/api", tags=["document-api"])
logger = logging.getLogger(__name__)

@router.post("/classify_document_type")
async def upload_pdf(file: UploadFile = File(...)):
    return await DocumentClassifierService().classify_document_with_genai(file)

@router.get("/show_litemlm_helper_functions")
async def show_litemlm_helper_functions():
    return DocumentClassifierService().show_litemlm_helper_functions()

@router.get("/show_litemlm_helper_functions_with_caching")
async def show_litemlm_helper_functions_with_caching():
    return DocumentClassifierService().show_litemlm_helper_functions_with_caching()