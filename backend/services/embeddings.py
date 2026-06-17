from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config.settings import (
    GEMINI_API_KEY
)

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY
)