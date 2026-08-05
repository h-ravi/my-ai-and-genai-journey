# AI & GenAI Engineering Journey

Hi, I'm documenting my journey toward becoming an AI/GenAI Engineer — one day at a time, with hands-on practice and real projects instead of just theory.

This repo has two parts:
1. **Phase 0 — Python Foundation Review** (current phase, folder-wise Day 1, Day 2...)
2. **The Roadmap** — a structured 6-month, 29-week path I'll follow after the foundation is solid

---

## Phase 0 — Python Foundation Review

Before starting the roadmap, I'm reviewing core Python through daily practice and mini-projects. Progress is tracked day-wise inside this repo.

- [x] Variables, Data Types, Operators
- [x] Conditional Statements (if-elif-else)
- [x] While Loop — ATM Machine, Bank Management System
- [x] For Loop — range, enumerate, zip, nested loops
- [x] Collections — List, Tuple, Set, Dict + Comprehensions
- [x] Functions — parameters, return values
- [x] Exception Handling — try/except/else/finally
- [x] 10 Core Python Practice Projects (Library, Expense Tracker, Contact Book, Quiz, Bank System, Student Analyzer, Inventory, Ticket Booking, Payroll, To-Do)
- [x] File Handling

*(This checklist updates as I go — each item links to its Day folder once complete.)*

---

## The Roadmap

A 6-month, 29-week structured path from backend fundamentals to a job-ready GenAI portfolio.

---

### Month 1 — Python Production Engineering
*Notebook se bahar niklo — async, APIs, Docker, CI/CD (4 Weeks)*

**Week 1 — Git + Python OOP + Project Structure**
- [x] Git & GitHub — init, add, commit, push, pull, branches, .gitignore
- [x] Python OOP — classes, objects, `__init__`, instance methods
- [ ] Inheritance, Encapsulation
- [ ] Modular code — one function/class per task
- [ ] Project structure — `src/`, `tests/`, `docs/`
- [ ] python-dotenv (.env for secrets)
- [ ] Virtual environments + requirements.txt

**Week 2 — Async Python**
- [ ] Synchronous vs Asynchronous — the core difference
- [ ] `async def`, `await`
- [ ] `asyncio.run()`, `asyncio.gather()`
- [ ] Why async matters for GenAI — concurrent LLM calls, streaming
- [ ] `aiohttp` for async HTTP requests

**Week 3 — FastAPI + Pydantic + Auth**
- [ ] FastAPI basics — GET/POST/PUT/DELETE, path/query params, request body
- [ ] Async routes, streaming responses
- [ ] Uvicorn + Swagger UI
- [ ] Pydantic — BaseModel, type hints, validation
- [ ] Using Pydantic to validate LLM JSON output
- [ ] JWT Authentication — tokens, Bearer auth, protected routes
- [ ] API keys for third-party access

**Week 4 — Docker + CI/CD + Logging**
- [ ] Dockerfile, docker build/run, port mapping
- [ ] docker-compose (FastAPI + DB together)
- [ ] GitHub Actions — workflow files, secrets, test badges
- [ ] pytest — test functions, fixtures, mocking, integration tests, coverage
- [ ] Python `logging` module — log levels
- [ ] Custom exceptions, production error handling
- [ ] **Project:** Async FastAPI app with JWT auth, background async task, Dockerized, GitHub Actions auto-test

---

### Month 2 — ML Basics + Database Foundations
*Minimum viable ML + PostgreSQL + Redis + MLflow (5 Weeks)*

**Week 1 — Minimum Viable Math + NumPy + Pandas**
- [ ] Vectors, dot product, cosine similarity intuition
- [ ] Normal distribution, basic probability
- [ ] NumPy — `np.dot()`, `np.mean()`, `np.std()`, array ops
- [ ] Pandas — DataFrame, `head()`, `info()`, `describe()`
- [ ] Missing values — `fillna()`, `dropna()`
- [ ] Boolean filtering, `groupby` + `agg`

