from fastapi import APIRouter
from pydantic import BaseModel

from services.translator import (
    explain_in_hindi
)

router = APIRouter(
    prefix="/explain",
    tags=["Legal Explanation"]
)

class ClauseRequest(
    BaseModel
):
    clause: str
    
@router.post("/")
def explain_clause(
    data: ClauseRequest
):

    result = explain_in_hindi(
        data.clause
    )

    return {
        "explanation": result
    }