<br>
<div align="left">
  <img
    src="https://drive.google.com/uc?export=view&id=1YhXegnF3JsG51RUCGZIL1_6P9fGqCxbW"
    alt="Tiara"
    style="width:100%; max-width:1400px;"
  />
</div>
<br>

> **⚕️ Medical Disclaimer**: TIARA is not a medical diagnosis tool. It is a cognitive trend monitoring and caregiver support platform. All outputs are informational only and should not replace professional clinical assessment.

---

## What is TIARA?

TIARA (Thinking, Interaction, And Recall Assistant) is an AI-powered early cognitive risk screening and caregiver support platform for elderly users, their caregivers, and healthcare workers.

TIARA uses daily AI-guided conversations — voice, video, and language signals — to monitor cognitive trends over time and surface early indicators that may warrant timely clinical attention.

### Core User Flows

```
Elderly User:
  Login → Home → Daily Check-In (camera + mic + AI questions) → Warm result

Caregiver:
  Profile → PIN Entry → Dashboard Analytics → Alerts → Recommendations → Guidance AI → Reports

Healthcare Worker:
  Login → Patient List → Session History → Longitudinal Trends
```

---

## Features

- 🎥 **Daily Video/Audio Check-In** — AI-guided spoken questions with real recording
- 🧠 **AI Analysis Pipeline** — Transcription, voice features, language analysis, risk scoring
- 📊 **Caregiver Dashboard** — Real-time cognitive trend charts and analytics
- 🔔 **Smart Alerts** — Pattern-based caregiver notifications
- 💬 **Dementia Guidance AI** — Evidence-informed caregiver chatbot
- 📋 **Monthly Reports** — Downloadable care summaries
- 🏥 **Healthcare Worker Portal** — Patient monitoring dashboard
- 🔐 **PIN-Protected Caregiver Access** — Shared device safety

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14 + TypeScript + Tailwind CSS + shadcn/ui |
| Backend | FastAPI + Python + SQLAlchemy + PostgreSQL |
| Auth | JWT + Passlib (bcrypt) |
| AI/STT | faster-whisper + librosa + OpenCV |
| Charts | Recharts |
| Migrations | Alembic |
| Infrastructure | Docker + Docker Compose |

---

## Architecture Overview

```
Frontend (Next.js)
    │
    │ REST API + JWT
    ▼
Backend (FastAPI)
  ├── Auth Routes
  ├── Elderly Routes
  ├── Check-in Routes
  ├── Caregiver Routes
  ├── Healthcare Routes
  └── AI Pipeline
        ├── TranscriptionService (Whisper)
        ├── VoiceAnalysisService (librosa)
        ├── LanguageAnalysisService (rule-based + LLM-ready)
        ├── FacialAnalysisService (OpenCV/MediaPipe)
        └── RiskScoringService
    │
    ▼
PostgreSQL Database
```

---

## Folder Structure

```
tiara/
├── frontend/              # Next.js App Router
│   ├── app/               # Pages
│   ├── components/        # UI components
│   └── lib/               # API client, auth, types, hooks
├── backend/               # FastAPI
│   ├── app/
│   │   ├── core/          # Config, security, constants
│   │   ├── database/      # Session management
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── routes/        # HTTP handlers
│   │   ├── services/      # Business logic + AI pipeline
│   │   ├── repositories/  # Database access
│   │   └── scripts/       # Seed, migration helpers
│   └── alembic/           # Database migrations
├── docs/                  # Documentation (9 docs)
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## How to Run

### Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL 15+
- (Optional) Docker + Docker Compose

---

### Option A: Docker Compose (Recommended)

```bash
# 1. Copy environment file
cp .env.example .env

# 2. Edit .env — set a strong JWT_SECRET_KEY
nano .env

# 3. Start all services
docker-compose up --build

# Frontend: http://localhost:3000
# Backend:  http://localhost:8000
# API docs: http://localhost:8000/docs
```

---

### Option B: Manual Setup

#### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp ../.env.example .env
# Edit .env with your PostgreSQL connection string and JWT secret

# Run database migrations
alembic upgrade head

# Seed demo users
python -m app.scripts.seed

# Start backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Copy and configure environment
cp .env.local.example .env.local
# NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1

# Start frontend
npm run dev
```

---

## Database Setup

```bash
# Create PostgreSQL database
psql -U postgres -c "CREATE USER tiara WITH PASSWORD 'tiara_password';"
psql -U postgres -c "CREATE DATABASE tiara_db OWNER tiara;"

# Run Alembic migrations
cd backend
alembic upgrade head
```

---

## How to Seed Demo Users

```bash
cd backend
python -m app.scripts.seed
```

This creates:
- Elderly user linked to a patient profile
- Caregiver user with hashed PIN
- Healthcare worker user
- Caregiver-patient link
- Healthcare-patient link
- Initial question bank (8 questions, 4 categories)

---

## Demo Credentials