**Week 2 — PostgreSQL + SQLAlchemy**
- [ ] Relational DB basics — tables, rows, columns
- [ ] PostgreSQL install + psql CLI
- [ ] CREATE, INSERT, SELECT, UPDATE, DELETE
- [ ] JOINs (LEFT, INNER), Indexes
- [ ] Transactions — ACID concept
- [ ] SQLAlchemy ORM — Engine, Session, Models, CRUD
- [ ] FastAPI + SQLAlchemy integration
- [ ] Alembic migrations
- [ ] Connection pooling

**Week 3 — Redis: Caching + Queues**
- [ ] Redis fundamentals — in-memory key-value store
- [ ] Redis vs PostgreSQL — when to use which
- [ ] SET, GET, EXPIRE, Lists, Hashes, Sets
- [ ] redis-py client
- [ ] Cache-aside pattern, TTL
- [ ] Semantic caching for LLM queries
- [ ] Session storage
- [ ] Task queues — Celery + Redis basics

**Week 4 — ML Algorithms (Intuition First)**
- [ ] Linear Regression — MSE/RMSE/R²
- [ ] Logistic Regression — sigmoid, binary classification
- [ ] Random Forest, XGBoost
- [ ] Confusion Matrix, Precision, Recall, F1, ROC-AUC
- [ ] When to use ML vs LLM API (tabular vs text)

**Week 5 — ML Pipeline + Deployment + Experiment Tracking**
- [ ] Scikit-learn — train_test_split, StandardScaler, cross-validation
- [ ] Pipeline objects, GridSearchCV
- [ ] Model save/load with joblib
- [ ] MLflow — experiment tracking, model registry
- [ ] FastAPI async `/predict` endpoint
- [ ] Save predictions to PostgreSQL, cache with Redis
- [ ] **Project:** Fraud Detection System — XGBoost + MLflow + FastAPI + PostgreSQL + Redis + Docker

---

### Month 3 — Deep Learning Foundations + LLMs + Frontend
*Transformer ki samajh se LLM APIs aur demo-ready UI tak (5 Weeks)*

**Week 1 — Deep Learning + Transformer Foundations**
- [ ] Neural network intuition — perceptron, weights, bias, activation
- [ ] Layers, forward pass
- [ ] Activation functions — ReLU, Sigmoid, Softmax
- [ ] Backpropagation (intuition), loss functions
- [ ] PyTorch basics — tensors, autograd, `nn.Module`
- [ ] Training loop skeleton
- [ ] Transformer architecture — attention (Query/Key/Value)
- [ ] Self-attention, multi-head attention
- [ ] Encoder vs Decoder (BERT vs GPT)
- [ ] Positional encoding

**Week 2 — LLM Fundamentals + APIs**
- [ ] Tokenization, context window limits
- [ ] Temperature, top_p, max_tokens
- [ ] tiktoken — token counting + cost
- [ ] OpenAI API, Anthropic (Claude) API
- [ ] Async API calls
- [ ] Rate limit handling — retry with backoff
- [ ] Timeout handling, fallback logic between providers
- [ ] Hugging Face Inference API

**Week 3 — Advanced Prompt Engineering**
- [ ] Zero-shot, Few-shot prompting
- [ ] Chain of Thought (CoT)
- [ ] System prompt design, negative prompting
- [ ] Structured JSON outputs + Pydantic validation
- [ ] Multi-turn conversation, context trimming
- [ ] Multimodal — vision APIs (image input, OCR use cases)

**Week 4 — Streamlit (Frontend UI)**
- [ ] Streamlit basics — chat_message, chat_input
- [ ] session_state for conversation history
- [ ] Streaming LLM output in UI
- [ ] File upload (PDF/CSV)
- [ ] Streamlit Cloud deployment
- [ ] Server-Sent Events (SSE) — FastAPI StreamingResponse

