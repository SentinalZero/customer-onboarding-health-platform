from fastapi import APIRouter
from api.models.customer import Customer

router = APIRouter()
CUSTOMERS = {}

@router.post("/customers")
def create_customer(id: str, name: str):
    customer = Customer(id, name)
    CUSTOMERS[id] = customer
    return {"id": id, "name": name}

@router.post("/customers/{id}/onboarding-step")
def add_onboarding_step(id: str, step: str):
    customer = CUSTOMERS[id]
    customer.onboarding_steps.append(step)
    return {"onboarding_steps": customer.onboarding_steps}
