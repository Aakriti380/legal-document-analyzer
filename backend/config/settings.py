from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

JWT_SECRET=os.getenv("JWT_SECRET")
JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")