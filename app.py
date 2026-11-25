import os
import tempfile
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="MeetMind | AI Video Assistant",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Visual theme ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root { --cream:#F5E8D0; --green:#153D32; --pink:#FF3EA5; --softpink:#F6C7D8; --ink:#18352E; }
    html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
    .stApp { background:var(--cream); color:var(--ink); }
    [data-testid="stHeader"] { background:rgba(245,232,208,.92); }
    [data-testid="stSidebar"] { background:var(--green); }
    [data-testid="stSidebar"] * { color:#FFF8ED !important; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color:#E9E2D5 !important; }
    .block-container { max-width:1240px; padding-top:2.2rem; padding-bottom:4rem; }
    h1,h2,h3 { font-family:'Manrope',sans-serif !important; color:var(--green) !important; letter-spacing:-.035em; }
    .hero { background:var(--green); border-radius:26px; padding:34px 38px; color:#FFF8ED; position:relative; overflow:hidden; margin-bottom:24px; }
    .hero:after { content:'✳'; position:absolute; right:34px; top:-35px; font-size:190px; color:rgba(246,199,216,.13); transform:rotate(18deg); }
    .hero-kicker { color:#F6C7D8; font-size:12px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
    .hero h1 { color:#FFF8ED !important; font-size:clamp(30px,4vw,48px); margin:8px 0 8px; line-height:1.08; }
    .hero p { color:#E9E2D5; font-size:15px; max-width:640px; margin:0; }
    .eyebrow { color:#A33B72; font-weight:700; text-transform:uppercase; letter-spacing:.13em; font-size:11px; }
    .panel { background:#FFF9EF; border:1px solid rgba(21,61,50,.10); border-radius:20px; padding:22px 24px; box-shadow:0 8px 28px rgba(21,61,50,.045); }
    .metric { background:#FFF9EF; border:1px solid rgba(21,61,50,.10); border-radius:18px; padding:17px 19px; }
    .metric-label { color:#66756D; font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:.08em; }
    .metric-value { color:var(--green); font-family:'Manrope'; font-size:25px; font-weight:800; margin-top:4px; }
    .stButton>button, .stDownloadButton>button { background:var(--pink); color:white; border:0; border-radius:12px; font-weight:700; padding:.62rem 1.1rem; transition:.2s; }
    .stButton>button:hover, .stDownloadButton>button:hover { background:#E52D91; color:white; border:0; transform:translateY(-1px); }
    .stTextInput input, .stTextArea textarea { background:#FFF9EF; border-radius:11px; border:1px solid #D9D5C9; }
    [data-testid="stFileUploader"] { background:#FFF9EF; border:1px dashed #B7B9A9; border-radius:14px; padding:8px; }
    .stTabs [data-baseweb="tab-list"] { gap:8px; }
    .stTabs [data-baseweb="tab"] { background:#EADFCB; border-radius:10px 10px 0 0; padding:10px 17px; }
    .stTabs [aria-selected="true"] { background:#FFF9EF !important; color:var(--green) !important; }
    .stAlert { border-radius:12px; }
    div[data-testid="stChatMessage"] { background:#FFF9EF; border:1px solid rgba(21,61,50,.08); border-radius:14px; }
    .footer-note { color:#7A8178; font-size:12px; text-align:center; margin-top:30px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helpers ----------
def save_upload(uploaded_file) -> str:
    suffix = Path(uploaded_file.name).suffix or ".mp4"
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    safe_name = Path(uploaded_file.name).name
    target = upload_dir / safe_name
    # Avoid overwriting a previous upload with the same filename.
    if target.exists():
        target = upload_dir / f"{target.stem}_{next(tempfile._get_candidate_names())}{suffix}"
    target.write_bytes(uploaded_file.getbuffer())
    return str(target.resolve())


def render_text_block(text: str, empty_message: str = "Nothing was identified for this section."):
    if text and text.strip():
        st.markdown(text)
    else:
        st.caption(empty_message)


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("<div style='font-size:12px;letter-spacing:.18em;font-weight:800;color:#F6C7D8'>✦ MEETMIND</div>", unsafe_allow_html=True)
    st.markdown("## Your video workspace")
    page = st.radio("NAVIGATION", ["Create summary", "Workspace guide"], label_visibility="visible")
    st.divider()
    st.markdown("**SUPPORTED INPUTS**")
    st.caption("YouTube links · MP4 · MOV · MP3 · WAV · M4A · WEBM")
    st.divider()
    st.caption("English transcription uses local Whisper. Hinglish transcription uses your configured Sarvam API key.")

# ---------- Header ----------
st.markdown(
    """
    <div class="hero">
      <div class="hero-kicker">Your AI-powered video companion</div>
      <h1>Less watching.<br>More understanding.</h1>
      <p>Turn long videos and meetings into clear summaries, useful takeaways, and a conversation you can search.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if page == "Workspace guide":
    st.markdown("## A simpler way to understand long videos")
    st.markdown(
        """
        <div class="panel">
        <h3>How it works</h3>
        1. Add a YouTube URL or upload a video/audio file.<br><br>
        2. Choose English or Hinglish transcription.<br><br>
        3. MeetMind transcribes the audio and prepares the summary, action items, decisions, and open questions.<br><br>
        4. Open the <b>Ask the video</b> tab to ask questions grounded in the transcript.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info("For Hinglish, make sure SARVAM_API_KEY is configured in your .env file. Gemini features require GEMINI_API_KEY.")
    st.stop()

# ---------- Input panel ----------
st.markdown("<div class='eyebrow'>01 / Add your source</div>", unsafe_allow_html=True)
st.markdown("## What should we break down today?")
source_mode = st.radio("Choose source", ["YouTube link", "Upload a file"], horizontal=True, label_visibility="collapsed")
source_value = None
uploaded_file = None

left, right = st.columns([1.45, 1], gap="large")
with left:
    if source_mode == "YouTube link":
        youtube_url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...", label_visibility="collapsed")
        if youtube_url.strip():
            source_value = youtube_url.strip()
        st.caption("Paste a public YouTube video link. Audio will be downloaded for transcription.")
    else:
        uploaded_file = st.file_uploader(
            "Drop your video or audio here",
            type=["mp4", "mov", "mkv", "webm", "mp3", "wav", "m4a", "mpeg", "mpga", "ogg", "flac"],
            help="Choose a video or audio file from your computer.",
        )
        if uploaded_file is not None:
            st.success(f"Ready: {uploaded_file.name} · {uploaded_file.size / (1024 * 1024):.1f} MB")
with right:
    language_choice = st.selectbox("Transcription language", ["English", "Hinglish"], help="English uses local Whisper. Hinglish uses Sarvam speech-to-text translation.")
    st.markdown("<div class='panel'><b>What you’ll get</b><br><br>✦ AI-generated title & summary<br>✦ Action items and decisions<br>✦ Open questions<br>✦ Transcript-based Q&A</div>", unsafe_allow_html=True)

start_col, note_col = st.columns([1, 2])
with start_col:
    analyze = st.button("✦  Analyze video", use_container_width=True, disabled=(not source_value and uploaded_file is None))
with note_col:
    st.caption("Long videos can take time to process. Whisper also downloads its model the first time it runs.")

if analyze:
    try:
        if uploaded_file is not None:
            source_value = save_upload(uploaded_file)
        if not source_value:
            st.warning("Add a YouTube URL or upload a file first.")
            st.stop()

        # Import only when the user starts processing; the CLI is protected by __main__ in main.py.
        from main import run_pipeline

        with st.status("MeetMind is working on your video…", expanded=True) as status:
            st.write("Preparing audio and splitting it into chunks…")
            st.write("Transcribing audio and generating your meeting insights…")
            st.write("Building your transcript Q&A assistant…")
            result = run_pipeline(source_value, language_choice.lower())
            status.update(label="Your video breakdown is ready!", state="complete", expanded=False)

        st.session_state["video_result"] = result
        st.session_state["chat_history"] = []
        st.session_state["source_label"] = uploaded_file.name if uploaded_file is not None else source_value
        st.success("Analysis completed successfully.")
    except Exception as exc:
        st.error(f"Something went wrong while processing the video: {exc}")
        st.info("Check that your .env contains the required API keys and that FFmpeg is installed and available in PATH.")

# ---------- Results ----------
result = st.session_state.get("video_result")
if result:
    st.divider()
    st.markdown("<div class='eyebrow'>02 / Your breakdown</div>", unsafe_allow_html=True)
    st.markdown(f"## {result.get('title') or 'Your video summary'}")
    st.caption("Source: " + str(st.session_state.get("source_label", "Current video")))

    transcript = result.get("transcript", "")
    words = len(transcript.split()) if transcript else 0
    chars = len(transcript)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"<div class='metric'><div class='metric-label'>Transcript words</div><div class='metric-value'>{words:,}</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric'><div class='metric-label'>Transcript characters</div><div class='metric-value'>{chars:,}</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown("<div class='metric'><div class='metric-label'>AI status</div><div class='metric-value'>Ready ✦</div></div>", unsafe_allow_html=True)

    tab_summary, tab_actions, tab_transcript, tab_chat = st.tabs(["✦ Summary", "✓ Action items", "≡ Transcript", "✳ Ask the video"])
    with tab_summary:
        st.markdown("### The big picture")
        render_text_block(result.get("summary", ""))
        st.divider()
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown("### Key decisions")
            render_text_block(result.get("key_decisions", ""))
        with c2:
            st.markdown("### Open questions")
            render_text_block(result.get("open_questions", ""))
        export_text = f"# {result.get('title', 'Video summary')}\n\n## Summary\n{result.get('summary', '')}\n\n## Action items\n{result.get('action_items', '')}\n\n## Key decisions\n{result.get('key_decisions', '')}\n\n## Open questions\n{result.get('open_questions', '')}\n"
        st.download_button("Download meeting notes (.md)", data=export_text, file_name="meetmind_notes.md", mime="text/markdown")
    with tab_actions:
        st.markdown("### Things to follow up on")
        render_text_block(result.get("action_items", ""))
    with tab_transcript:
        st.markdown("### Full transcript")
        if transcript:
            st.text_area("Transcript text", value=transcript, height=420, label_visibility="collapsed")
            st.download_button("Download transcript (.txt)", data=transcript, file_name="transcript.txt", mime="text/plain")
        else:
            st.info("No transcript was returned by the pipeline.")
    with tab_chat:
        st.markdown("### Ask questions about this video")
        st.caption("Answers are generated using the transcript context. If the transcript does not contain the answer, the assistant should say so.")
        for message in st.session_state.get("chat_history", []):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        prompt = st.chat_input("Ask something from the video…")
        if prompt:
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                with st.spinner("Searching the transcript…"):
                    try:
                        answer = result["rag_chain"].invoke(prompt)
                        st.markdown(answer)
                        st.session_state.chat_history.append({"role": "assistant", "content": answer})
                    except Exception as exc:
                        st.error(f"I couldn't answer that right now: {exc}")

st.markdown("<div class='footer-note'>MEETMIND · Built to turn long videos into clear next steps.</div>", unsafe_allow_html=True)
