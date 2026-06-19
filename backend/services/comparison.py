from services.llm import (
    llm
)

def compare_contracts(
    contract_a: str,
    contract_b: str
):

    prompt = f"""
You are a legal contract analyst.

Compare the two contracts.

Identify:

1. Added Clauses
2. Removed Clauses
3. Modified Clauses
4. Payment Differences
5. Liability Differences
6. Risk Differences

Return the result in a clear,
structured format.

Contract A:

{contract_a}

--------------------------------

Contract B:

{contract_b}
"""

    response = llm.invoke(
        prompt
    )

    return response.content