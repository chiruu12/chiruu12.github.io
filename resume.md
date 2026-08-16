# Chirag Gupta

chirag.gupta.290403@gmail.com | +91 7827721664
https://linkedin.com/in/chiruu12 | https://github.com/chiruu12 | https://chiruu12.github.io

## Profile

AI engineer building multi-agent systems and the infrastructure that makes them measurable: cost accounting, evaluation, and runtime security for LLM agents.

## Experience

### AI Engineer, GoManzanas (US Startup)
May 2025 - Present | Remote

AEGIS, Multi-Agent Pipeline: Detected pirated CAD software usage by analyzing telemetry and signal patterns.
- Staged multi-agent pipeline over multi-backend LLM orchestration (fallback routing, stage-specific prompting): 89% precision against a 94% manual baseline at $0.05/case, down from $1.06

Ace1t, Real-Time Voice AI: Built voice-AI backend for a real-time accent training platform.
- Built the streaming push-to-talk pipeline end to end: multiple TTS models behind Whisper and FastConformer ASR, model-driven speech control, silence handling

Booster, AI Collaboration Platform: Built multi-agent infrastructure for an ideation platform (FastAPI + React + PostgreSQL).
- Built multi-agent group chat with turn-based orchestration and real-time collaboration across agent personas
- Designed containerized code execution environment and agent session lifecycle with idle cleanup and queue-based concurrency
- Built custom MCP server, skills system with model tiering, and agent benchmarking framework

### GSoC '25 Contributor | '26 Mentor, Jenkins
May 2025 - Present
https://github.com/jenkinsci/domain-llm

- Built modular multi-agent diagnostic system (log-parser, classifier, recommender) for Jenkins build failures, across OpenAI, Gemini, and Claude backends
- Added vector-store RAG layer, benchmarked on 20 curated questions: 95% context relevance, 3.75/5.0 overall score

### AI Engineer, Reasonify Technology Pvt Ltd

- Built multi-agent LLM pipelines for adaptive learning content and automated study-plan generation
- Built automated Manim video generation pipeline (CLI + prompt standardization + component library), cutting production time from 5h to 20min
- Implemented hybrid semantic filtering for TTS using regex rules and a fine-tuned Gemma 270M model

### Open Source Contributions

- Merged upstream fixes: keephq/keep, datalayer/jupyter-mcp-server (stale-tool fallback and concurrent-miss coalescing), topoteretes/cognee, HKUDS/DeepTutor
- Rago (OSL Incubator): Added 5 API backends (Cohere, Fireworks, Together, Groq, HuggingFace) for embeddings and generation. 7 merged PRs.
- Keras: np.diff and np.log2 via the OpenVINO backend. Agno: Exa Answer method, deprecated-model migration across 7+ providers, Crawl4ai URL expansion.

### AI & Data Science Intern
Mindcraft Labs | EvoAstra Ventures, May 2024 - Jan 2025

- Mindcraft Labs: automated 19+ workflows (RETELL, Voiceflow, Make). EvoAstra: fraud-detection model on 6.3M+ records at 94% recall

## Projects

Unplug: Open-source runtime security layer for AI agents. 3-stage detection pipeline (regex engine, ML classifier, LLM judge) with taint tracking across tool calls and span-level redaction. Ships as a Python SDK (pip install "unplug-ai[ml]"), hosted API, and MCP server.
- Trained and shipped unplug-tiny-v1, a dual-head prompt-injection span detector (DeBERTa-v3-xsmall, 70M params) on HuggingFace under Apache-2.0. A document head classifies; a BIOES token head localizes the attack, so the pipeline redacts the malicious span instead of discarding the whole document.
- Measured on a frozen held-out eval harness: 94.4% recall at 0.5% FPR on core injection, 96.3% recall at 0.0% FPR on indirect injection in context, 97.1% span F1. Failure axes documented openly (61.9% recall on OOD direct injection; over-fires on harmful-but-not-injection text, since it detects hijacking, not harm).
- Runs on CPU via ONNX, no GPU. 12-stage text normalizer defeats evasion (leetspeak, homoglyphs, base64, zero-width, reversed, cross-language).
https://unplug-ai.org
https://github.com/UnplugAI/Unplug
https://huggingface.co/Unplug-AI/unplug-tiny-v1

Jailbreak Dojo: Browser game where players social-engineer a local LLM guardian into leaking a secret, past Unplug's defenses across 5 escalating levels (regex, hardened prompt, output redaction, ML classifier). Doubles as a red-team data flywheel: every bypass becomes labeled training data for the next Unplug model. Built for the Build Small Hackathon; live on a HuggingFace Space.
https://build-small-hackathon-whisperkey.hf.space

Hive: Local-first agent OS. Persistent agents from YAML, multi-model routing (Claude, Codex, LM Studio), agent rooms for collaboration.
https://github.com/chiruu12/Hive

Marshal: Orchestration engine that runs a fleet of headless coding agents (Claude Code, Codex, Cursor, OpenCode) in parallel, each in an isolated git worktree, with a per-provider cost ledger. Ships as a CLI, an MCP server, and a Claude Code plugin; on PyPI as marshal-agents.
- One task benchmarked across four backends, measured from the ledger: the cheapest correct run cost 1/115th of the most expensive.
https://github.com/chiruu12/marshal
https://pypi.org/project/marshal-agents/

## Education

M.Sc. (Hons.) Mathematics & B.E. (Hons.) Electronics & Instrumentation
BITS Pilani, Goa Campus, Goa, India | 2021 - 2026

## Skills

Languages: Python, C/C++, SQL
ML/AI: PyTorch, Hugging Face Transformers, ONNX Runtime, vLLM, LangChain, MLflow
Infrastructure: Docker, Git, FastAPI, Pydantic, PostgreSQL, MCP, gRPC

## Achievements

- Top 20, Meta Hacker Cup Open AI practice round (13,000+ entrants)
- Winner, Smart India Hackathon (SIH) 2025
- 4th place, ContextCon, YC Startup School hackathon
