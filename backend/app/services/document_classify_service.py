#app/services/document_classify_service.py
import json, logging, os
from fastapi import UploadFile
from typing import Dict
from services.document_embedding_service import DocumentEmbeddingService
from litellm import completion
from config.litellm_config import LiteLLMConfig
from models.document_types import DocumentClassification
from litellm.utils import trim_messages

logger = logging.getLogger(__name__)

class DocumentClassifierService:
    """Service for classifying documents using embeddings"""
    def __init__(self):
        config = LiteLLMConfig()
        config.initialize()
        self.embedding_service = DocumentEmbeddingService()
        
    async def classify_document_with_genai(self, file: UploadFile) -> Dict:
        try:

            extracted_text = await self.embedding_service.get_document_text(file, max_pages=100)
                
            system_message = """Analyze the document content and classify it into one of the predefined document types.
                Return a JSON object with the type, confidence, and brief reasoning."""
            user_message = f"Classify this document:\n\n{extracted_text[:2000]}"
            
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
            
            response = completion(
                model=os.getenv("MODEL_DOCUMENT_CLASSIFIER", ""),
                messages=messages,
                response_format=DocumentClassification
            )
            result = json.loads(response.choices[0].message.content)
            if 'confidence_score' in result:
                result['confidence'] = result.pop('confidence_score')
                
            return DocumentClassification(**result)
            
        except Exception as e:
            logger.error(f"Error in document classification: {e}")
            raise
            
    # trim_messages ensures tokens(messages) < max_tokens(model)
    def show_litemlm_helper_functions(self):
        
        model = os.getenv("MODEL_DOCUMENT_CLASSIFIER", "")
        messages = [
            {"role": "system", "content": "This is a system message"},
            {"role": "user", "content": "This is a user message"}
        ]

        response = completion(
            model=model,
            messages=trim_messages(messages, model) 
        ) 
        return response.choices[0].message.content
    

