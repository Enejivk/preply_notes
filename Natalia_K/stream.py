import streamlit as st

st.set_page_config(page_title="JLPT N5 Trainer", page_icon="⛩️", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}

    .stApp {
        background: #f4f5f7;
    }

    /* Turn the actual content block into the white card */
    .block-container {
        max-width: 420px;
        margin: 40px auto 0 auto;
        background: #ffffff !important;
        border-radius: 20px;
        padding: 44px 40px 32px 40px !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.06);
    }

    .torii-icon {
        text-align: center;
        font-size: 40px;
        margin-bottom: 6px;
    }

    .app-title {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 2px;
    }

    .app-subtitle {
        text-align: center;
        font-size: 13px;
        color: #9a9a9a;
        margin-bottom: 22px;
    }

    hr.divider {
        border: none;
        border-top: 1px solid #eee;
        margin: 0 0 22px 0;
    }

    .create-title {
        text-align: center;
        font-size: 19px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 2px;
    }

    .create-subtitle {
        text-align: center;
        font-size: 13px;
        color: #9a9a9a;
        margin-bottom: 22px;
    }

    /* Force labels to plain dark text, not Streamlit's theme accent color */
    .stTextInput label p {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #333333 !important;
    }

    /* Force light input fields regardless of system/browser dark mode */
    .stTextInput input {
        background-color: #fafafa !important;
        color: #1a1a1a !important;
        border: 1px solid #e3e3e8 !important;
        border-radius: 10px !important;
        font-size: 14px !important;
    }

    .stTextInput input::placeholder {
        color: #b0b0b0 !important;
    }

    div[data-baseweb="base-input"] {
        background-color: #fafafa !important;
        border-radius: 10px !important;
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #7b3fe4, #a259e6);
        color: white !important;
        font-weight: 600;
        font-size: 15px;
        border: none;
        border-radius: 10px;
        padding: 12px 0;
        margin-top: 8px;
    }

    div.stButton > button:hover {
        opacity: 0.92;
    }

    div.stButton > button p {
        color: white !important;
    }

    .login-link {
        text-align: center;
        font-size: 13px;
        color: #666;
        margin-top: 18px;
    }

    .login-link a {
        color: #7b3fe4;
        font-weight: 600;
        text-decoration: none;
    }

    .footer-note {
        text-align: center;
        font-size: 11px;
        color: #b5b5b5;
        margin-top: 28px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- PAGE CONTENT ----------
st.markdown('<div class="torii-icon">⛩️</div>', unsafe_allow_html=True)
st.markdown('<div class="app-title">JLPT N5 Trainer</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Learn Japanese. Step by step.</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown('<div class="create-title">Create your account</div>', unsafe_allow_html=True)
st.markdown('<div class="create-subtitle">Sign up to start your Japanese learning journey.</div>', unsafe_allow_html=True)

full_name = st.text_input("Full Name", placeholder="Enter your full name")
email = st.text_input("Email", placeholder="Enter your email")
password = st.text_input("Password", placeholder="Create a password", type="password")

if st.button("Sign Up", use_container_width=True):
    if not full_name or not email or not password:
        st.warning("Please fill in all fields.")
    else:
        st.success(f"Account created for {full_name}!")

st.markdown('<div class="login-link">Already have an account? <a href="#">Log in</a></div>', unsafe_allow_html=True)
st.markdown('<div class="footer-note">© 2025 JLPT N5 Trainer</div>', unsafe_allow_html=True)