**Week 5 — LLM App Project**
- [ ] Token usage + cost tracking per request
- [ ] Redis caching for repeated queries
- [ ] Budget alerts
- [ ] **Project:** Customer Review Analyzer — sentiment/issue extraction, Streamlit chat UI, streaming, JWT-protected, Dockerized

---

### Month 4 — RAG + Vector Databases
*LLM ko private data sikhao — bina training ke (4 Weeks)*

**Week 1 — Embeddings + Vector Databases**
- [ ] Text → vector → meaning (embeddings concept)
- [ ] OpenAI text-embedding-3-small
- [ ] Vector DB vs normal DB
- [ ] ChromaDB (local), Qdrant (production), Pinecone (managed)
- [ ] Storing text + embedding + metadata

**Week 2 — RAG Pipeline + Search Types**
- [ ] Why RAG — hallucination, training cutoff, private data
- [ ] Document loading (PDF, text, web)
- [ ] Chunking — size + overlap strategies
- [ ] Embed → store → retrieve → generate flow
- [ ] Semantic search, keyword search (BM25), hybrid search
- [ ] Reranking

**Week 3 — LangChain + LlamaIndex + Real Evaluation**
- [ ] LangChain — document loaders, splitters, RetrievalQA, PromptTemplate, memory
- [ ] LlamaIndex — SimpleDirectoryReader, VectorStoreIndex, QueryEngine
- [ ] Faithfulness & answer relevancy metrics
- [ ] Ragas basic evaluation
- [ ] Building a Golden Dataset (50+ questions)
- [ ] Promptfoo, Langfuse basics

**Week 4 — Production RAG: Security + RBAC**
- [ ] Source citations, metadata filtering, confidence scores
- [ ] Async RAG pipeline
- [ ] Chat history in PostgreSQL, frequent queries in Redis
- [ ] Role-Based Access Control (JWT roles)
- [ ] Prompt injection defense, PII masking, input sanitization
- [ ] NeMo Guardrails basics
- [ ] **Project (Portfolio Main):** Enterprise Q&A System — RAG + RBAC + guardrails + async + Ragas eval score

---

### Month 5 — Agentic AI + MCP + System Design
*Autonomous workflows + standardized tool protocols + AI system architecture (6 Weeks)*

**Week 1 — Agent Fundamentals: Tool Calling**
- [ ] What is an AI agent — Plan → Action → Observe → Reflect loop
- [ ] ReAct pattern
- [ ] Tool/function calling — OpenAI & Anthropic syntax
- [ ] Returning tool results back to the LLM

**Week 2 — Custom Tools + LangChain Agents**
- [ ] Web search tool, SQL tool, RAG-as-tool, calculator/weather/news tools
- [ ] `@tool` decorator
- [ ] `create_react_agent()`, AgentExecutor
- [ ] Agent memory, max iterations, verbose debugging

**Week 3 — MCP + A2A Protocol**
- [ ] Why MCP — the "integration tax" problem
- [ ] MCP architecture — Host, Client, Server
- [ ] JSON-RPC 2.0, STDIO vs HTTP+SSE transport
- [ ] Building an MCP server (FastAPI-based)
- [ ] Connecting an MCP client, using community MCP servers
- [ ] A2A Protocol awareness (agent-to-agent communication)

**Week 4 — LangGraph: Multi-Agent Orchestration**
- [ ] Graph-based workflows — nodes and edges
- [ ] State management between agents
- [ ] Conditional edges, checkpointing
- [ ] Human-in-the-loop approval steps
- [ ] Cost control — iteration limits, model tiering, token budgets

**Week 5 — AI System Design**
- [ ] Request flow — API → queue → worker → LLM → response
- [ ] Celery + Redis queues, worker scaling
- [ ] Caching architecture — semantic, embedding, response caches
- [ ] Inference batching, load balancing, rate limiting
- [ ] Horizontal vs vertical scaling, stateless APIs
- [ ] Monitoring — CPU, memory, latency, error rate

