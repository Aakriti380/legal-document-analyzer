from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

import os
import uuid

from middleware.auth_middleware import (
    get_current_user
)

from services.pdf_parser import (
    extract_text_from_pdf
)

from services.chunker import (
    create_chunks
)

from services.embeddings import (
    embedding_model
)

from vectorstore.chroma_store import (
    collection
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("/")
async def upload_document(
    file: UploadFile = File(...),
    current_user = Depends(get_current_user)
):

    file_id = str(uuid.uuid4())

    file_path = f"uploads/{file_id}.pdf"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_path)

    chunks = create_chunks(text)

    for idx, chunk in enumerate(chunks):

        embedding = embedding_model.embed_query(
            chunk
        )

        collection.add(
            ids=[f"{file_id}_{idx}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "file_id": file_id,
                "user_id": current_user["user_id"]
            }]
        )

    return {
        "message": "Document indexed successfully",
        "file_id": file_id,
        "chunks": len(chunks)
    }