import streamlit as st

# Page configuration for a clean layout
st.set_page_config(page_title="Secure Login", page_icon="🔐", layout="centered")

# CSS for the exact professional look without extra icons
st.markdown("""
    <style>
    /* ১. অপ্রয়োজনীয় হেডার এবং ফুটার পুরোপুরি রিমুভ করা */
    [data-testid="stHeader"] { display: none !important; }
    footer { visibility: hidden !important; }
    .stApp { background-color: #d1d5db; } /* বাইরের ব্যাকগ্রাউন্ড */

    /* ২. মোবাইল কন্টেইনার ফিক্স */
    .app-main {
        background-color: white;
        max-width: 400px;
        height: auto;
        min-height: 700px;
        margin: 20px auto;
        border-radius: 40px;
        overflow: hidden;
        box-shadow: 0 30px 60px rgba(0,0,0,0.3);
        position: relative;
    }

    /* ৩. গ্রিন গ্রেডিয়েন্ট সেকশন (টাইম/ওয়াইফাই ছাড়া) */
    .header-gradient {
        background: linear-gradient(135deg, #2b6c6b 0%, #3e817e 100%);
        height: 350px;
        width: 100%;
        border-bottom-left-radius: 120px;
        display: flex;
        align-items: center;
        padding-left: 40px;
        z-index: 1;
        position: relative;
    }

    .login-text {
        color: white;
        font-size: 45px;
        font-weight: 300;
        margin: 0;
    }

    /* ৪. ফরম সেকশন (নিচের হালকা মিন্ট কালার) */
    .form-container {
        background-color: #e6f9f6;
        margin-top: -100px; /* গ্রেডিয়েন্টের ওপরে উঠানোর জন্য */
        padding: 120px 35px 50px 35px;
        border-top-right-radius: 120px;
        position: relative;
        z-index: 2;
        min-height: 450px;
    }

    /* ৫. ইনপুট ফিল্ড স্টাইলিং (ID/Email Placeholder সহ) */
    div[data-testid="stTextInput"] label, div[data-testid="stPasswordInput"] label {
        color: #4b5563 !important;
        font-weight: bold !important;
        font-size: 15px !important;
    }

    div[data-testid="stTextInput"] input, div[data-testid="stPasswordInput"] input {
        border: none !important;
        border-bottom: 1.5px solid #cbd5e1 !important;
        border-radius: 0px !important;
        background-color: transparent !important;
        color: #1f2937 !important;
        padding: 10px 0px !important;
        font-size: 16px !important;
    }

    /* ৬. সাইন-ইন বাটন পজিশন ও স্টাইল */
    .stButton > button {
        background-color: #0d2925 !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 30px !important;
        font-weight: bold !important;
        float: right; /* মকআপের মতো ডানে পজিশন */
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }

    /* Forgot Password Link */
    .forgot-pass {
        text-align: right;
        font-size: 13px;
        color: #6b7280;
        margin-top: 5px;
        display: block;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# লগইন লজিক শুরু
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def render_login():
    # মেইন কন্টেইনার শুরু
    st.markdown('<div class="app-main">', unsafe_allow_html=True)
    
    # উপরের গ্রিন সেকশন (কোনো আইকন নেই)
    st.markdown('<div class="header-gradient"><h1 class="login-text">Login</h1></div>', unsafe_allow_html=True)

    # ফরম সেকশন শুরু
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Username (ID/Email)
    st.text_input("Username", placeholder="Enter User ID or Email")
    
    # Password
    st.text_input("Password", type="password", placeholder="Enter Password")
    
    st.markdown('<a class="forgot-pass">Forgot Password</a>', unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.checkbox("Remember Me")
    with col2:
        if st.button("Sign In"):
            st.session_state.logged_in = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # সোশ্যাল আইকন এরিয়া (নিচে)
    st.markdown("""
        <div style='margin-top: 60px; text-align: center;'>
            <p style='color: #9ca3af; font-size: 14px;'>or</p>
            <div style='display: flex; justify-content: center; gap: 25px; margin-top: 15px;'>
                <div style='border: 1px solid #d1d5db; padding: 10px 22px; border-radius: 12px; color: #4b5563;'>G</div>
                <div style='border: 1px solid #d1d5db; padding: 10px 22px; border-radius: 12px; color: #4b5563;'></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True) # ক্লোজিং কন্টেইনার

if not st.session_state.logged_in:
    render_login()
else:
    st.success("Successfully Logged In!")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
