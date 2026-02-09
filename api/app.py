from fastapi import FastAPI
from api.routes.customers import router as customer_router
from api.routes.events import router as events_router

app = FastAPI()

app.include_router(customer_router)
app.include_router(events_router)

@app.get("/health")
def health():
    return {"status": "ok"}
