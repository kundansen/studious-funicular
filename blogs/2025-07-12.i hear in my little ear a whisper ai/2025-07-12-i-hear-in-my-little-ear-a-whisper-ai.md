# I Hear in My Little Ear - a Whisper.AI

*July 12, 2025*

**Turn any MP3 into text in minutes on your laptop.**

Whisper, OpenAI's open-source speech-to-text engine, landed back in September 2022 and has quietly become a fan-favorite for journalists, students, and anyone tired of typing out audio by hand. If you've meant to try it but never got to the setup, this guide is the nudge you needed. In five minutes, you'll have Whisper running locally on Windows or macOS, and your audio will start pouring into a text file.

It's well worth the minuscule effort to be able to run this yourself without any subscriptions and any third-party services. Use your phone to record audio—at your next lecture, conference, public event (do check for privacy rules)—and then drop the MP3 into this process.

---

## 1. One-time setup (≈ 5 min)

### Windows 10/11

**Step 1: Install Python 3.**

Download from [https://python.org](https://python.org) and tick **"Add Python to PATH."**

**Step 2: Open an elevated terminal.** Press Win + X → Terminal (Admin) and run:

```
winget install Git.Git ffmpeg
```

**Step 3. Check everything.** Each of the below should print a version number.

```
python --version
git --version
ffmpeg -version
```

### macOS (Intel or Apple Silicon)

**Step 1: Install Homebrew**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Step 2: Grab the tools**

```
brew install python git ffmpeg
```

**Step 3: Verify** (same three commands as above for Windows).

---

## 2. Install Whisper (one command)

```
pip install -U openai-whisper      # use pip3 if pip points to Python 2
```

---

## 3. Transcribe an MP3

1. Drop speech.mp3 into any folder. Need a sample? Download a famous speech from [Top 100 Speeches of the 20th Century by Rank - American Rhetoric](https://www.americanrhetoric.com/top100speechesall.html)
2. Open Terminal / Command Prompt **in that folder**.
3. Run:

```
python -m whisper speech.mp3 --model small --language en
```

You'll get speech.txt (full transcript) and a .vtt caption file.

---

### Pro tips

- **Need accuracy?** Swap "--model small" for medium or large (needs more RAM/GPU).
- **Multiple languages?** Drop the "--language" flag. Whisper auto-detects, but will need some time to sample.
- **Batch jobs?** In the same folder: "whisper *.mp3".
- **Have an NVIDIA GPU?** Download the latest **CUDA Toolkit + driver** for your OS from [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads), then install CUDA-enabled PyTorch to allow Whisper to auto-detect the GPU and run up to 10× faster:

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

Five minutes of prep, one command, and your audio is printable, searchable, and ready for dropping into your favorite LLM for summarizing. Free your voice recordings!
