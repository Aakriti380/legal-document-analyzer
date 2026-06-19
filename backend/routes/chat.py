from fastapi import (
    APIRouter,
    Depends
)

from pydantic import BaseModel

from middleware.auth_middleware import (
    get_current_user
)

from services.retriever import (
    retrieve_chunks
)

from services.llm import (
    llm
)

from config.database import (
    chats_collection
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class QuestionRequest(
    BaseModel
):
    file_id: str
    question: str


@router.post("/")
def ask_question(
    data: QuestionRequest,
    current_user=Depends(
        get_current_user
    )
):

    retrieved_data = retrieve_chunks(
        question=data.question,
        file_id=data.file_id,
        user_id=current_user[
            "user_id"
        ]
    )

    chunks = retrieved_data[
        "chunks"
    ]

    metadata = retrieved_data[
        "metadata"
    ]

    context = "\n\n".join(
        chunks
    )

    prompt = f"""
You are a legal document assistant.

Answer ONLY using the
provided context.

If the answer is not found
in the context, reply:

"Information not found in the uploaded document."

Context:
{context}

Question:
{data.question}
"""

    response = llm.invoke(
        prompt
    )

    answer = response.content

    chats_collection.insert_one({
        "user_id":
        current_user["user_id"],

        "file_id":
        data.file_id,

        "question":
        data.question,

        "answer":
        answer
    })

    seen = set()

    citations = []

    for meta in metadata:

        key = (
            meta["document_name"],
            meta["page_number"]
        )

        if key not in seen:

            seen.add(key)

            citations.append({
                "document_name":
                meta["document_name"],

                "page_number":
                meta["page_number"]
            })

    return {
        "answer": answer,
        "citations": citations
    }


@router.get("/history/{file_id}")
def get_chat_history(
    file_id: str,
    current_user=Depends(
        get_current_user
    )
):

    chats = list(
        chats_collection.find(
            {
                "user_id":
                current_user["user_id"],

                "file_id":
                file_id
            },
            {
                "_id": 0
            }
        )
    )

    return chats