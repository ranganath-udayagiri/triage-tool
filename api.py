from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Triage API is running"}

@app.get("/tickets")
def get_tickets():
    return [
        {"id": 101, "customer": "Rangu", "priority": "HIGH PRIORITY"},
        {"id": 102, "customer": "kohli", "priority": "standard"},
        {"id": 103, "customer": "dhoni", "priority": "aging"},
    ]