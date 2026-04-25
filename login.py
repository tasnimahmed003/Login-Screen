import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Tasnim Ahmad | Portal", page_icon="🔐")

# Aesthetic Glassmorphism UI with Pop Animation
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
        margin-bottom: 5px;
        text-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }

    /* Button Styling */
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
        box-shadow: 0px 0px 15px rgba(255,255,255,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Session State
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
            st.error("Access Denied: Invalid credentials.")

    st.markdown('</div>', unsafe_allow_html=True)

def dashboard():
    st.markdown("<h3 style='text-align: center; opacity: 0.7;'>WORKSPACE ACTIVATED</h3>", unsafe_allow_html=True)
    
    name = st.text_input("Input your name:", placeholder="Type here and press Enter")

    if name:
        # Quick Burst Effect using HTML/JS (1 second pop)
        st.components.v1.html("""
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>
                confetti({
                    particleCount: 150,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#00f2fe', '#ff00cc', '#ffffff', '#7ef1ff']
                });
            </script>
        """, height=0)

        # Greeting Card
        st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.05);
                padding: 60px;
                border-radius: 30px;
                border: 1px solid rgba(0, 242, 254, 0.2);
                text-align: center;
                margin-top: 40px;
                animation: pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            ">
                <h1 style="font-size: 50px; font-weight: 100; color: #00f2fe; margin-bottom: 10px;">Hello, {name}!</h1>
                <p style="font-size: 20px; font-weight: 300; opacity: 0.9;">
                    You are looking exceptionally amazing today! ✨
                </p>
            </div>
            <style>
                @keyframes pop {
                    0% { transform: scale(0.8); opacity: 0; }
                    100% { transform: scale(1); opacity: 1; }
                }
            </style>
        """, unsafe_allow_html=True)

        # Success toast
        st.toast(f"Welcome back, {name}", icon="⚡")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# Execution
if st.session_state.logged_in:
    dashboard()
else:
    login()
