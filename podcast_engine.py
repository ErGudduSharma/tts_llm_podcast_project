import os
import uuid
import edge_tts
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv

# Env variables load kar rahe hain (API keys fix karne ke liye)
load_dotenv()

def log_activity(prompt, script_path, audio_path):
    """
    Kyu banaya: User ki har activity ka record rakhne ke liye.
    Problem solve: Agar baad me dekhna ho ki user ne kya search kiya aur kya output mila, toh ye log file kaam aati h.
    Zaruri kyu h: Tracking aur debugging me help karta h.
    """
    log_dir = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir) # Logs folder nahi h toh bana do
    
    log_file = os.path.join(log_dir, "activity.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Log entry format
    log_entry = f"[{timestamp}]\nPrompt: {prompt}\nScript: {script_path}\nAudio: {audio_path}\n{'-'*50}\n"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry) # File me entry append kar rahe hain

# Gemini API setup
GENIMIN_API_KEY = os.getenv("GEMINI_API_KEY")
if GENIMIN_API_KEY:
    genai.configure(api_key=GENIMIN_API_KEY)

async def generate_script(prompt: str):
    """
    Kyu banaya: User ke topic ke basis par AI script generate karne ke liye.
    Problem solve: User ko khud script likhne ki zarurat nahi h, LLM (Gemini) ye kaam professional host ki tarah kar deta h.
    Zaruri kyu h: Bina script ke podcast ka content nahi ban sakta.
    """
    if not GENIMIN_API_KEY:
        raise Exception("Gemini API Key missing h! .env file check karein.")
    
    # Model configuration (User requested no changes here)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    system_prompt = "You are a professional podcast host. Create a short, engaging, and conversational podcast script based on the user's topic. Keep it under 150 words. Do not include speaker names like 'Host:', just the spoken text."
    
    # Content generation call
    response = model.generate_content(f"{system_prompt}\n\nUser Topic: {prompt}")
    script_text = response.text.strip()

    # Script ko file me save kar rahe hain separate folder me
    filename = f"{uuid.uuid4()}.txt"
    scripts_dir = os.path.join(os.getcwd(), "static", "scripts")
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
    
    filepath = os.path.join(scripts_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(script_text)

    return script_text, f"/static/scripts/{filename}"

async def generate_audio(text: str):
    """
    Kyu banaya: Generated text ko natural sounding voice (audio) me badalne ke liye.
    Problem solve: Text ko sirf padhna boring ho sakta h, Edge-TTS ise sunne layak podcast banata h.
    Zaruri kyu h: Podcast ka matlab hi 'Audio content' hota h.
    """
    filename = f"{uuid.uuid4()}.mp3"
    audio_dir = os.path.join(os.getcwd(), "static", "audio")
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
        
    filepath = os.path.join(audio_dir, filename)
    
    # AndrewNeural voice use kar rahe hain jo professional lagti h
    voice = "en-US-AndrewNeural" 
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filepath)
    
    return f"/static/audio/{filename}"
