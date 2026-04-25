import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Tasnim Ahmad | Portal", page_icon="❄️", layout="centered")

# Professional Aesthetic Glassmorphism UI
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e293b, #334155, #1e1b4b);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #f8fafc;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 50px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        text-align: center;
    }

    /* Input Styling */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 12px !important;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px;
        border-radius: 12px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.5);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# Session State Persistence
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

def login():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='font-weight: 200; letter-spacing: 2px;'>TASNIM AHMAD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; opacity: 0.6; margin-bottom: 30px;'>SECURE ACCESS TERMINAL</p>", unsafe_allow_html=True)
    
    u = st.text_input("IDENTITY", placeholder="Admin ID")
    p = st.text_input("ACCESS KEY", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("INITIALIZE"):
        if u == "admin" and p == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.session_state.attempts += 1
            left = 3 - st.session_state.attempts
            if left > 0:
                st.toast(f"Access Denied. {left} attempts remaining.", icon="⚠️")
            else:
                st.error("System Override: Terminal Locked.")
                st.stop()
    st.markdown('</div>', unsafe_allow_html=True)

def workspace():
    st.markdown("<h2 style='text-align: center; font-weight: 200;'>ACCESS GRANTED</h2>", unsafe_allow_html=True)
    
    name = st.text_input("ENTER USERNAME TO ACTIVATE:", placeholder="Waiting for input...")

    if name:
        # Visual Effects
        st.balloons()
        st.snow()
        
        # Minimalist Transparent Greeting Card
        st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.05);
                padding: 60px;
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                text-align: center;
                margin-top: 40px;
            ">
                <p style='letter-spacing: 3px; opacity: 0.5;'>WELCOME BACK</p>
                <h1 style="font-size: 60px; font-weight: 100; margin: 10px 0;">{name.upper()}</h1>
                <div style="width: 50px; hieght: 2px; background: white; margin: 20px auto; opacity: 0.2;"></div>
                <p style="font-style: italic; opacity: 0.7;">Dashboard synchronization in progress...</p>
            </div>
        """, unsafe_allow_html=True)

        with st.spinner('Syncing...'):
            time.sleep(5)
            st.toast(f"Workspace Ready: {name}", icon="✔️")

    if st.sidebar.button("DISCONNECT"):
        st.session_state.logged_in = False
        st.session_state.attempts = 0
        st.rerun()

# Logic Gate
if st.session_state.logged_in:
    workspace()
else:
    login()
