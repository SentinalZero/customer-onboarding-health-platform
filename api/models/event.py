from datetime import datetime

class UsageEvent:
    def __init__(self, customer_id: str, event_type: str):
        self.customer_id = customer_id
        self.event_type = event_type
        self.timestamp = datetime.utcnow()
