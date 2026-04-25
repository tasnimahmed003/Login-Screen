import streamlit as st
import random

# --- Page Configuration ---
st.set_page_config(page_title="Tasnim Ahmad - App", page_icon="✨", layout="centered")

# --- Custom CSS for Orange Theme & Professional Look ---
st.markdown("""
<style>
    .stApp {
        background-color: #F7F9FC;
    }
    div.stButton > button:first-child {
        background-color: #E65100;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #BF360C;
        color: white;
    }
    .title-text {
        text-align: center;
        color: #E65100;
        font-family: 'Arial', sans-serif;
        font-size: 36px;
        font-weight: bold;
        margin-top: -20px;
    }
    .subtitle-text {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Management ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- Login Screen ---
if not st.session_state['logged_in']:
    st.markdown("<div class='title-text'>Tasnim Ahmad</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle-text'>Welcome Back</div>", unsafe_allow_html=True)
    
    # White card-like container for login
    with st.container():
        username = st.text_input("Username", placeholder="Enter username here...")
        password = st.text_input("Password", type="password", placeholder="Enter password here...")
        
        st.markdown("<br>", unsafe_allow_html=True) # Spacing
        
        login_button = st.button("Login")
        
        if login_button:
            if username == "Tasnim" and password == "12345":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("❌ Invalid Username or Password!")

# --- Dashboard Screen ---
else:
    st.title("🎛️ Dashboard")
    st.write("Welcome to your professional workspace.")
    st.divider()
    
    # 1. Name Input & Welcome Message
    st.subheader("👋 Greetings")
    user_name = st.text_input("Please enter your name:")
    if st.button("Say Hello"):
        if user_name:
            st.success(f"Welcome, **{user_name}**! You are looking absolutely stunning today. Keep shining and have a wonderful day ahead! ✨")
        else:
            st.warning("Please enter your name first.")
            
    st.divider()
    
    # Dashboard Features (Columns)
    col1, col2 = st.columns(2)
    
    # 2. Calculator Tool
    with col1:
        st.subheader("🧮 Calculator")
        num1 = st.number_input("First Number", value=0.0)
        operation = st.selectbox("Select Operation", ["+", "-", "×", "÷"])
        num2 = st.number_input("Second Number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "+":
                st.info(f"**Result:** {num1 + num2}")
            elif operation == "-":
                st.info(f"**Result:** {num1 - num2}")
            elif operation == "×":
                st.info(f"**Result:** {num1 * num2}")
            elif operation == "÷":
                if num2 != 0:
                    st.info(f"**Result:** {num1 / num2}")
                else:
                    st.error("Cannot divide by zero!")
                    
    # 3. Mini Game (Number Guessing)
    with col2:
        st.subheader("🎮 Mini Game")
        st.write("Guess the secret number (1 to 10)")
        
        if 'target_number' not in st.session_state:
            st.session_state['target_number'] = random.randint(1, 10)
            
        guess = st.number_input("Your Guess:", min_value=1, max_value=10, step=1)
        
        if st.button("Submit Guess"):
            if guess == st.session_state['target_number']:
                st.balloons()
                st.success("🎉 You Win! Correct Guess!")
                # Reset game
                st.session_state['target_number'] = random.randint(1, 10) 
            elif guess < st.session_state['target_number']:
                st.warning("Too low! Try a higher number.")
            else:
                st.warning("Too high! Try a lower number.")
                
    st.divider()
    
    # Logout Button
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
