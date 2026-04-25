import streamlit as st
import random

# --- Page Configuration ---
st.set_page_config(page_title="Tasnim Ahmad - Project", page_icon="✨", layout="centered")

# --- Premium Custom CSS ---
st.markdown("""
<style>
    /* Background Color */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Login Header Gradient Text */
    .login-header {
        text-align: center;
        background: -webkit-linear-gradient(#E65100, #FF9800);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: -10px;
    }
    .login-subheader {
        text-align: center;
        color: #64748B;
        font-size: 18px;
        margin-bottom: 30px;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 2.5em;
        background: linear-gradient(135deg, #E65100 0%, #FF9800 100%);
        color: white;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(230, 81, 0, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #BF360C 0%, #E65100 100%);
        box-shadow: 0 6px 10px rgba(230, 81, 0, 0.3);
        transform: translateY(-2px);
    }
    
    /* Input Fields Styling */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #CBD5E1;
        padding: 10px;
    }
    .stNumberInput>div>div>input {
        border-radius: 8px;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        box-shadow: 2px 0 5px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'login_attempts' not in st.session_state:
    st.session_state['login_attempts'] = 0
if 'account_locked' not in st.session_state:
    st.session_state['account_locked'] = False

# ==========================================
#              LOGIN PORTAL
# ==========================================
if not st.session_state['logged_in']:
    st.markdown("<div class='login-header'>Tasnim Ahmad</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-subheader'>Welcome back! Please login to your dashboard.</div>", unsafe_allow_html=True)
    
    # লগইন ফর্ম মাঝখানে রাখার জন্য কলাম ব্যবহার
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.session_state['account_locked']:
            st.error("🔒 Account Locked: Too many failed attempts. Please contact administrator.")
        else:
            with st.container():
                username = st.text_input("👤 Username", placeholder="Enter your username")
                password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
                
                st.write("") # একটু ফাঁকা জায়গা তৈরির জন্য
                if st.button("Secure Login"):
                    if username == "Tasnim" and password == "12345":
                        st.session_state['logged_in'] = True
                        st.rerun()
                    else:
                        st.session_state['login_attempts'] += 1
                        if st.session_state['login_attempts'] >= 3:
                            st.session_state['account_locked'] = True
                            st.rerun()
                        else:
                            remaining = 3 - st.session_state['login_attempts']
                            st.warning(f"⚠️ Invalid credentials. {remaining} attempts remaining.")

# ==========================================
#              MAIN DASHBOARD
# ==========================================
else:
    # --- Sidebar Navigation ---
    st.sidebar.markdown("<h2 style='text-align: center; color: #E65100;'>📌 Navigation</h2>", unsafe_allow_html=True)
    page = st.sidebar.radio("", ["🏠 Home", "🧮 Calculator", "🎮 Rock Paper Scissors"])
    
    st.sidebar.divider()
    if st.sidebar.button("🚪 Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    # --- 1. Home Page ---
    if page == "🏠 Home":
        st.markdown("<h1 style='color: #334155;'>User Dashboard</h1>", unsafe_allow_html=True)
        st.write("Welcome to the premium management system. Select an option from the sidebar to get started.")
        st.divider()
        
        st.subheader("✨ Let's personalize your experience!")
        name_input = st.text_input("Enter your beautiful name:")
        if st.button("Say Hello"):
            if name_input:
                st.success(f"🎉 Welcome, **{name_input}**! You are looking exceptionally amazing today! ✨ Take care of yourself 🤍")
                st.balloons() # কিউট অ্যানিমেশন
            else:
                st.info("Please provide a name above.")

    # --- 2. Normal (Reliable) Calculator ---
    elif page == "🧮 Calculator":
        st.markdown("<h1 style='color: #334155;'>Smart Calculator</h1>", unsafe_allow_html=True)
        st.write("সহজ, দ্রুত এবং নির্ভুল হিসাব করার টুল।")
        st.markdown("""---""")
        
        # পাশাপাশি ৩টি কলামে ইনপুট নেওয়ার ব্যবস্থা
        calc_col1, calc_col2, calc_col3 = st.columns([2, 1, 2])
        
        with calc_col1:
            num1 = st.number_input("First Number", value=0.0, step=1.0)
            
        with calc_col2:
            operator = st.selectbox("Operator", ["+", "-", "×", "÷"])
            
        with calc_col3:
            num2 = st.number_input("Second Number", value=0.0, step=1.0)
            
        st.write("")
        if st.button("Calculate Result"):
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "×":
                result = num1 * num2
            elif operator == "÷":
                if num2 == 0:
                    result = "Error: Cannot divide by zero!"
                else:
                    result = num1 / num2
            
            # ফলাফল দেখানো
            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"**Result:** {num1} {operator} {num2} = **{result}**")

    # --- 3. Rock Paper Scissors Game ---
    elif page == "🎮 Rock Paper Scissors":
        st.markdown("<h1 style='color: #334155;'>Rock Paper Scissors</h1>", unsafe_allow_html=True)
        st.write("Can you beat the computer? Try your luck!")
        st.markdown("""---""")
        
        col_game1, col_game2 = st.columns(2)
        with col_game1:
            user_choice = st.radio("Select your move:", ["🪨 Rock", "📄 Paper", "✂️ Scissors"])
            
        with col_game2:
            st.write("")
            st.write("")
            if st.button("🎮 Play Now"):
                options = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
                computer_choice = random.choice(options)
                
                st.markdown(f"**You chose:** {user_choice}")
                st.markdown(f"**Computer chose:** {computer_choice}")
                
                # লজিক
                if user_choice == computer_choice:
                    st.info("🤝 It is a Tie!")
                elif (user_choice == "🪨 Rock" and computer_choice == "✂️ Scissors") or \
                     (user_choice == "📄 Paper" and computer_choice == "🪨 Rock") or \
                     (user_choice == "✂️ Scissors" and computer_choice == "📄 Paper"):
                    st.success("🎉 Awesome! You Win!")
                    st.balloons()
                else:
                    st.error("💻 Computer Wins! Better luck next time.")
