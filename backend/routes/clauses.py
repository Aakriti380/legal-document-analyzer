from fastapi import (
    APIRouter,
    Depends
)

from middleware.auth_middleware import (
    get_current_user
)

from services.clause_extractor import (
    extract_clauses
)

from vectorstore.chroma_store import (
    collection
)

router = APIRouter(
    prefix="/clauses",
    tags=["Clauses"]
)

@router.get("/{file_id}")
def get_clauses(
    file_id: str,
    current_user=Depends(
        get_current_user
    )
):

    results = collection.get()

    document_text = ""

    for doc, meta in zip(
        results["documents"],
        results["metadatas"]
    ):

        if (
            meta["file_id"] == file_id
            and
            meta["user_id"]
            ==
            current_user["user_id"]
        ):
            document_text += doc

    clauses = extract_clauses(
        document_text
    )

    return {
        "clauses": clauses
    }