| Role | Email | Password |
|---|---|---|
| Elderly | `elderly@tiara.app` | `password123` |
| Caregiver | `caregiver@tiara.app` | `password123` |
| Healthcare Worker | `doctor@tiara.app` | `password123` |

**Caregiver Dashboard PIN**: `123456`

---

## How the AI Pipeline Works

After a check-in session is completed:

1. **TranscriptionService** — Converts audio to text using `faster-whisper` (or fallback)
2. **VoiceAnalysisService** — Extracts speech rate, hesitations, pauses, repetitions using `librosa`
3. **LanguageAnalysisService** — Scores orientation, memory recall, coherence, vocabulary (rule-based)
4. **FacialAnalysisService** — Basic face detection and video duration using `OpenCV`
5. **RiskScoringService** — Computes composite risk score (0-100) with weighted components
6. **AlertService** — Generates caregiver alerts based on thresholds and trends
7. **RecommendationService** — Creates care recommendations based on risk level and indicators

All services use **provider abstraction** — real implementations when libraries are available, graceful non-fake fallbacks when not.

### Adding a Real AI Model

To plug in a custom cognitive decline model:

```python
# backend/app/services/risk_scoring_service.py
class CustomModelProvider(BaseRiskScoringProvider):
    def score(self, inputs: RiskScoringInput) -> RiskScore:
        # Your custom model logic here
        ...
```

Set `RISK_SCORING_PROVIDER=custom` in `.env`.

### Setting Up Whisper

```bash
pip install faster-whisper

# In .env:
WHISPER_MODEL_SIZE=base  # Options: tiny, base, small, medium, large
```

### Configuring Guidance AI (LLM)

```bash
# In .env:
LLM_PROVIDER=openai  # or: anthropic, gemini, none (uses rule-based fallback)
LLM_API_KEY=your-api-key-here
```

---

## Safety Disclaimer

> TIARA is a cognitive trend monitoring and caregiver support platform. It is **not** a medical diagnosis tool. All risk indicators are informational only. Outputs should not replace professional clinical assessment. TIARA encourages timely clinical consultation when patterns warrant it.

---

## Known Limitations

- Whisper transcription requires a non-trivial model download (base model: ~150MB)
- Facial analysis quality depends on lighting and camera angle
- Language analysis uses rule-based heuristics in MVP — LLM integration improves accuracy
- PDF generation requires WeasyPrint and its system dependencies
- No real-time alert push notifications (polling or WebSocket upgrade needed)
- Single caregiver per patient in MVP (multi-caregiver post-MVP)

---

## Future Improvements

- Custom trained cognitive decline ML model
- RAG with validated medical knowledge base (DSM-5, NICE guidelines)
- Push notifications (mobile app or PWA)
- WhatsApp/email caregiver alerts
- FHIR-compliant healthcare portal
- Multi-patient caregiver management
- Offline PWA mode
- Automated model training pipeline
- Media encryption at rest
- GDPR-compliant data deletion workflow
- Longitudinal baseline calibration per patient

---

## Documentation

Full documentation in `/docs`:

| File | Content |
|---|---|
| `01-product-requirements.md` | What TIARA is, goals, safety positioning |
| `02-mvp-scope.md` | MVP features and success criteria |
| `03-system-architecture.md` | Tech stack and architecture diagrams |
| `04-database-design.md` | All tables, columns, and relationships |
| `05-api-specification.md` | All endpoints with request/response examples |
| `06-ai-pipeline.md` | Full AI pipeline design and code patterns |
| `07-security-and-privacy.md` | Auth, RBAC, PIN, consent, media privacy |
| `08-development-roadmap.md` | 10-phase implementation plan |
| `09-demo-script.md` | Step-by-step competition demo script |

---

## API Documentation

When backend is running: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)

---

<br>
<div align="left">
  <h2>Meet the Team</h2>
  <p>The people behind Tiara</p>
</div>

<a href="#"><img width="144px" height="180px" src="https://drive.google.com/uc?export=view&id=17JzgCaF45gCTXnlIglXVKpq05sTQq5Vx" alt=""/></a> | <a href="#"><img width="144px" height="180px" src="https://drive.google.com/uc?export=view&id=1eOFVxZgBGwHtyDeV7OwQkiE4X2GUxEJE" alt=""/></a> | <a href="#"><img width="144px" height="180px" src="https://drive.google.com/uc?export=view&id=1kbe9CbYZBaLMgQ-PSwiz179-lZVjKZ9v" alt=""/></a> | <a href="#"><img width="144px" height="180px" src="https://drive.google.com/uc?export=view&id=17fSXYU6hc4AbKMvgcrPub7wiV55OcjNr" alt=""/></a> |
| --- | --- | --- | --- |
| <div align="left"><h3><b>Muhammad Aris Maulana</b></h3></div> | <div align="left"><h3><b>Nazla Azzahra Hermana</b></h3></div> | <div align="left"><h3><b>Ladya Kalascha</b></h3></div> | <div align="left"><h3><b>Muhammad Azka Subhan</b></h3></div> |

