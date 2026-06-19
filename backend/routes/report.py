from fastapi import (
    APIRouter,
    Depends
)

from uuid import uuid4

from middleware.auth_middleware import (
    get_current_user
)

from vectorstore.chroma_store import (
    collection
)

from services.summarizer import (
    generate_summary
)

from services.clause_extractor import (
    extract_clauses
)

from services.risk_analyzer import (
    analyze_risks
)

from services.report_generator import (
    generate_report
)

from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/report",
    tags=["Reports"]
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
            meta["file_id"] == file_id
            and
            meta["user_id"] == user_id
        ):
            text += doc + "\n"

    return text
@router.get("/{file_id}")
def create_report(
    file_id: str,
    current_user=Depends(
        get_current_user
    )
):

    document_text = get_document_text(
        file_id,
        current_user["user_id"]
    )

    summary = generate_summary(
        document_text
    )

    clauses = extract_clauses(
        document_text
    )

    risk_report = analyze_risks(
        document_text
    )

    report_name = (
        f"reports/{uuid4()}.pdf"
    )

    generate_report(
        report_name,
        summary,
        risk_report,
        clauses
    )

    return FileResponse(
        path=report_name,
        filename="LegalLens_Report.pdf",
        media_type="application/pdf"
    )