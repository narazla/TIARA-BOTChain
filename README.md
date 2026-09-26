# TIARA - BOT Chain Care DApp

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

TIARA (Thinking, Interaction, And Recall Assistant) is an AI-powered cognitive care platform for older adults, caregivers, and healthcare workers.

The application combines daily AI-guided check-ins with caregiver workflows. It is designed to help families notice changes over time through conversation, voice, video, and language signals, while keeping the user experience supportive and non-clinical.

The project also includes a Web3 wallet connection for the BOT Chain ecosystem and publishes the deployed contract reference used by the application.

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
- **BOT Chain wallet connection:** Connects a browser wallet and switches to BOT Chain Mainnet when requested.
- **On-chain deployment reference:** Provides a public explorer link for the deployed BOT Chain contract address.

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

### Frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

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