**Week 6 — Agent Project + System Design Apply**
- [ ] Tool failure handling, hallucinated tool call detection
- [ ] Timeout logic, fallback responses
- [ ] **Project:** Multi-Agent Research Assistant (Researcher → Analyst → Writer agents, MCP tools, Celery+Redis queue, Streamlit UI, system design diagram)

---

### Month 6 — LLMOps + Production Infra + Portfolio
*Production reliability + Kubernetes + AWS + LoRA basics + job-ready portfolio (5 Weeks)*

**Week 1 — Advanced Evaluation + Observability**
- [ ] Full Ragas suite — Faithfulness, Relevancy, Precision, Recall
- [ ] DeepEval, LLM-as-a-judge
- [ ] Expanding Golden Dataset to 50+ edge cases
- [ ] LangSmith — tracing, latency, cost, dashboards, alerts

**Week 2 — Guardrails + Cost Control + LiteLLM**
- [ ] Semantic router, output parsers (Pydantic enforcement)
- [ ] Jailbreak detection, PII masking in responses
- [ ] Prompt caching, model routing (cheap vs expensive)
- [ ] Token optimization, monthly budget alerts
- [ ] LiteLLM — unified API across providers, fallback rules

**Week 3 — Kubernetes + AWS Cloud Deployment**
- [ ] Kubernetes basics — Pods, Deployments, Services
- [ ] kubectl basics, YAML manifests
- [ ] vLLM — production LLM serving, continuous batching
- [ ] Quantization intuition (int8/int4)
- [ ] GGUF + Ollama for local models
- [ ] AWS — EC2, S3, IAM, Bedrock
- [ ] Deploying Docker containers to ECS/EC2
- [ ] SSH, journalctl, tmux for production Linux
- [ ] Load testing — Locust, p50/p95/p99 latency, bottleneck analysis

**Week 4 — LoRA + PEFT (Fine-tuning Overview)**
- [ ] Why fine-tune vs RAG/prompting
- [ ] Hugging Face ecosystem — AutoTokenizer, AutoModelForCausalLM, pipeline()
- [ ] Hugging Face Hub — models/datasets
- [ ] LoRA (Low-Rank Adaptation) concept
- [ ] PEFT library, instruction tuning
- [ ] Unsloth, Axolotl
- [ ] Small-dataset LoRA fine-tune, upload to HF Hub

**Week 5 — CI/CD Evaluation + Portfolio Final**
- [ ] GitHub Actions — automated evaluation on PR
- [ ] Hallucination-rate gating, LangSmith test results
- [ ] Deployment options — HF Spaces, AWS, Render
- [ ] Portfolio — pinned repos, consistent commits, clean READMEs, live links
- [ ] Resume keywords — RAG, LangChain, LangGraph, MCP, FastAPI, Docker, Kubernetes, AWS, MLflow, LLMOps
- [ ] LeetCode — 25-30 easy Python problems
- [ ] **Final Capstone:** Full LLMOps added to M4's RAG system — CI/CD eval, LangSmith tracing, LiteLLM routing, Redis semantic caching, Guardrails, K8s/AWS deploy, system design diagram

---

## Progress Log

| Day | Phase | Topic | Project(s) |
|-----|-------|-------|------------|
| 1 | Foundation Review | Python Basics — variables, data types, operators | - |
| 2 | Foundation Review | Conditional Statements | Practice questions |
| 3 | Foundation Review | While Loop | ATM Machine, Bank Management System |

*(Updated as I go, day by day.)*

## How I'm Learning

I believe in learning by building — every topic here comes with hands-on practice and working mini-projects, not copied tutorials. Some concepts (like operators) weren't practiced as a standalone topic because they came up naturally while practicing conditionals and calculations.

## Why This Repo Is Public

Sharing this openly to stay accountable, track my own growth, and hopefully help someone on a similar path. Feel free to follow along.
