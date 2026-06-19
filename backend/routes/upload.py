from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

import uuid

from middleware.auth_middleware import (
    get_current_user
)

from services.pdf_parser import (
    extract_pages
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
    current_user=Depends(get_current_user)
):

    file_id = str(uuid.uuid4())

    file_path = f"uploads/{file_id}.pdf"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    pages = extract_pages(file_path)

    total_chunks = 0

    for page in pages:

        page_number = page["page_number"]

        chunks = create_chunks(
            page["text"]
        )

        total_chunks += len(chunks)

        for idx, chunk in enumerate(chunks):

            embedding = embedding_model.embed_query(
                chunk
            )

            collection.add(
                ids=[
                    f"{file_id}_{page_number}_{idx}"
                ],
                embeddings=[
                    embedding
                ],
                documents=[
                    chunk
                ],
                metadatas=[{
                    "file_id": file_id,
                    "user_id": current_user["user_id"],
                    "page_number": page_number,
                    "chunk_index": idx,
                    "document_name": file.filename
                }]
            )

    return {
        "message": "Document indexed successfully",
        "file_id": file_id,
        "chunks": total_chunks
    }