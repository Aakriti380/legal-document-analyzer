from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.upload import (
    router as upload_router
)
from routes.chat import (
    router as chat_router
)

from routes.summary import (
    router as summary_router
)

from routes.clauses import (
    router as clause_router
)

from routes.risk import (
    router as risk_router
)

from routes.explain import (
    router as explain_router
)

from routes.comparison import (
    router as comparison_router
)

from routes.multi_chat import (
    router as multi_chat_router
)
from routes.report import (
    router as report_router
)


app=FastAPI(
    title="LegalLens AI",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(
    chat_router
)
app.include_router(summary_router)
app.include_router(clause_router)
app.include_router(risk_router)
app.include_router(explain_router)
app.include_router(
    comparison_router
)

app.include_router(
    multi_chat_router
)
app.include_router(
    report_router
)

@app.get("/")
def root():
    return {
        "message": "LegalLens AI Backend Running"
    }