import streamlit as st
import random

# --- Page Configuration ---
st.set_page_config(page_title="Tasnim Ahmad - Project", layout="wide")

# --- Custom CSS for Professional Look & Mobile-Style Calculator ---
st.markdown("""
<style>
    .main {
        background-color: #F0F2F6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #E65100;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #BF360C;
        color: white;
    }
    .login-header {
        text-align: center;
        color: #E65100;
        font-size: 40px;
        font-weight: bold;
    }
    .calc-btn {
        height: 60px !important;
        font-size: 20px !important;
        margin: 2px;
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
if 'calc_expression' not in st.session_state:
    st.session_state['calc_expression'] = ""

# --- Login Logic ---
if not st.session_state['logged_in']:
    st.markdown("<div class='login-header'>Tasnim Ahmad</div>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Professional Login Portal</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.session_state['account_locked']:
            st.error("Account Locked: Too many failed attempts. Please contact administrator.")
        else:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
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
                        st.warning(f"Invalid credentials. {remaining} attempts remaining.")

# --- Dashboard Logic ---
else:
    # Sidebar for Professional Navigation (3-line menu style)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "Calculator", "Rock Paper Scissors"])
    
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    # 1. Home Page (Greetings)
    if page == "Home":
        st.title("User Dashboard")
        st.write("Welcome to the professional management system.")
        st.divider()
        
        name_input = st.text_input("Enter your name")
        if st.button("Enter"):
            if name_input:
                st.success(f"Welcome, {name_input}! You are looking exceptionally amazing today! ✨
Take care of yourself 🤍")
            else:
                st.info("Please provide a name to receive a greeting.")

    # 2. Mobile-Style Calculator
    elif page == "Calculator":
        st.title("Calculator")
        st.write("Professional Calculation Tool")
        
        # Display Screen
        st.text_input("Screen", value=st.session_state['calc_expression'], key="display", disabled=True)
        
        # Calculator Buttons Grid
        btns = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in btns:
            cols = st.columns(4)
            for i, char in enumerate(row):
                if cols[i].button(char, key=f"btn_{char}"):
                    if char == 'C':
                        st.session_state['calc_expression'] = ""
                    elif char == '=':
                        try:
                            st.session_state['calc_expression'] = str(eval(st.session_state['calc_expression']))
                        except:
                            st.session_state['calc_expression'] = "Error"
                    else:
                        st.session_state['calc_expression'] += char
                    st.rerun()

    # 3. Rock Paper Scissors Game
    elif page == "Rock Paper Scissors":
        st.title("Rock Paper Scissors")
        st.write("Choose your move to play against the computer.")
        
        user_choice = st.selectbox("Select Choice", ["Rock", "Paper", "Scissors"])
        if st.button("Play"):
            options = ["Rock", "Paper", "Scissors"]
            computer_choice = random.choice(options)
            st.write(f"You chose: {user_choice}")
            st.write(f"Computer chose: {computer_choice}")
            
            if user_choice == computer_choice:
                st.info("It is a Tie!")
            elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                 (user_choice == "Paper" and computer_choice == "Rock") or \
                 (user_choice == "Scissors" and computer_choice == "Paper"):
                st.success("Result: You Win!")
            else:
                st.error("Result: Computer Wins!")
