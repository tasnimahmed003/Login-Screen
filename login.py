import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Tasnim Login", page_icon="📱", layout="centered")

# CSS Fix for exact alignment and visibility
st.markdown("""
    <style>
    /* ১. পুরো পেজের ব্যাকগ্রাউন্ড এবং হেডার লুকানো */
    [data-testid="stHeader"] { display: none !important; }
    footer { visibility: hidden; }
    .stApp { background-color: #d1d5db; }

    /* ২. মেইন কন্টেইনার (মোবাইল লুক) */
    .app-frame {
        background: white;
        max-width: 380px;
        margin: 0 auto;
        border-radius: 30px;
        overflow: hidden;
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
        position: relative;
        min-height: 750px;
    }

    /* ৩. উপরের গ্রিন গ্রেডিয়েন্ট সেকশন */
    .top-section {
        background: linear-gradient(135deg, #2b6c6b 0%, #3e817e 100%);
        height: 320px;
        padding: 20px;
        position: relative;
        border-bottom-left-radius: 100px;
        z-index: 1;
    }

    .status-bar { display: flex; justify-content: space-between; color: white; font-size: 14px; opacity: 0.9; }
    .login-title { color: white; font-size: 42px; margin-top: 80px; font-weight: 300; }

    /* ৪. ফরম সেকশন (নিচের হালকা মিন্ট অংশ) */
    .form-section {
        background-color: #e6f9f6;
        margin-top: -80px;
        padding: 100px 30px 40px 30px;
        border-top-right-radius: 100px;
        min-height: 500px;
        position: relative;
        z-index: 2;
    }

    /* ৫. ইনপুট বক্স ফিক্স (টাইপ করলে যেন দেখা যায়) */
    div[data-testid="stTextInput"] input, div[data-testid="stPasswordInput"] input {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 2px solid #cbd5e1 !important;
        border-radius: 0px !important;
        color: #1e293b !important; /* টেক্সট কালার এখন স্পষ্ট ডার্ক */
        font-size: 16px !important;
        padding: 10px 0px !important;
    }
    
    /* ইনপুট লেবেল স্টাইল */
    label { color: #475569 !important; font-weight: 600 !important; }

    /* ৬. সাইন-ইন বাটন */
    .stButton>button {
        background-color: #0d2925 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 30px !important;
        float: right;
        border: none !important;
    }

    /* Forgot password and other text */
    .forgot-link { text-align: right; color: #64748b; font-size: 14px; margin-top: 5px; cursor: pointer; }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_ui():
    # ফ্রেম শুরু
    st.markdown('<div class="app-frame">', unsafe_allow_html=True)
    
    # উপরের অংশ
    st.markdown("""
        <div class="top-section">
            <div class="status-bar"><span>17:58</span><span>📶🔋</span></div>
            <h1 class="login-title">Login</h1>
        </div>
    """, unsafe_allow_html=True)

    # ফরমের অংশ
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    
    user = st.text_input("Username", placeholder="Enter User ID")
    pw = st.text_input("Password", type="password", placeholder="Enter Password")
    
    st.markdown('<p class="forgot-link">Forgot Password</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.checkbox("Remember Me")
    with col2:
        if st.button("Sign In"):
            st.session_state.logged_in = True
            st.rerun()

    # নিচের সোশ্যাল আইকন (ঐচ্ছিক)
    st.markdown("""
        <p style='text-align:center; color:#94a3b8; margin-top:30px;'>or</p>
        <div style='display:flex; justify-content:center; gap:20px;'>
            <div style='border:1px solid #cbd5e1; padding:10px 20px; border-radius:10px; color:#475569;'>G</div>
            <div style='border:1px solid #cbd5e1; padding:10px 25px; border-radius:10px; color:#475569;'></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True) # সব কন্টেইনার ক্লোজ

if st.session_state.logged_in:
    st.success("Success! Welcome, Tasnim.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
else:
    login_ui()
