import streamlit as st
import streamlit.components.v1 as components
import time

# Page Configuration
st.set_page_config(page_title="Tasnim Ahmad | Portal", page_icon="🔐")

# Aesthetic Glassmorphism UI with Orange Highlight
st.markdown("""
    <style>
    /* Background Animation */
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
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 50px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        text-align: center;
    }

    /* Bold Gradient Name */
    .my-name {
        font-size: 55px;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2fe, #7ef1ff, #ff00cc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 2px;
    }

    /* Login Button Styling */
    .stButton>button {
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px;
        border-radius: 12px;
        font-weight: 700;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.2);
    }

    /* Highlighted Orange Input for Name */
    .orange-highlight input {
        border: 2px solid #ff7b00 !important;
        box-shadow: 0 0 15px rgba(255, 123, 0, 0.4) !important;
        background: rgba(255, 123, 0, 0.05) !important;
        color: white !important;
        border-radius: 15px !important;
    }

    /* Pulse effect for the Orange Guide */
    .apply-hint {
        color: #ff7b00;
        font-weight: bold;
        font-size: 14px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { opacity: 0.5; }
        50% { opacity: 1; }
        100% { opacity: 0.5; }
    }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="my-name">TASNIM AHMAD</h1>', unsafe_allow_html=True)
    st.markdown("<p style='opacity: 0.5; font-size: 14px;'>SECURE SYSTEM AUTHENTICATION</p>", unsafe_allow_html=True)
    
    u = st.text_input("Username", placeholder="Enter your ID")
    p = st.text_input("Password", type="password", placeholder="Enter security key")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Login"):
        if u == "admin" and p == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Access Denied.")
    st.markdown('</div>', unsafe_allow_html=True)

def dashboard():
    st.markdown("<h3 style='text-align: center; opacity: 0.7;'>WORKSPACE ACTIVATED</h3>", unsafe_allow_html=True)
    
    # Highlighting the name input section
    st.markdown('<p class="apply-hint">⚡ PRESS ENTER TO APPLY AFTER TYPING</p>', unsafe_allow_html=True)
    
    # Custom class for orange highlight
    st.markdown('<div class="orange-highlight">', unsafe_allow_html=True)
    name = st.text_input("Input your name:", placeholder="Type your name here...")
    st.markdown('</div>', unsafe_allow_html=True)

    if name:
        # Instant Burst (1s Pop)
        components.html("""
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>
                confetti({
                    particleCount: 200,
                    spread: 100,
                    origin: { y: 0.6 },
                    colors: ['#ff7b00', '#00f2fe', '#ffffff']
                });
            </script>
        """, height=0)

        st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.05); padding: 50px; border-radius: 30px; text-align: center; border: 1px solid #ff7b00; margin-top: 40px;">
                <h1 style="font-size: 45px; color: #ff7b00;">Hello, {name}!</h1>
                <p style="font-size: 20px; opacity: 0.9;">You are looking exceptionally amazing today! ✨</p>
            </div>
        """, unsafe_allow_html=True)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

if st.session_state.logged_in:
    dashboard()
else:
    login()
