from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.upload import (
    router as upload_router
)

app.include_router(upload_router)

app=FastAPI(
    title="LegalLens AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "LegalLens AI Backend Running"
    }