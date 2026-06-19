from fastapi import (
    APIRouter,
    Depends
)

from pydantic import BaseModel

from middleware.auth_middleware import (
    get_current_user
)

from services.retriever import (
    retrieve_chunks_across_documents
)

from services.llm import (
    llm
)

router = APIRouter(
    prefix="/multi-chat",
    tags=["Multi Document Chat"]
)

class MultiQuestionRequest(
    BaseModel
):
    question: str
    
@router.post("/")
def ask_across_documents(
    data: MultiQuestionRequest,
    current_user=Depends(
        get_current_user
    )
):

    retrieved_data = (
        retrieve_chunks_across_documents(
            question=data.question,
            user_id=current_user[
                "user_id"
            ]
        )
    )

    chunks = (
        retrieved_data["chunks"]
    )

    metadata = (
        retrieved_data["metadata"]
    )

    context = ""

    for chunk, meta in zip(
        chunks,
        metadata
    ):

        context += f"""
Document:
{meta['document_name']}

Page:
{meta['page_number']}

Content:
{chunk}

-------------------
"""

    prompt = f"""
You are a legal analyst.

The context contains
information from multiple
legal documents.

When answering:

- Mention document names.
- Mention page numbers.
- Compare documents if needed.
- Use only provided context.

Context:

{context}

Question:

{data.question}
"""

    response = llm.invoke(
        prompt
    )

    return {
        "answer":
        response.content
    }