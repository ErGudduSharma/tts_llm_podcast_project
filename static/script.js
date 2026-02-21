async function generatePodcast() {
    const prompt = document.getElementById('promptInput').value;
    if (!prompt) {
        alert("Please enter a topic first!");
        return;
    }

    const loader = document.getElementById('loader');
    const resultSection = document.getElementById('resultSection');
    const generateBtn = document.querySelector('.generate-btn');

    loader.style.display = 'block';
    resultSection.style.display = 'none';
    generateBtn.disabled = true;
    generateBtn.style.opacity = '0.5';

    try {
        const response = await fetch('/generate-podcast', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt }),
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById('scriptContent').innerText = data.script;
            const audioPlayer = document.getElementById('audioPlayer');
            audioPlayer.src = data.audio_url;
            resultSection.style.display = 'block';
            audioPlayer.play();
        } else {
            alert("Error: " + (data.detail || "Something went wrong"));
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Could not connect to the backend. Is main.py running?");
    } finally {
        loader.style.display = 'none';
        generateBtn.disabled = false;
        generateBtn.style.opacity = '1';
    }
}
