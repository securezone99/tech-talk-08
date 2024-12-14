#app/config/litellm_config.property
import os, litellm, logging
from pydantic import BaseModel
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv(override=True)

class LiteLLMConfig(BaseModel):
    """
    Settings for LiteLLM configuration
    """
    #print LITELLM_KEY and ENVIRONMENT
    print(os.getenv("LITELLM_KEY", ""))
    print(os.getenv("ENVIRONMENT", "DEVELOP"))
    
    api_key: str = os.getenv("LITELLM_KEY", "")
    environment: str = os.getenv("ENVIRONMENT", "DEVELOP")

    def initialize(self):
        """Initialize LiteLLM configuration """
        
        litellm.api_key = self.api_key
        
        # Log the first 4 and last 4 characters of the API key for identification
        if self.api_key:
            masked_key = f"{self.api_key[:4]}{'*' * (len(self.api_key) - 8)}{self.api_key[-4:]}"
            logger.info(f"LiteLLM API Key set: {masked_key}")
        else:
            logger.warning("No LiteLLM API Key provided")

    class Config:
        env_prefix = "LITELLM_"
        case_sensitive = False