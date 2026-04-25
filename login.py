import streamlit as st

# পেজ কনফিগারেশন
st.set_page_config(page_title="Login UI", layout="centered", page_icon="🔐")

# হুবহু মকআপের ডিজাইনের জন্য CSS
st.markdown("""
    <style>
    /* ডিফল্ট হেডার ও ফুটার হাইড করা */
    [data-testid="stHeader"] { display: none !important; }
    footer { visibility: hidden !important; }
    
    /* পেজের বাইরের গ্রে ব্যাকগ্রাউন্ড */
    .stApp {
        background-color: #d1d5db !important;
    }

    /* ১. মেইন মোবাইল/অ্যাপ কন্টেইনার */
    .block-container {
        max-width: 360px !important;
        min-width: 360px !important;
        padding: 0rem !important;
        background-color: #eefbf7 !important; /* হালকা মিন্ট কালার */
        border-radius: 40px !important;
        box-shadow: 0 25px 50px rgba(0,0,0,0.2) !important;
        margin: 50px auto !important;
        overflow: hidden !important;
        min-height: 720px !important;
    }

    /* ২. উপরের গ্রিন গ্রেডিয়েন্ট এবং কার্ভ (টাইম/নেটওয়ার্ক ছাড়া) */
    .header-shape {
        background: linear-gradient(145deg, #2b6c6b 0%, #438b88 100%);
        height: 280px;
        width: 100%;
        border-bottom-left-radius: 90px; /* এই কার্ভটাই মকআপের মূল আকর্ষণ */
        position: relative;
        margin-bottom: 35px;
    }

    /* Login লেখার পজিশন */
    .login-title {
        position: absolute;
        bottom: 35px;
        left: 35px;
        color: #ffffff;
        font-size: 40px;
        font-weight: 300;
        margin: 0;
        letter-spacing: 0.5px;
    }

    /* ৩. ইনপুট ফিল্ড কাস্টমাইজেশন (ইউজারনেম লেবেল ছাড়া) */
    div[data-testid="stTextInput"] label {
        display: none !important; /* লেবেল পুরোপুরি মুছে ফেলা হলো */
    }
    div[data-testid="stTextInput"] input {
        border: none !important;
        border-bottom: 1.5px solid #cbd5e1 !important;
        border-radius: 0px !important;
        background: transparent !important;
        padding: 5px 0px 10px 0px !important;
        color: #1f2937 !important;
        font-size: 15px !important;
        box-shadow: none !important;
    }
    div[data-testid="stTextInput"] input::placeholder {
        color: #94a3b8 !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-bottom: 1.5px solid #2b6c6b !important;
    }

    /* ৪. Forgot Password */
    .forgot-text {
        text-align: right;
        font-size: 12px;
        font-weight: bold;
        color: #334155;
        margin-top: 5px;
        cursor: pointer;
    }

    /* ৫. চেকবক্স এবং বাটন */
    div[data-testid="stCheckbox"] label {
        color: #475569 !important;
        font-size: 13px !important;
    }
    div[data-testid="stCheckbox"] div[role="checkbox"] {
        border-radius: 3px !important;
        border-color: #94a3b8 !important;
    }

    .stButton>button {
        background-color: #1b4341 !important; /* ডার্ক গ্রিন */
        color: white !important;
        border-radius: 8px !important;
        padding: 5px 25px !important;
        border: none !important;
        font-weight: 600 !important;
        float: right !important; /* বাটন ডানদিকে ফিক্সড */
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    }

    /* ৬. সোশ্যাল আইকন */
    .social-container {
        text-align: center;
        margin-top: 60px;
    }
    .or-text {
        font-size: 13px;
        color: #94a3b8;
        margin-bottom: 15px;
    }
    .icon-box {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 45px;
        height: 45px;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        margin: 0 10px;
        font-weight: bold;
        color: #1b4341;
        font-size: 18px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# সেশন স্টেট সেটআপ
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_screen():
    # হেডার গ্রিন শেপ (স্ট্যাটাস বার ছাড়া)
    st.markdown('<div class="header-shape"><h1 class="login-title">Login</h1></div>', unsafe_allow_html=True)

    # দুই পাশে ফাঁকা জায়গা রাখার জন্য কলাম ব্যবহার
    _, col_form, _ = st.columns([0.12, 0.76, 0.12])

    with col_form:
        # Username ইনপুট (শুধু Placeholder থাকবে)
        st.text_input("user_input", placeholder="Enter User ID", label_visibility="collapsed")
        
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        # Password ইনপুট (শুধু Placeholder থাকবে)
        st.text_input("pass_input", type="password", placeholder="Enter Password", label_visibility="collapsed")
        
        # Forgot Password লিঙ্ক
        st.markdown('<div class="forgot-text">Forgot Password</div>', unsafe_allow_html=True)
        
        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
        
        # চেকবক্স এবং বাটন পাশাপাশি
        c1, c2 = st.columns([1, 1])
        with c1:
            st.checkbox("Remember Me")
        with c2:
            if st.button("Sign In"):
                st.session_state.logged_in = True
                st.rerun()

        # সোশ্যাল আইকন (G এবং )
        st.markdown("""
            <div class="social-container">
                <div class="or-text">or</div>
                <div style="display:flex; justify-content:center;">
                    <div class="icon-box">G</div>
                    <div class="icon-box"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# লজিক এক্সিকিউশন
if st.session_state.logged_in:
    st.success("Successfully Logged In!")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
else:
    login_screen()
