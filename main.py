import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from podcast_engine import generate_script, generate_audio, log_activity

# FastAPI application initialization
app = FastAPI()

# CORS Middleware setup: Taki frontend se backend easily communicate kar sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route: Yeh function user ko home page (index.html) show karta h
@app.get("/", response_class=HTMLResponse)
async def read_index():
    """
    Kyu banaya: Browser jab localhost:8000 hit kare toh UI render ho.
    Zaruri kyu h: Bina root route ke user ko website nahi dikhegi.
    """
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html file nahi mili!")

# Static files mounting: Taki images, audio, scripts browser me load ho sakein
static_dir = os.path.join(os.getcwd(), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Request Model: User se data lene ka format fix karta h
class PodcastRequest(BaseModel):
    prompt: str

# Main Podcast Generation Endpoint
@app.post("/generate-podcast")
async def generate_podcast_api(request: PodcastRequest):
    """
    Kyu banaya: Frontend se request handle karne ke liye (Prompt to Podcast flow).
    Problem solve: AI engine aur Web interface ko connect karta h.
    Workflow: Generate Script -> Generate Audio -> Log Activity.
    """
    try:
        # 1. Script Generation: Text content banata h
        script_text, script_file_url = await generate_script(request.prompt)
        
        # 2. Audio Generation: Text ko voice me badalta h
        audio_url = await generate_audio(script_text)

        # 3. Logging: Activity record karta h files me
        log_activity(request.prompt, script_file_url, audio_url)

        # Sab kuch sahi h toh frontend ko URL and text return karta h
        return {
            "script": script_text,
            "script_file_url": script_file_url,
            "audio_url": audio_url
        }

    except Exception as e:
        # Error handling: Taki crash hone ki wajah pta chale
        print(f"Error Occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Server start karne ka logic
    # localhost pe 8000 port use kar rahe hain
    print("Starting server on http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
