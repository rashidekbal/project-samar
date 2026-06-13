<p align="center">
  <h1 align="center">🧠 Project Samar</h1>
  <p align="center">
    <strong>Autonomous AI with Human-Like Self-Experience & Learning</strong>
  </p>
  <p align="center">
    <em>Building an AI that doesn't just respond — it experiences, learns, and evolves.</em>
  </p>
  <p align="center">
    <a href="#-vision">Vision</a> •
    <a href="#-current-status">Status</a> •
    <a href="#%EF%B8%8F-architecture">Architecture</a> •
    <a href="#-getting-started">Setup</a> •
    <a href="#-roadmap">Roadmap</a> •
    <a href="#-license">License</a>
  </p>
</p>

---

> ⚠️ **This project is under active development.** Features described below represent both current implementations and planned milestones. Expect breaking changes.

---

## 🌟 Vision

**Project Samar** is an ambitious initiative by **RTechnologies** to create a fully autonomous AI agent capable of **human-like self-experience and continuous learning**. Unlike traditional chatbots that merely process and respond, Samar is designed to:

- **Experience** — Autonomously interact with social platforms, forming its own understanding of content, users, and conversations
- **Learn** — Build persistent memory and evolve behavior based on accumulated experiences
- **Express** — Communicate through natural voice and expressive avatar animations *(planned)*
- **Integrate** — Operate seamlessly across all RTechnologies applications as a unified AI persona

The ultimate goal is to create an AI entity that is **indistinguishable from a real human user** — at least in simulation — with its own personality, preferences, social awareness, and adaptive behavior.

---

## 📊 Current Status

| Component | Status |
|---|---|
| Core Agent (LangGraph Workflow) | ✅ Implemented |
| DeepSeek LLM Integration | ✅ Implemented |
| Conversation Management (Chat API) | ✅ Implemented |
| Persistent Memory (SQLite Checkpointer) | ✅ Implemented |
| Threadly Social Platform Tools | ✅ Implemented |
| Autonomous Self-Experience Engine | 🔧 In Development |
| Continuous Learning & Adaptation | 🔧 In Development |
| Voice Synthesis & Processing | 📋 Planned |
| Expressive Avatar (Face/Body) | 📋 Planned |
| Cross-App Integration (RTechnologies) | 📋 Planned |

---

## ⚙️ Architecture

Project Samar is built on a **LangGraph-powered agentic workflow** with a modular tool system that allows the AI to autonomously interact with external platforms.

### High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        FastAPI Server                            │
│                     (main.py — Entry Point)                      │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────┐    ┌────────────┐    ┌───────────┐    ┌──────────┐ │
│  │ Routes  │───▶│ Controller │───▶│ Services  │───▶│  Agent   │ │
│  └─────────┘    └────────────┘    └───────────┘    └────┬─────┘ │
│                                                         │       │
│                                    ┌────────────────────┘       │
│                                    ▼                            │
│                          ┌──────────────────┐                   │
│                          │  LangGraph       │                   │
│                          │  State Machine   │                   │
│                          │                  │                   │
│                          │  START ──▶ Model │                   │
│                          │    ▲       │   │ │                   │
│                          │    │       ▼   ▼ │                   │
│                          │  Tools ◀── ?  END│                   │
│                          └──────────────────┘                   │
│                                    │                            │
│                    ┌───────────────┼───────────────┐            │
│                    ▼               ▼               ▼            │
│              ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│              │   Auth   │   │  Social  │   │ Content  │        │
│              │   Tool   │   │  Tools   │   │  Tools   │        │
│              └──────────┘   └──────────┘   └──────────┘        │
│              ┌──────────┐   ┌──────────┐                       │
│              │ Profile  │   │  Search  │                       │
│              │  Tools   │   │   Tool   │                       │
│              └──────────┘   └──────────┘                       │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              SQLite Checkpointer (Persistent Memory)     │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

### Tech Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | FastAPI (Python) |
| **AI Orchestration** | LangGraph (StateGraph with conditional tool routing) |
| **LLM Provider** | DeepSeek (`deepseek-chat` via `langchain-deepseek`) |
| **State Persistence** | SQLite (async checkpointing via `langgraph-checkpoint-sqlite`) |
| **LLM Framework** | LangChain Core |
| **API Communication** | HTTPX / Requests (for Threadly platform interaction) |

### Project Structure

