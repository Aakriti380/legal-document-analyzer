from pydantic import BaseModel

class ComparisonRequest(
    BaseModel
):
    file_id_1: str
    file_id_2: str