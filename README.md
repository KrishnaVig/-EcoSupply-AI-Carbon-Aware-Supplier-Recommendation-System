# Sustainable Materials Optimizer

Backend-first hackathon starter project with:

- FastAPI backend
- Hard-coded sample supplier/material data
- Basic frontend served by FastAPI
- Simple optimizer module that can later be replaced with PuLP

## Project Structure

```text
app/
  data.py
  main.py
  optimizer.py
  schemas.py
static/
  index.html
requirements.txt
```

## Sample Input

```json
{
  "project_name": "Metro Tower",
  "material": "steel",
  "quantity": 100,
  "budget": 5000000,
  "carbon_limit": 300
}
```

## Run Locally

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`

## Run with Docker

Build and start the backend via Docker:

```powershell
docker compose up --build
```

Then open `http://127.0.0.1:8000`

To stop the service:

```powershell
docker compose down
```

## Main API Endpoints

- `GET /api/health`
- `GET /api/sample-input`
- `GET /api/materials`
- `GET /api/suppliers/{material}`
- `POST /api/optimize`
