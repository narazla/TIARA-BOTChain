# TIARA — BOT Chain Care DApp

<br>
<div align="left">
  <img
    src="https://drive.google.com/uc?export=view&id=1rhJCGPOvsYHlw2Tl5m5wh-WzsWgavw_K"
    alt="TIARA DApp"
    style="width:100%; max-width:1400px;"
  />
</div>
<br>

> **Medical disclaimer:** TIARA is not a medical diagnosis tool. It provides informational cognitive trend monitoring and caregiver support only, and does not replace professional clinical assessment.

## Overview

TIARA (Thinking, Interaction, And Recall Assistant) is a decentralized AI-powered cognitive care platform that bridges empathetic caregiving with immutable on-chain record-keeping on BOT Chain Mainnet.

The application combines daily AI-guided check-ins with caregiver workflows. It is designed to help families notice changes over time through conversation, voice, video, and language signals, while keeping the user experience supportive and non-clinical.

The platform combines daily AI-guided check-ins with caregiver workflows, Web3 wallet access, and a public smart contract reference for verifiable care checkpoints. Sensitive medical content remains off-chain while cryptographic records can provide a tamper-evident audit trail.

## Core User Flows

```text
Older adult:
Login -> Home -> Daily check-in -> Video/audio capture -> Supportive result

Caregiver:
Login -> Caregiver PIN -> Dashboard -> Alerts -> Recommendations -> Guidance AI -> Reports

Healthcare worker:
Login -> Patient monitoring -> Session history -> Longitudinal trends
```

## Features

- **Daily video/audio check-in:** AI-guided questions with consent-based media capture.
- **AI analysis pipeline:** Transcription, voice feature extraction, language analysis, and risk scoring.
- **Caregiver dashboard:** Cognitive trend charts, patient summaries, alerts, and recommendations.
- **Dementia Guidance AI:** Evidence-informed caregiver guidance with a medical disclaimer.
- **Role-based access:** Separate elderly, caregiver, and healthcare worker flows.
- **Caregiver PIN protection:** An additional access step for sensitive caregiver insights.
- **Decentralized Wisdom Logs & Smart Contract:** Secures longitudinal cognitive check-ins and audit trails directly on BOT Chain Mainnet (`0x9E71519cD8C72379caD79c6A6Fc5bf5FF261b149`), enabling tamper-proof and publicly verifiable data records.
- **Web3 Wallet-Based Authentication:** Integrates MetaMask-compatible browser wallets to securely manage caregiver and family access without relying solely on centralized passwords.

## Deployment & Smart Contract

The smart contract source code (`.sol`) is located in the [`contracts/WisdomLog.sol`](contracts/WisdomLog.sol) directory. TIARA's contract is fully deployed and verified on the **BOT Chain Mainnet**:

| Network | Contract Name | Address / Explorer Link |
|---|---|---|
| **BOT Chain Mainnet** | WisdomLog.sol | `0x9E71519cD8C72379caD79c6A6Fc5bf5FF261b149` ([View on Explorer](https://scan.bohr.life/address/0x9E71519cD8C72379caD79c6A6Fc5bf5FF261b149)) |
| **Network Architecture** | Production | Direct Mainnet Deployment (Chain ID: 677) ensuring immutable On-Chain Wisdom Logs. |

TIARA operates directly on BOT Chain Mainnet to provide a reliable production environment for its immutable On-Chain Wisdom Logs.

### BOT Chain network configuration

- **Network:** BOT Chain Mainnet
- **Chain ID:** `677` (`0x2A5`)
- **RPC URL:** `https://rpc.botchain.ai`
- **Block explorer:** `https://scan.bohr.life`
- **Native currency:** BOT

### Note on Frontend Integration

TIARA operates directly on BOT Chain Mainnet (Chain ID: 677) with its smart contract fully deployed and verified. The frontend currently supports active Web3 wallet connection, network auto-switching, and live on-chain reference tracking. Full ABI write integration is designed for ongoing production scaling and will connect the caregiver workflows to callable contract methods once the generated ABI is checked into the repository.

## How to Use the Live Application

1. Open [tiaracare.my.id](https://tiaracare.my.id).
2. Click **Connect Wallet** in the public navigation or caregiver dashboard.
3. Approve the wallet connection in MetaMask or another EIP-1193-compatible browser wallet.
4. Approve the network switch or add BOT Chain Mainnet when prompted.
5. Use the application flows appropriate to your role.

The current wallet feature establishes a browser-wallet connection and network configuration. It does not expose a contract write action in the frontend until the deployed contract ABI and callable method are added to the repository.

## Demo Accounts

The seeded development environment includes these demo accounts:

| Role | Email | Password |
|---|---|---|
| Older adult | `elderly@tiara.app` | `password123` |
| Caregiver | `caregiver@tiara.app` | `password123` |
| Healthcare worker | `doctor@tiara.app` | `password123` |

**Caregiver dashboard PIN:** `123456`

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js, TypeScript, Tailwind CSS, Framer Motion, Recharts |
| Backend | FastAPI, Python, SQLAlchemy, PostgreSQL, Alembic |
| Authentication | JWT, bcrypt, caregiver PIN protection |
| AI and media | Google GenAI SDK, faster-whisper, librosa, OpenCV |
| Wallet integration | Browser EIP-1193 provider, MetaMask-compatible wallets |
| Blockchain target | BOT Chain Mainnet |

## Repository Structure

```text
TIARA_2/
├── frontend/              # Next.js application
│   ├── app/               # App Router pages and user flows
│   ├── components/        # Shared UI components, including ConnectWallet
│   └── lib/               # API client, authentication, and types
├── backend/               # FastAPI application
│   ├── app/               # Routes, models, services, and configuration
│   └── alembic/           # Database migrations
├── contracts/             # Solidity smart contracts
│   └── WisdomLog.sol      # On-chain care checkpoint registry
├── docs/                  # Product, architecture, API, AI, and security docs
├── docker-compose.yml     # PostgreSQL, backend, and frontend services
└── README.md
```

## Local Setup

### Prerequisites

- Node.js 18 or newer
- Python 3.11 or newer
- PostgreSQL 15 or newer
- Optional: Docker and Docker Compose

### Backend

```bash
cd backend
python -m venv venv

# Windows PowerShell
venv\Scripts\Activate.ps1

# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt
alembic upgrade head
python -m app.scripts.seed
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

For Render, set the service root directory to `backend` and use this start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Set these environment variables in Render:

```text
FRONTEND_URL=https://tiaracare.my.id,https://www.tiaracare.my.id
DATABASE_URL=<your-render-postgres-connection-string>
JWT_SECRET_KEY=<a-long-random-production-secret>
```

`FRONTEND_URL` accepts comma-separated origins so local development and Vercel preview URLs can be added when needed. The API CORS policy uses this value instead of allowing every origin.

### Railway alternative

Create a Railway project with a **PostgreSQL** service and a backend service connected to this repository. Configure the backend service with:

- **Root Directory:** `/backend`
- **Builder:** `Dockerfile`
- **Build Command:** leave empty; the Dockerfile installs dependencies
- **Start Command:** leave empty; the Dockerfile runs migrations and Uvicorn

Add the same `FRONTEND_URL` and `JWT_SECRET_KEY` variables listed above. Copy Railway PostgreSQL&apos;s `DATABASE_URL` into the backend service variables. The backend automatically converts Railway&apos;s standard PostgreSQL URL to the async SQLAlchemy driver required by the application.

For the Railway Free plan, leave `ENABLE_LOCAL_RAG` unset or set it to `false`; the large local embedding model is disabled by default so caregiver guidance stays responsive. Set `GEMINI_API_KEY` to enable AI-generated answers. Set `ENABLE_LOCAL_RAG=true` only on a host with enough memory for the embedding model.

### Frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

For the deployed frontend, configure `NEXT_PUBLIC_BACKEND_URL` in Vercel with the Render service URL, for example `https://tiara-backend.onrender.com`.

The frontend runs at `http://localhost:3000` and the backend API runs at `http://localhost:8000`. The API documentation is available at `http://localhost:8000/docs` when the backend is running.

### Docker Compose

From the repository root:

```bash
docker compose up --build
```

Configure database credentials, JWT settings, and the backend URL through the environment variables documented in the project configuration before using Docker in production.

## AI Pipeline

After a check-in is submitted, TIARA processes the session through these stages:

1. Transcription from recorded audio.
2. Voice feature extraction, including speech rate and hesitation signals.
3. Language analysis for orientation, memory recall, coherence, and vocabulary.
4. Basic facial and video analysis when media is available.
5. Composite cognitive trend scoring.
6. Caregiver alerts and recommendations based on observed patterns.

All results are informational indicators. They are not diagnoses.

## Security and Privacy

- Authentication uses JWT access tokens.
- Caregiver dashboard access requires a separate PIN.
- Camera and microphone flows require user consent.
- The system should be deployed with strong secrets and protected database credentials.
- Do not commit `.env` files, API keys, private keys, or wallet seed phrases.

## Documentation

Additional project documentation is available in [`docs/`](docs/), including:

- [Product requirements](docs/01-product-requirements.md)
- [MVP scope](docs/02-mvp-scope.md)
- [System architecture](docs/03-system-architecture.md)
- [Database design](docs/04-database-design.md)
- [API specification](docs/05-api-specification.md)
- [AI pipeline](docs/06-ai-pipeline.md)
- [Security and privacy](docs/07-security-and-privacy.md)
- [Development roadmap](docs/08-development-roadmap.md)
- [Demo script](docs/09-demo-script.md)

## Known Limitations

- The repository includes the `WisdomLog.sol` source, but the generated contract ABI is not checked in.
- The frontend wallet connection does not yet submit a contract write transaction.
- The project intentionally uses a production-only Mainnet deployment for the On-Chain Wisdom Log.
- AI model quality depends on available models, media quality, and runtime configuration.
- TIARA must not be used as a substitute for professional medical evaluation.

## Team

TIARA is built by the project team for the BOT Chain hackathon.