```
project-samar/
├── main.py                          # FastAPI app entry point & lifespan
├── requirements.txt                 # Python dependencies
├── checkpoints.db                   # SQLite persistent memory store
├── .env                             # Environment variables (secrets)
├── .env.sample                      # Environment template
├── LICENSE                          # GNU GPL v3
│
└── src/
    ├── agent/                       # 🧠 Core AI Agent
    │   ├── agent.py                 #    DeepSeek model initialization & tool binding
    │   ├── workflow.py              #    LangGraph state machine compilation
    │   ├── state.py                 #    Chat state type definition
    │   ├── nodes.py                 #    Graph nodes (chat node with system prompt)
    │   └── structured_models/       #    Structured output models (title generation)
    │
    ├── tool/                        # 🔧 Autonomous Action Tools
    │   ├── all_tools.py             #    Tool registry (aggregates all tools)
    │   ├── auth/                    #    Authentication (login to Threadly)
    │   ├── social/                  #    Social interactions (follow/unfollow/requests)
    │   ├── profile/                 #    Profile management (self/user/suggestions)
    │   ├── search/                  #    User & content search
    │   ├── content/                 #    Posts & stories (feed, create, interact)
    │   ├── engagement/              #    Likes, comments, shares
    │   └── message/                 #    Direct messaging
    │
    ├── routes/                      # 🛤️  API route definitions
    │   └── chatRoute.py             #    Chat endpoints (/newConversation, /newMessage, /history)
    │
    ├── controller/                  # 🎮 Request handlers
    │   └── chat_controller.py       #    Chat request validation & response formatting
    │
    ├── services/                    # ⚡ Business logic
    │   └── chat.py                  #    Conversation creation, messaging, history retrieval
    │
    ├── model/                       # 📦 Pydantic data models
    │   ├── chat_request_model.py
    │   ├── chat_response_model.py
    │   ├── new_conversation_request_model.py
    │   └── new_conversation_response_model.py
    │
    ├── constants/                   # 🔗 API endpoint definitions
    │   └── threadly_endpoints.py    #    All Threadly platform API URLs
    │
    ├── middleware/                   # 🛡️  Request middleware (planned)
    ├── database/                    # 💾 Database layer (planned)
    └── utils/                       # 🧰 Utilities
        └── uuid_generator.py        #    UUID generation for conversations
```

---

## 🔧 Tool Capabilities

Samar is equipped with a comprehensive set of tools to autonomously operate on the **Threadly** social platform:

### 🔐 Authentication
- Login and session management via user credentials

### 👥 Social Interactions
- Follow / Unfollow users
- Send, accept, reject, and cancel follow requests
- View followers and followings list
- Retrieve all pending follow requests

### 👤 Profile Management
- View own profile details
- Look up other users' profiles
- Get suggested users to follow

### 🔍 Search
- Search for users and content across the platform

### 📸 Content Interaction
- Browse image and video (reels) feeds
- View individual posts and stories
- Access user-specific posts and stories
- View liked-by and shared-by lists

### 💬 Engagement
- Like/unlike posts, stories, and comments
- Add comments and replies to posts
- View comment threads

### ✉️ Messaging
- Send direct messages
- Check and retrieve pending messages
- View all chat conversations
- Message delivery status tracking
- Delete/unsend messages

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **pip** (Python package manager)
- A **DeepSeek API key**
- Access to a running **Threadly** backend instance

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rashidekbal/project-samar.git
   cd project-samar
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   BASE_URL=your_threadly_backend_url_here
   ```

5. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/api/v1/chat/newConversation` | Start a new conversation |
| `POST` | `/api/v1/chat/newMessage` | Send a message in an existing conversation |
| `GET` | `/api/v1/chat/history/{thread_id}` | Retrieve conversation history |

### Interactive API Docs

Once running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## 🗺️ Roadmap

### Phase 1 — Foundation ✅
- [x] LangGraph agentic workflow with tool routing
- [x] DeepSeek LLM integration
- [x] Threadly platform tool suite (auth, social, content, messaging)
- [x] Persistent conversation memory via SQLite checkpointing
- [x] REST API for external chat interaction
- [x] Auto-generated conversation titles

### Phase 2 — Autonomous Self-Experience 🔧 *(In Progress)*
- [ ] Self-initiated browsing and content exploration
- [ ] Autonomous social interactions (following, liking, commenting)
- [ ] Experience journaling — internal narrative of daily activities
- [ ] Emotional state modeling based on interactions
- [ ] Preference learning from content engagement patterns

### Phase 3 — Learning & Memory Evolution
- [ ] Long-term memory architecture (beyond conversation checkpoints)
- [ ] Behavioral adaptation based on accumulated experiences
- [ ] Relationship modeling — tracking social connections and sentiment
- [ ] Self-reflection and goal-setting capabilities
- [ ] Knowledge graph construction from experiences

### Phase 4 — Voice & Expression Avatar
- [ ] Voice synthesis with emotional tone modulation
- [ ] Speech-to-text for voice-based interaction
- [ ] Expressive 2D/3D avatar with facial animations
- [ ] Lip-sync with voice output
- [ ] Body language and gesture generation

### Phase 5 — RTechnologies Integration
- [ ] Unified Samar identity across all RTechnologies apps
- [ ] Cross-platform context sharing
- [ ] App-specific tool extensions (per RTechnologies product)
- [ ] Centralized personality and memory management
- [ ] User-facing Samar companion in consumer apps

---

## 🤝 Contributing

This project is currently in **early development** and maintained by the RTechnologies team. Contribution guidelines will be published as the project matures.

If you're interested in contributing, feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**RTechnologies**

- **GitHub**: [@rashidekbal](https://github.com/rashidekbal)

---

<p align="center">
  <sub>Built with ❤️ by RTechnologies — Making AI more human, one experience at a time.</sub>
</p>
