from services.llm import llm

def explain_in_hindi(clause):

    prompt = f"""
Explain the legal clause in:

1. Simple English
2. Hindi

Clause:

{clause}
"""

    response = llm.invoke(
        prompt
    )

    return response.content