import json
import os
import streamlit as st
import hashlib

# Helper function to hash passwords for basic security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

st.set_page_config(page_title="Register", page_icon="⛩️", layout="centered")
st.markdown(
    """
    <style>
    #mainMenu, header {visibility: hidden}

    .block-container{
        max-width: 420px;
        border-radius: 20px;
    }
    .torri-icon{
        font-size: 40px;
        text-align: center;
        }
    .trainer-text{
        text-align: center;
        font-size: 20px;
        }
    .small{
        text-align: center;
        font-size: 10px;
        }
    .stForm{
        border: 1px solid black;
    }
    </style>

    """,
    unsafe_allow_html=True
)

st.markdown("""<div class="torri-icon">⛩️</div>""", unsafe_allow_html=True)
st.markdown("""<h3 class="trainer-text">JLPT N5 Trainer</h3>""", unsafe_allow_html=True)
st.markdown("""<p class="small">Learn japanese step by step</p>""", unsafe_allow_html=True)
st.markdown("""<h3 class="trainer-text">Create your account</h3>""", unsafe_allow_html=True)
st.markdown("""<p class="small">Signup to start your Japanese learning journey</p>""", unsafe_allow_html=True)

with st.form("register_form"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit_button = st.form_submit_button("Register", use_container_width=True)
    
    # Logic handles execution after the form submit button is pressed
    if submit_button:
        if not username or not email or not password:
            st.error("Please fill out all fields.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            FILE_PATH = "users.json"
            
            # 1. Load existing data if file exists, else start fresh
            if os.path.exists(FILE_PATH):
                with open(FILE_PATH, "r") as f:
                    try:
                        users_data = json.load(f)
                    except json.JSONDecodeError:
                        users_data = {}
            else:
                users_data = {}
            
            # 2. Check if username or email already exists
            if username in users_data:
                st.error("Username already exists!")
            else:
                # 3. Add new user data (hashing the password)
                users_data[username] = {
                    "email": email,
                    "password": hash_password(password)
                }
                
                # 4. Save updated dictionary back to the JSON file
                with open(FILE_PATH, "w") as f:
                    json.dump(users_data, f, indent=4)
                    
                st.success("Registration successful!")

st.markdown("""<p class="small">Already have an account? <a href="/login">Login here</a></p>""", unsafe_allow_html=True)
