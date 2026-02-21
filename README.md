# EchoCast AI - AI Generated Podcast Project

Yeh ek advanced **AI Podcast Generator** h jo user ke topic se automatically **Podcast Script** generate karta h aur use **Natural Human Voice (Audio)** me convert karta h.

## 🚀 Key Features

- **LLM Script Generation**: Google Gemini API use karke professional podcast script banata h.
- **Natural TTS (Text-To-Speech)**: Microsoft Edge-TTS use karke high-quality human-like audio voices generate karta h.
- **Premium UI**: Glassmorphism aur floating animations wala stunning user interface (HTML, CSS, JS unified).
- **Activity Logging**: Har user request ka track record `logs/` folder me save hota h.
- **Separate Storage**: Scripts (`.txt`) aur Audio (`.mp3`) alag-alag folders me securely store hote hain.

## 📂 Project Structure Explained (Hinglish)

1. **`main.py`**:
   - **Kyu?**: Yeh hmara backend server h (FastAPI based).
   - **Role**: Routing handle karta h, static files serv karta h, aur frontend ko engine se connect karta h.

2. **`podcast_engine.py`**:
   - **Kyu?**: Yeh project ka 'Brain' h.
   - **Role**: Script generation, audio conversion, aur logical logging isi ke andar hoti h.

3. **`index.html`**:
   - **Kyu?**: Yeh single-file frontend h (HTML + CSS + JS).
   - **Role**: Premium design UI provide karta h aur API call karke response display karta h.

4. **`static/`**:
   - **Kyu?**: Client side assets storage.
   - **Role**: Isme `audio/` aur `scripts/` folders hain jisme artifacts save hote hain.

5. **`logs/`**:
   - **Kyu?**: Admin/History tracking ke liye.
   - **Role**: `activity.log` file me timestamp ke sath user history rakhta h.

## 🛠 Tech Stack

- **Backend**: FastAPI (Python)
- **AI Model**: Google Gemini 1.5/2.5 Flash
- **Voice Engine**: edge-tts
- **Frontend**: Vanilla CSS, Modern JavaScript, HTML5

## 🔧 Installation

Check `steps.txt` for detailed setup and run guide.

---
Created by Antigravity AI
