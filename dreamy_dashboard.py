
import streamlit as st
from datetime import datetime
import pytz
import os

st.set_page_config(page_title="Dreamy Desk", layout="wide")

NOTE_PATH = "sticky_note.txt"
def load_note():
    if os.path.exists(NOTE_PATH):
        with open(NOTE_PATH, "r") as f:
            return f.read()
    return ""

def save_note(content):
    with open(NOTE_PATH, "w") as f:
        f.write(content)

def delete_note():
    if os.path.exists(NOTE_PATH):
        os.remove(NOTE_PATH)

st.markdown("""
    <style>
        html, body {
            background: linear-gradient(to right, #fcefee, #e6f0ff);
        }
        .glass {
            background: rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            padding: 20px;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .icon-tile {
            width: 100px;
            height: 100px;
            background: rgba(255,255,255,0.5);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-weight: bold;
            transition: all 0.3s ease;
            color: #6c5ce7;
        }
        .icon-tile:hover {
            transform: scale(1.05);
            background: #dfe6e9;
        }
    </style>
""", unsafe_allow_html=True)

tab = st.sidebar.radio("Navigate", ["Home", "Productivity"])

if tab == "Home":
    st.markdown('<h1 style="color: #6c5ce7;">Your dreamy desk awaits</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        tz = pytz.timezone("America/New_York")
        st.markdown(f"<h3>{datetime.now(tz).strftime('%I:%M %p')} — Fincastle, VA</h3>", unsafe_allow_html=True)
    with col2:
        search = st.text_input("Google Search", "")
        if search:
            st.markdown(f"[Search Google for '{search}'](https://www.google.com/search?q={search})")

    st.subheader("Quick Tools")
    col1, col2, col3 = st.columns(3)
    col1.markdown('<div class="icon-tile">⏱️ Timer</div>', unsafe_allow_html=True)
    col2.markdown('<div class="icon-tile">🎙️ Podcast</div>', unsafe_allow_html=True)
    col3.markdown('<div class="icon-tile">📝 Notes</div>', unsafe_allow_html=True)

    st.markdown("### Spotify")
    st.markdown('[Connect your Spotify](https://accounts.spotify.com/authorize)')

    st.markdown("### Weather — Fincastle, VA")
    st.info("72°F — Mostly Sunny\nLow: 58°F | High: 74°F")

    st.markdown("### Sticky Note")
    note = st.text_area("Note", value=load_note(), height=150)
    col1, col2 = st.columns(2)
    if col1.button("Save Note"):
        save_note(note)
        st.success("Note saved!")
    if col2.button("Delete Note"):
        delete_note()
        st.warning("Note deleted!")

elif tab == "Productivity":
    st.markdown("## Your Work Essentials")
    icons = {
        "Canva": "https://www.canva.com",
        "Zoom": "https://zoom.us",
        "Wealthbox": "https://www.wealthbox.com",
        "Gmail": "https://mail.google.com",
        "Gamma": "https://gamma.app",
        "Docs": "https://docs.google.com",
        "ChatGPT": "https://chat.openai.com",
        "Browser": "https://www.google.com",
        "Pinterest": "https://www.pinterest.com",
        "Monday": "https://monday.com",
        "Calendar": "https://calendar.google.com",
        "Calculator": "https://www.google.com/search?q=calculator"
    }
    cols = st.columns(4)
    for i, (name, url) in enumerate(icons.items()):
        with cols[i % 4]:
            st.markdown(f"[<div class='icon-tile'>{name}</div>]({url})", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### To-Do List")
    st.markdown("- [x] Task 1\n  - [ ] Subtask 1.1\n  - [x] Subtask 1.2\n- [ ] Task 2")

    st.markdown("### Clock In / Clock Out")
    col1, col2 = st.columns(2)
    col1.button("Clock In")
    col2.button("Clock Out")

    st.markdown("### Meeting Notes")
    st.text_area("Meeting Notes", "")

    st.markdown("### End-of-Day Summary")
    st.text_area("Highlights", "")
    st.text_area("Challenges", "")
    st.text_area("Wrap-up", "")

    st.markdown("### Timecard")
    st.markdown('[Open Canva Timecard](https://www.canva.com)', unsafe_allow_html=True)

    st.markdown("### Quick Access Folder")
    with st.expander("📁 Click to view saved links/files"):
        st.markdown("- [Google Docs](https://docs.google.com)")
        st.markdown("- [My Timecard](https://www.canva.com)")
        st.markdown("- [Drive Folder](https://drive.google.com)")
