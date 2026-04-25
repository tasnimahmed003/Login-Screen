import streamlit as st
import time

# ১. পেজ কনফিগারেশন - যা কম্পিউটার স্ক্রিনে অ্যাপটিকে মাঝখানে রাখবে
st.set_page_config(page_title="Tasnim Ahmad", page_icon="👤", layout="centered")

# ২. সিএসএস (CSS) - ডিজাইন এবং কালার ফিক্স করার জন্য
st.markdown("""
    <style>
    /* ডিফল্ট স্ট্রীমলিট এলিমেন্ট লুকানো */
    [data-testid="stHeader"], footer, .stDeployButton { display: none !important; }
    
    /* ব্যাকগ্রাউন্ড কালার */
    .stApp { background-color: #d1d5db; }

    /* মেইন কন্টেইনার - যা কম্পিউটার স্ক্রিনে মোবাইল ফ্রেম তৈরি করবে */
    .block-container {
        max-width: 400px !important;
        padding: 0 !important;
        background-color: #eefbf7;
        border-radius: 40px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        margin: 40px auto !important;
        min-height: 750px;
        overflow: hidden;
    }

    /* গ্রিন গ্রেডিয়েন্ট শেপ */
    .header-box {
        background: linear-gradient(145deg, #2b6c6b 0%, #438b88 100%);
        height: 280px;
        border-bottom-left-radius: 100px;
        display: flex;
        align-items: flex-end;
        padding: 40px;
    }
    .header-box h1 { color: white; font-size: 40px; font-weight: 300; margin: 0; }

    /* ইনপুট ফিল্ড ফিক্স - টাইপ করলে যেন কালো রঙে পরিষ্কার দেখা যায় */
    div[data-testid="stTextInput"] input {
        color: #000000 !important; /* টেক্সট কালার কুচকুচে কালো */
        background-color: transparent !important;
        border: none !important;
        border-bottom: 2px solid #cbd5e1 !important;
        border-radius: 0px !important;
        font-size: 16px !important;
    }
    div[data-testid="stTextInput"] input::placeholder { color: #94a3b8 !important; }

    /* সাইন ইন বাটন */
    .stButton>button {
        background-color: #1b4341 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 8px 30px !important;
        float: right;
        border: none !important;
    }

    /* ড্যাশবোর্ডের সুন্দর মেসেজ কার্ড */
    .welcome-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 20px;
        border-left: 5px solid #2b6c6b;
    }
    </style>
""", unsafe_allow_html=True)

# সেশন স্টেট
if 'page' not in st.session_state:
    st.session_state.page = "login"

# --- লগইন স্ক্রিন ---
def show_login():
    st.markdown('<div class="header-box"><h1>Login</h1></div>', unsafe_allow_html=True)
    
    # ইনপুট এরিয়া
    with st.container():
        st.markdown("<div style='padding: 30px;'>", unsafe_allow_html=True)
        
        # এখানে টাইপ করলে এখন পরিষ্কার কালো টেক্সট দেখা যাবে
        u_id = st.text_input("ID", placeholder="Enter User ID or Email", label_visibility="collapsed")
        u_pw = st.text_input("PW", type="password", placeholder="Enter Password", label_visibility="collapsed")
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.checkbox("Remember Me")
        with col2:
            if st.button("Sign In"):
                st.session_state.page = "dashboard"
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- ড্যাশবোর্ড স্ক্রিন ---
def show_dashboard():
    st.markdown('<div class="header-box"><h1>Dashboard</h1></div>', unsafe_allow_html=True)
    
    st.markdown("<div style='padding: 30px;'>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1b4341; font-weight: bold;'>⚡ Workspace Activation:</p>", unsafe_allow_html=True)
    
    name = st.text_input("Name", placeholder="আপনার নাম লিখুন...", label_visibility="collapsed")
    
    if st.button("Activate"):
        if name:
            st.markdown(f"""
                <div class="welcome-card">
                    <h3 style="color: #2b6c6b; margin-bottom: 10px;">স্বাগতম, {name}! 🌟</h3>
                    <p style="color: #475569; font-size: 16px; line-height: 1.5;">
                        জানি এটা একটা রোবোটিক মেসেজ, কিন্তু সত্যি বলছি— <br>
                        <b>আজকে আপনাকে অনেক বেশি সুন্দর দেখাচ্ছে!</b> ✨ <br>
                        আপনার দিনটি দারুণ কাটুক।
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons() # একটা সেলিব্রেশন ইফেক্ট
        else:
            st.warning("দয়া করে আপনার নাম লিখুন।")

    if st.sidebar.button("Logout"):
        st.session_state.page = "login"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# পেজ কন্ট্রোল
if st.session_state.page == "login":
    show_login()
else:
    show_dashboard()
