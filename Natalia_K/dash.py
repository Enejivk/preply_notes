import streamlit as st

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="JLPT N5 Trainer - Dashboard",
    page_icon="⛩️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------
# SESSION STATE (swap this out for real data later)
# ------------------------------------------------------------------
if "user_name" not in st.session_state:
    st.session_state.user_name = "Riaan"
if "words_learned" not in st.session_state:
    st.session_state.words_learned = 0
if "words_total" not in st.session_state:
    st.session_state.words_total = 800
if "quizzes_taken" not in st.session_state:
    st.session_state.quizzes_taken = 0
if "quizzes_total" not in st.session_state:
    st.session_state.quizzes_total = 100
if "kanji_learned" not in st.session_state:
    st.session_state.kanji_learned = 0
if "kanji_total" not in st.session_state:
    st.session_state.kanji_total = 300
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

# ------------------------------------------------------------------
# CSS — recreates the purple/white look from the mock
# ------------------------------------------------------------------
st.markdown("""
<style>
    :root{
        --purple: #7C3AED;
        --purple-dark: #6D28D9;
        --purple-light: #F3EEFF;
        --text-dark: #1F2937;
        --text-gray: #6B7280;
        --border: #E5E7EB;
        --green: #16A34A;
        --orange: #EA580C;
    }

    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1.5rem; max-width: 1100px;}

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid var(--border);
    }
    section[data-testid="stSidebar"] .block-container {padding-top: 1.2rem;}

    .brand {
        display:flex; align-items:center; gap:.5rem;
        font-weight:700; font-size:1.05rem; color:var(--text-dark);
        margin-bottom: 1.5rem; padding-left:.25rem;
    }
    .brand span.icon {font-size:1.4rem;}

    div[data-testid="stSidebar"] button {
        width:100%;
        text-align:left;
        border:none;
        background:transparent;
        color:var(--text-gray);
        font-weight:500;
        padding:.55rem .8rem;
        border-radius:10px;
        margin-bottom:.25rem;
    }
    div[data-testid="stSidebar"] button:hover {
        background:var(--purple-light);
        color:var(--purple-dark);
    }
    div[data-testid="stSidebar"] button p {font-size:.92rem;}

    .nav-active button {
        background:var(--purple-light) !important;
        color:var(--purple-dark) !important;
        font-weight:600 !important;
    }

    /* ---------- Top bar ---------- */
    .topbar {
        display:flex; justify-content:flex-end; align-items:center;
        gap:1rem; margin-bottom:1.2rem;
    }
    .avatar {
        width:34px; height:34px; border-radius:50%;
        background:var(--purple); color:white;
        display:flex; align-items:center; justify-content:center;
        font-weight:600; font-size:.85rem;
    }
    .user-chip {display:flex; align-items:center; gap:.5rem; font-weight:600; color:var(--text-dark);}
    .bell {font-size:1.2rem; color:var(--text-gray);}

    /* ---------- Welcome ---------- */
    .welcome-title {font-size:1.7rem; font-weight:700; color:var(--text-dark); margin-bottom:.1rem;}
    .welcome-title .name {color:var(--purple);}
    .welcome-sub {color:var(--text-gray); margin-bottom:1.4rem;}

    /* ---------- Progress cards ---------- */
    .stat-card {
        background:white; border:1px solid var(--border); border-radius:14px;
        padding:1.1rem 1.2rem; height:100%;
    }
    .stat-icon {
        width:38px; height:38px; border-radius:10px;
        display:flex; align-items:center; justify-content:center;
        font-size:1.1rem; margin-bottom:.6rem;
    }
    .stat-value {font-size:1.6rem; font-weight:700; color:var(--text-dark); line-height:1;}
    .stat-label {color:var(--text-gray); font-size:.85rem; margin:.3rem 0 .7rem 0;}
    .progress-track {
        width:100%; height:6px; background:#F0F0F3; border-radius:6px; overflow:hidden; margin-bottom:.4rem;
    }
    .progress-fill {height:100%; border-radius:6px;}
    .stat-fraction {font-size:.78rem; color:var(--text-gray);}

    /* ---------- Section header ---------- */
    .section-title {font-size:1.15rem; font-weight:700; color:var(--text-dark); margin: 1.6rem 0 .8rem 0;}

    /* ---------- Practice cards ---------- */
    .practice-card {
        background:var(--purple-light); border-radius:14px; padding:1.2rem;
        display:flex; align-items:flex-start; gap:.9rem; height:100%;
    }
    .practice-card.blue {background:#EFF6FF;}
    .practice-icon {
        width:42px; height:42px; min-width:42px; border-radius:10px; background:white;
        display:flex; align-items:center; justify-content:center; font-size:1.3rem;
    }
    .practice-heading {display:flex; align-items:center; gap:.4rem; font-weight:700; color:var(--text-dark); font-size:1.02rem;}
    .practice-desc {color:var(--text-gray); font-size:.85rem; margin-top:.15rem;}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# TOP BAR
# ------------------------------------------------------------------
top_l, top_r = st.columns([6, 1])
with top_r:
    initial = st.session_state.user_name[0].upper()
    st.markdown(f"""
    <div class="topbar">
        <span class="bell">🔔</span>
        <div class="user-chip">
            <div class="avatar">{initial}</div>
            {st.session_state.user_name} ▾
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------
# WELCOME
# ------------------------------------------------------------------
st.markdown(f"""
<div class="welcome-title">Welcome back, <span class="name">{st.session_state.user_name}</span>! 👋</div>
<div class="welcome-sub">Let's continue your Japanese learning.</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# PROGRESS SECTION
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Your Progress</div>', unsafe_allow_html=True)

def stat_card(icon, icon_bg, value, label, current, total, bar_color):
    pct = int((current / total) * 100) if total else 0
    return f"""
    <div class="stat-card">
        <div class="stat-icon" style="background:{icon_bg};">{icon}</div>
        <div class="stat-value">{value}</div>
        <div class="stat-label">{label}</div>
        <div class="progress-track">
            <div class="progress-fill" style="width:{pct}%; background:{bar_color};"></div>
        </div>
        <div class="stat-fraction">{current} / {total}</div>
    </div>
    """

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(stat_card("📖", "#F3EEFF", st.session_state.words_learned, "Words Learned",
                           st.session_state.words_learned, st.session_state.words_total, "#7C3AED"),
                unsafe_allow_html=True)
with c2:
    st.markdown(stat_card("✅", "#E7F8EC", st.session_state.quizzes_taken, "Quizzes Taken",
                           st.session_state.quizzes_taken, st.session_state.quizzes_total, "#16A34A"),
                unsafe_allow_html=True)
with c3:
    st.markdown(stat_card("漢", "#FDECE1", st.session_state.kanji_learned, "Kanji Learned",
                           st.session_state.kanji_learned, st.session_state.kanji_total, "#EA580C"),
                unsafe_allow_html=True)

# ------------------------------------------------------------------
# PRACTICE SECTION
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Practice</div>', unsafe_allow_html=True)

p1, p2 = st.columns(2)
with p1:
    st.markdown("""
    <div class="practice-card">
        <div class="practice-icon">📇</div>
        <div>
            <div class="practice-heading">Flashcards →</div>
            <div class="practice-desc">Learn new words with flashcards.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Flashcards", key="open_flashcards", use_container_width=True):
        st.session_state.active_page = "Flashcards"

with p2:
    st.markdown("""
    <div class="practice-card blue">
        <div class="practice-icon">❓</div>
        <div>
            <div class="practice-heading">Take a Quiz →</div>
            <div class="practice-desc">Test your knowledge with a quiz.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Quiz", key="open_quiz", use_container_width=True):
        st.session_state.active_page = "Quiz"
