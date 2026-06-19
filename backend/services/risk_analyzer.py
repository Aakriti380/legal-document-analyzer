from services.llm import llm
import json

def analyze_risks(document_text):

    prompt = f"""
You are a legal risk analyst.

Analyze the contract and return ONLY valid JSON.

Required format:

{{
  "overall_risk": 0,
  "payment_risk": 0,
  "liability_risk": 0,
  "termination_risk": 0,
  "confidentiality_risk": 0,
  "issues": [
    {{
      "type": "",
      "severity": "",
      "description": ""
    }}
  ]
}}

Document:

{document_text}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except:
        return {
            "overall_risk": 0,
            "payment_risk": 0,
            "liability_risk": 0,
            "termination_risk": 0,
            "confidentiality_risk": 0,
            "issues": []
        }