import logging
from fastapi import FastAPI
from controllers import document_api, health_api

# Configure logging comprehensively for all services
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(docs_url="/docs")
app.include_router(health_api.router)
app.include_router(document_api.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")