# 🧠 MeetMind – AI Video Assistant

MeetMind is an AI-powered video assistant that converts long YouTube videos and audio files into meaningful, structured, and easy-to-understand information.

Instead of spending hours watching lengthy videos, MeetMind helps you quickly understand the important content through AI-generated summaries, action items, key decisions, and interactive question answering.

Built using **Python, Streamlit, OpenAI Whisper, Groq, LangChain, and ChromaDB**.

## ✨ Features

- 🎥 **YouTube Video Processing:** Extract audio from YouTube videos.
- 🎵 **Audio File Support:** Process uploaded audio files.
- 🗣️ **Speech-to-Text:** Transcribe audio using locally running OpenAI Whisper.
- 🌐 **Multilingual Support:** Supports English transcription through Whisper and Hinglish transcription through Sarvam API.
- 📝 **AI Summarization:** Generate concise and meaningful video summaries.
- 📌 **Action Item Extraction:** Identify important tasks and action points.
- 🎯 **Key Decision Extraction:** Extract important decisions discussed in the video.
- ❓ **Open Questions:** Identify unanswered questions from the content.
- 💬 **Interactive Q&A:** Ask questions about the video using Retrieval-Augmented Generation (RAG).
- 🔍 **Semantic Search:** Retrieve relevant information using ChromaDB vector storage.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Interactive web interface |
| OpenAI Whisper | Audio transcription |
| Sarvam AI | Hinglish transcription |
| Groq API | LLM inference |
| LangChain | LLM application framework |
| ChromaDB | Vector database |
| HuggingFace Embeddings | Text embeddings |
| yt-dlp | YouTube audio extraction |
| FFmpeg | Audio conversion and processing |

## ⚙️ How It Works

1. User provides a YouTube URL or uploads an audio file.
2. MeetMind extracts and processes the audio.
3. Audio is divided into manageable chunks.
4. Whisper or Sarvam converts speech into text.
5. Groq processes the transcript to generate structured insights.
6. The transcript is converted into embeddings and stored in ChromaDB.
7. Users can ask questions and receive context-aware answers through RAG.

## 🏗️ Project Structure

```text
MeetMind/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── core/
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── extractor.py
│   ├── rag_engine.py
│   └── vector_store.py
│
├── utils/
│   ├── audio_processor.py
│   └── ...
│
└── downloads/
```

*Note: The structure above is illustrative. Adjust it to match your actual project files.*


## 🧠 Understanding RAG in MeetMind

MeetMind uses Retrieval-Augmented Generation (RAG) to answer questions based on the processed video content.

**RAG workflow:**

1. Split the transcript into smaller text chunks.
2. Generate embeddings using HuggingFace.
3. Store embeddings in ChromaDB.
4. Retrieve relevant chunks based on the user's question.
5. Pass retrieved context to the LLM.
6. Generate an answer grounded in the video transcript.

## 🌐 Deployment

MeetMind can be deployed using Streamlit Community Cloud.

1. Push your project to GitHub.
2. Visit https://share.streamlit.io/
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Configure API keys in Streamlit Secrets.
6. Deploy your application.

**Deployment note:** Local Whisper inference requires sufficient CPU, memory, and model storage. Cloud deployment may require additional optimization.

## 🔮 Future Improvements

- [ ] Support more video platforms.
- [ ] Improve transcription speed.
- [ ] Optimize LLM API usage.
- [ ] Add transcript download functionality.
- [ ] Add user authentication and saved video history.
- [ ] Improve RAG retrieval accuracy.
- [ ] Support additional languages.

## 👨‍💻 Author

Developed as a Generative AI project to make learning from long-form video content faster and more productive.

## 📄 License

This project is intended for educational and learning purposes. Add a suitable open-source license if you want others to reuse and distribute your code.
