from services.llm import llm

def generate_summary(document_text):

    prompt = f"""
You are a legal contract analyst.

Analyze the document and extract:

1. Parties Involved
2. Contract Duration
3. Payment Terms
4. Responsibilities
5. Termination Conditions
6. Dispute Resolution

Return response in structured format.

Document:

{document_text}
"""

    response = llm.invoke(prompt)

    return response.content