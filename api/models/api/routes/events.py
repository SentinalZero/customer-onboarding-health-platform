from fastapi import APIRouter
from api.models.event import UsageEvent

router = APIRouter()
EVENTS = []

@router.post("/events")
def create_event(customer_id: str, event_type: str):
    event = UsageEvent(customer_id, event_type)
    EVENTS.append(event)
    return {
        "message": "event recorded",
        "customer_id": customer_id,
        "event_type": event_type
    }

@router.get("/events/{customer_id}")
def get_events(customer_id: str):
    customer_events = [
        e for e in EVENTS if e.customer_id == customer_id
    ]
    return {"events": customer_events}
