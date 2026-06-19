from fastapi import (
    APIRouter,
    Depends
)

from middleware.auth_middleware import (
    get_current_user
)

from services.risk_analyzer import (
    analyze_risks
)

from vectorstore.chroma_store import (
    collection
)

router = APIRouter(
    prefix="/risk",
    tags=["Risk Analysis"]
)

@router.get("/{file_id}")
def risk_report(
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

    report = analyze_risks(
        document_text
    )

    return {
        "risk_report": report
    }