# EchoCast AI - Intelligent Podcast Generation System

EchoCast AI is a sophisticated **AI-driven podcast creation platform** that transforms user ideas into professional-grade audio experiences. By leveraging Large Language Models (LLMs) and advanced Text-to-Speech (TTS) engines, it automates the entire production flow from scriptwriting to final mastering.

## 🌟 Core Features

- **AI Scriptwriter**: Utilizes Google Gemini API to generate engaging, conversational podcast scripts based on any topic.
- **Natural Voice Synthesis**: Powered by Microsoft Edge-TTS, providing high-fidelity, human-like voice narration.
- **Unified Premium UI**: A sleek, glassmorphism-inspired web interface with dynamic background animations and reactive elements.
- **Automated Logging**: Every production cycle is logged with timestamps, prompts, and file references for tracking and debugging.
- **Organized File Management**: Dedicated storage architecture for generated scripts (`.txt`) and mastered audio (`.mp3`).

## 📂 Project Architecture

1. **`main.py`** (The Orchestrator):
   - Handles the FastAPI web server.
   - Manages routing and serves the frontend as well as static assets (audio/scripts).
   - Coordinates the flow between the user interface and the AI engine.

2. **`podcast_engine.py`** (The Core Engine):
   - Contains the primary logic for LLM script generation.
   - Manages the audio synthesis process.
   - Implements the activity logging system.

3. **`index.html`** (Integrated Frontend):
   - A single-file frontend solution containing all HTML structure, CSS styling, and JavaScript logic.
   - Features responsive design and micro-animations for an immersive user experience.

4. **`static/`** (Artifact Repository):
   - `audio/`: Stores the final generated podcast MP3 files.
   - `scripts/`: Stores the corresponding text scripts for each episode.

5. **`logs/`** (System Logs):
   - Houses `activity.log` which provides a detailed audit trail of all generated content.

## 🛠 Technology Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **AI Model (LLM)**: [Google Gemini](https://ai.google.dev/)
- **Voice Engine (TTS)**: [Edge-TTS](https://pypi.org/project/edge-tts/)
- **Frontend**: Modern Vanilla JavaScript, CSS3 (Glassmorphism), HTML5

## 🔧 Installation & Setup

For detailed step-by-step installation instructions, please refer to the `steps.txt` file.

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your API key in a `.env` file: `GEMINI_API_KEY=your_key_here`
4. Start the server: `python main.py`
5. Access the UI at `http://localhost:8000`

---
*Created with ❤️ for Advanced Generative AI Projects*
