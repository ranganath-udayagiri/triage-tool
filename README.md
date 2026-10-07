# Triage Tool

Classifies support tickets as **HIGH PRIORITY**, **aging**, or **standard**.

Part of my AI Engineer learning track. This tool grows into a FastAPI service, then a RAG-powered support agent.

## Run it

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Expected output

```
Ticket 101 - Rangu - HIGH PRIORITY
Ticket 102 - kohli - standard
Ticket 103 - dhoni - aging
requests version: 2.34.2
```
## Run the API

```
fastapi dev api.py
```

Then open http://127.0.0.1:8000/docs

| Endpoint | Returns |
|---|---|
| `GET /` | Health message |
| `GET /tickets` | All tickets |
| `GET /tickets/urgent` | Only HIGH PRIORITY tickets |
| `GET /tickets/{ticket_id}` | One ticket by id |
