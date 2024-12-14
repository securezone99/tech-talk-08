
#app/services/document_embedding_service.py
import io, logging
from enum import Enum
from pypdf import PdfReader
from http.client import HTTPException
from fastapi import UploadFile, HTTPException

logger = logging.getLogger(__name__)

class DocumentEmbeddingService:
    """Service for handling document embeddings and similarity calculations"""

    def __init__(self):
        pass

    async def get_document_text(self, file: UploadFile, max_pages: int = None) -> str:
        """
        Extract text content from a PDF up to max_pages
        
        Args:
            file (UploadFile): PDF file
            max_pages (int): Maximum number of pages to extract, defaults to all pages
            
        Returns:
            str: Extracted text from the PDF
        """
        try:
            logger.info("Starting text extraction from PDF")
            file_content = await file.read()
            
            pdf_file = io.BytesIO(file_content)
            pdf_reader = PdfReader(pdf_file)
            
            total_pages = len(pdf_reader.pages)
            pages_to_extract = min(max_pages, total_pages) if max_pages else total_pages
            
            extracted_text = []
            for page_num in range(pages_to_extract):
                text = pdf_reader.pages[page_num].extract_text()
                if text:
                    extracted_text.append(text)
                logger.debug(f"Extracted text from page {page_num + 1}")
            
            full_text = " ".join(extracted_text).strip()
            
            if not full_text:
                raise HTTPException(
                    status_code=422,
                    detail="PDF appears to be empty or contains no extractable text"
                )
            
            logger.info(f"Text extraction complete - length: {len(full_text)}")
            return full_text
            
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {str(e)}", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail=f"Error extracting text from PDF: {str(e)}"
            )
