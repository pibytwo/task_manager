"""Main app"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load .env only in development
if os.getenv("ENV", "dev") == "dev":
    import dotenv
    dotenv.load_dotenv()

from src.router import app_router


app = FastAPI(
    title="Task Manager",
    version="2025.06.26",
)

origins = ["*"]  # Mention specific domains to restrict unwanted access

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies / credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
