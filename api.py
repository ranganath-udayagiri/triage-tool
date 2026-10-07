from fastapi import FastAPI

app = FastAPI()

tickets = [
    {"id": 101, "customer": "Rangu", "priority": "HIGH PRIORITY"},
    {"id": 102, "customer": "kohli", "priority": "standard"},
    {"id": 103, "customer": "dhoni", "priority": "aging"},
]

@app.get("/")
def home():
    return {"message": "Triage API is running"}

@app.get("/tickets")
def get_tickets():
    return tickets

@app.get("/tickets/urgent")
def get_urgent_tickets():
    result = []
    for t in tickets:
        if t["priority"] == "HIGH PRIORITY":
            result.append(t)
    return(result)

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    for t in tickets:
        if t["id"] == ticket_id:
            return t