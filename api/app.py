from fastapi import FastAPI
from api.routes.customers import router as customer_router

app = FastAPI()
app.include_router(customer_router)@app.get("/health")

@app.get("/health")
def health():
    return {"status": "ok"}

