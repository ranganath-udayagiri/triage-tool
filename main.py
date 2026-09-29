import requests

class Ticket:
    def __init__(self, id, customer, is_urgent, hours_open):
        self.id = id
        self.customer = customer
        self.is_urgent = is_urgent
        self.hours_open = hours_open

    def triage(self):
        if self.is_urgent:
            return "HIGH PRIORITY"
        elif self.hours_open > 5:
            return "aging"
        else:
            return "standard"

    def summary(self):
        return f"Ticket {self.id} - {self.customer} - {self.triage()}"


tickets = [
    Ticket(101, "Rangu", True, 6.0),
    Ticket(102, "kohli", False, 5.0),
    Ticket(103, "dhoni", False, 9.5),
]

for t in tickets:
    print(t.summary())

print(f"requests version: {requests.__version__}")