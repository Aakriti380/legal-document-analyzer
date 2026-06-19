from services.llm import llm

def extract_clauses(document_text):

    prompt = f"""
Extract the following clauses
from the legal document.

1. Payment Clause
2. Termination Clause
3. Liability Clause
4. Confidentiality Clause
5. Renewal Clause
6. Dispute Resolution Clause

Document:

{document_text}

Return clearly separated sections.
"""

    response = llm.invoke(
        prompt
    )

    return response.content