import streamlit as st
import time

# Page Configuration for a clean, app-like center layout
st.set_page_config(page_title="App Portal", page_icon="📱", layout="centered")

# HUBuhu (Exact) CSS for image_6.png Design
st.markdown("""
    <style>
    /* 1. Global Page Reset to match the light grey background */
    .stApp {
        background-color: #d1d5db; /* Light grey, like in the image */
    }

    /* 2. Hide Streamlit clutter (top-right menu and bottom-left "Created with Streamlit") */
    header[data-testid="stHeader"] { visibility: hidden; height: 0; }
    footer { visibility: hidden; height: 0; }
    div[data-testid="stToolbar"] { display: none; }
    #MainMenu { display: none; }
    div.stDeployButton { display: none; }

    /* 3. The main app container (The white phone body) */
    .app-container {
        background: white;
        max-width: 400px;
        height: 800px; /* Estimated height for the screen inside the container */
        border-radius: 40px; /* Sharp corners with phone-like curve */
        box-shadow: 0 40px 100px -30px rgba(0, 0, 0, 0.4); /* Strong shadow like the image */
        margin: 50px auto; /* Centers the phone on page */
        overflow: hidden; /* Important for the top gradient */
        position: relative;
        font-family: 'Inter', sans-serif; /* Clean professional font */
    }

    /* 4. The main screen inside (The light lime container) */
    .screen-content {
        background-color: #e6f9f6; /* Very light, lime/mint background */
        width: 100%;
        height: 100%;
        position: relative;
        overflow: hidden;
    }

    /* 5. The top gradient section with "Login" text */
    .top-gradient-mask {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 50%; /* Reaches about halfway down */
        background: linear-gradient(135deg, #2b6c6b 0%, #3e817e 100%); /* Greenish-teal gradient */
        z-index: 1;
        border-bottom-left-radius: 120px; /* Curved cut like image */
    }

    /* Status bar details (time, signal) */
    .status-bar {
        position: absolute;
        top: 15px;
        left: 20px;
        right: 20px;
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 14px;
        z-index: 5; /* Above gradient */
    }

    /* Time on the left */
    .status-time { font-weight: bold; }
    /* Signal/Battery icon details (placeholders) */
    .status-icons { font-size: 14px; }

    /* The "Login" Text */
    .login-header-text {
        color: white;
        font-size: 40px;
        font-weight: 300; /* Light weight font */
        margin-top: 120px;
        margin-left: 30px;
        position: relative;
        z-index: 5;
    }

    /* 6. Form elements container (the card/input area) */
    .form-inputs-container {
        padding: 50px 30px 20px 30px; /* Space around inputs */
        margin-top: 50px; /* Pulls form up into the gradient cut */
        background-color: #e6f9f6; /* Matching screen bg */
        border-top-right-radius: 120px; /* Opposite curve to the gradient */
        position: relative;
        z-index: 3; /* Above gradient */
        font-family: 'Inter', sans-serif;
    }

    /* Styling the Input Fields and Labels */
    div.stTextInput label, div.stPasswordInput label {
        color: #4b5563; /* Grey text for labels */
        font-weight: 600;
        font-size: 16px;
        font-family: 'Inter', sans-serif !important;
    }

    div.stTextInput input, div.stPasswordInput input {
        border-bottom: 1.5px solid #d1d5db !important; /* Bottom-only border */
        border-top: none !important;
        border-left: none !important;
        border-right: none !important;
        border-radius: 0 !important;
        background-color: transparent !important;
        color: #1f2937 !important;
        padding-left: 0 !important;
        font-family: 'Inter', sans-serif !important;
    }
    div.stTextInput input::placeholder, div.stPasswordInput input::placeholder {
        color: #9ca3af !important; /* Lighter grey for placeholder */
    }

    /* Forgot Password link */
    .forgot-password-link {
        text-align: right;
        font-size: 14px;
        color: #4b5563;
        margin-top: 10px;
        display: block;
        cursor: pointer;
    }

    /* Checkbox (Remember Me) row */
    div[data-testid="stCheckbox"] label {
        color: #4b5563;
        font-size: 14px;
        font-weight: 500;
    }
    div[data-testid="stCheckbox"] div[role="checkbox"] {
        border-radius: 3px !important;
    }

    /* THE LOGIN BUTTON (SIGN IN) */
    .stButton>button {
        width: auto !important; /* Not full width */
        background-color: #0d2925 !important; /* Very dark green button */
        color: white !important;
        font-weight: bold;
        border-radius: 12px !important; /* Rounded corners */
        border: none !important;
        padding: 10px 25px !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3) !important;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4) !important;
    }

    /* Alignment for button and checkbox row */
    .login-action-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 25px;
    }

    /* 7. The Social Login section at bottom (Or... G/Apple icons) */
    .social-separator-text {
        text-align: center;
        font-size: 16px;
        color: #6b7280;
        margin: 40px 0 20px 0;
        font-family: 'Inter', sans-serif;
    }

    .social-icons-row {
        display: flex;
        justify-content: center;
        gap: 30px;
    }

    /* Social icons placeholder styling */
    .social-icon-placeholder {
        width: 50px;
        height: 50px;
        border: 1.5px solid #d1d5db; /* Grey thin border */
        border-radius: 15px; /* Box curve like image */
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        color: #4b5563;
        font-size: 20px;
        cursor: pointer;
        font-family: 'Inter', sans-serif;
    }

    /* Confetti Burst and Card for Welcome */
    .welcome-card {
        background: white;
        padding: 60px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #3e817e;
        margin-top: 40px;
        animation: burst 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    @keyframes burst {
        0% { transform: scale(0); opacity: 0; }
        60% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Main Application Execution Logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_screen():
    # 1. Opening App Container (The phone frame)
    st.markdown('<div class="app-container">', unsafe_allow_html=True)
    
    # 2. Status Bar and Header inside the container
    st.markdown("""
        <div class="status-bar">
            <span class="status-time">17:58</span>
            <span class="status-icons">📶🔋</span>
        </div>
        <div class="top-gradient-mask">
            <h1 class="login-header-text">Login</h1>
        </div>
    """, unsafe_allow_html=True)

    # 3. Form fields container
    st.markdown('<div class="form-inputs-container">', unsafe_allow_html=True)
    
    # Username Field
    st.text_input("Username", placeholder="Enter User ID or Email")
    
    # Password Field
    st.text_input("Password", type="password", placeholder="Enter Password")
    
    # Forgot Password link
    st.markdown('<a class="forgot-password-link">Forgot Password</a>', unsafe_allow_html=True)
    
    # Action Row: Remember Me and Sign In Button
    st.markdown('<div class="login-action-row">', unsafe_allow_html=True)
    
    # Checkbox with custom style integration
    with st.container():
        st.checkbox("Remember Me")
    
    # THE Button (Hubuhu)
    if st.button("Sign In"):
        # Login is hardcoded to any input for this example
        st.session_state.logged_in = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True) # Closing Action Row

    # 4. Social Login section
    st.markdown('<p class="social-separator-text">or</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="social-icons-row">
            <div class="social-icon-placeholder">G</div>
            <div class="social-icon-placeholder"></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Closing Form container
    st.markdown('</div>', unsafe_allow_html=True) # Closing App container

def dashboard():
    st.markdown("<h2 style='text-align: center; color: #1f2937;'>Authorized Access</h2>", unsafe_allow_html=True)
    
    # Simple Dashboard Input like you had before, integrated into the new theme
    st.markdown('<p style="text-align: center; color: #3e817e; font-weight: bold;">⚡ Input your name to activate workspace:</p>', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Waiting for name...")

    if name:
        # Integrated Confetti and Welcome card that "Bursts"
        with st.container():
            st.markdown(f"""
                <div class="welcome-card">
                    <h1 style="font-size: 50px; color: #3e817e; margin-bottom: 10px;">Hello, {name}!</h1>
                    <p style="font-size: 20px; color: #4b5563;">You are looking exceptionally amazing today! ✨</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.toast(f"Synchronizing Workspace: {name}", icon='🚀')
        time.sleep(1)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# Execution Logic gate
if st.session_state.logged_in:
    dashboard()
else:
    login_screen()
