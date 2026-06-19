from fastapi import (
    APIRouter,
    Depends
)

from middleware.auth_middleware import (
    get_current_user
)

from models.comparison import (
    ComparisonRequest
)

from services.comparison import (
    compare_contracts
)

from vectorstore.chroma_store import (
    collection
)

router = APIRouter(
    prefix="/comparison",
    tags=["Comparison"]
)

def get_document_text(
    file_id,
    user_id
):

    results = collection.get()

    text = ""

    for doc, meta in zip(
        results["documents"],
        results["metadatas"]
    ):

        if (
            meta["file_id"]
            == file_id
            and
            meta["user_id"]
            == user_id
        ):

            text += doc + "\n"

    return text

@router.post("/")
def compare_documents(
    data: ComparisonRequest,
    current_user=Depends(
        get_current_user
    )
):

    contract_a = get_document_text(
        data.file_id_1,
        current_user["user_id"]
    )

    contract_b = get_document_text(
        data.file_id_2,
        current_user["user_id"]
    )

    comparison = compare_contracts(
        contract_a,
        contract_b
    )

    return {
        "comparison":
        comparison
    }