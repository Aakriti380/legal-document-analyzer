from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_report(
    file_path,
    summary,
    risk_report,
    clauses
):

    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "LegalLens AI Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Contract Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(summary),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            "Risk Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(risk_report),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            "Important Clauses",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(clauses),
            styles["BodyText"]
        )
    )

    doc.build(content)