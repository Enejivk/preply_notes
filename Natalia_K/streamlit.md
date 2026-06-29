# 🗻 JLPT N5 Trainer
## A 5-Class Course: From Zero to a Working Streamlit App

*Instructor Notes & Lesson Plan*
For complete beginners · 5 sessions, ~3.5 hours each

> **What students build**
>
> A real, working multi-page website (built with Streamlit) that teaches Japanese vocabulary for the JLPT N5 level: a Home dashboard showing progress, a Sign Up / Login system with saved accounts, a Flashcards page with real vocabulary, and a multiple-choice Quiz — all backed by their own data files and pushed to their own GitHub repository.

---

# Course Overview

## Who this is for

This lesson plan assumes complete beginners: nobody in the room has written code before. Every Python concept used later in the course is taught from scratch, in the class where it's first needed, rather than front-loaded as a separate "learn Python first" block. This keeps motivation high — every new idea is immediately used to build something visible.

## How the 5 classes are structured

| Class | Theme | What happens |
|-------|-------|---------------|
| Class 1 | Foundations | Install Python, VS Code, Git. Just enough Python (variables, f-strings, if/else, lists, dictionaries, functions). First Streamlit app: a home page with a title and two buttons. (Covers original Chapter 1) |
| Class 2 | Structure | Multi-page apps using the pages/ folder convention. Real navigation with st.switch_page. A dashboard UI using st.columns and st.metric. First push to GitHub. (Covers Chapters 2-3) |
| Class 3 | Data & Identity | Reading/writing JSON files. Why and how to hash passwords. The single most important concept of the course: st.session_state. Full sign up / login / logout system. (Covers Chapters 4-5) |
| Class 4 | Real Feature #1 | Designing vocabulary data. Building the Flashcards page: stepping through a list, showing/hiding answers, saving "words learned" to the logged-in user's account. (Covers Chapters 6-8) |
| Class 5 | Real Feature #2 + Polish | Generating multiple-choice quiz questions from vocabulary data. Scoring and a progress bar. Wiring the dashboard's numbers to real saved data. A CSS pass to visually approach the original design. Final push. (Covers Chapters 9-12) |

## Teaching principles used throughout

- **Type it, run it, break it, fix it.** Every new concept is demonstrated with a tiny, throwaway example before it's used in the real project. Beginners learn faster from a 3-line demo they fully understand than from reading 30 lines of "real" code.
- **Name the mental models explicitly.** Two ideas quietly do most of the conceptual work in this course: "Streamlit reruns your whole script on every interaction" and "session_state is the one thing that survives those reruns." Both are introduced with a dedicated, deliberately simple standalone demo (a play that restarts each clap; a click counter) before being applied to real features. Refer back to these analogies whenever a new feature relies on them.
- **Recap, every single class, out loud.** Each class opens with 2-3 cold-call questions about the previous class. This catches confusion early and costs almost no time.
- **Checkpoints, not just content.** Each class ends with a concrete, observable checklist — not "we covered X" but "can every student's app actually do X right now." Don't move to the next class's material until checkpoints are met; trim polish time instead.
- **Errors are part of the lesson plan.** Each class's most common error is called out in advance in an instructor callout box, so it can be handled calmly and quickly rather than derailing the room.

## What you need to prepare before Class 1

- Every student's laptop can install software (admin rights) — confirm this before day one, not during it.
- A stable shared wifi network, plus an offline installer backup for Python and VS Code in case of slow downloads.
- Students should create a free GitHub account before Class 2 (mentioned again at the end of Class 1).
- This document, the original build-guide poster, and the 4-screen UI mockup are useful to share with students directly as a "this is what we're building" reference on day one.

## How to use this document

Each class below is written as a run sheet: a timing table, then section-by-section content with the exact talking points, code to type, and common errors to expect, roughly in the order you'd actually deliver them live. Code blocks are written to be typed (or projected and copy-pasted) directly into each student's project. Blockquote boxes flag either a teaching tip, a common trap, or a discussion point worth pausing on.

---


# CLASS 1

### Python Basics + Your First Streamlit App

> **Class goal**
>
> By the end of today, every student has Python and VS Code installed, understands the handful of Python concepts we actually need, and has a working two-button Streamlit home page pushed to GitHub.

## Before class: instructor checklist

- Confirm every student can install software on their laptop (admin rights). Chase this up the day before, not in class.
- Have a USB stick or shared drive link with offline installers for Python and VS Code in case of slow wifi.
- Create a shared GitHub Organization (or have students ready to create personal accounts) before class so Class 2's push step doesn't stall.
- Print or share the project poster (chapter overview) so students can see the destination on day one.

## Timing overview (3.5 hours, including breaks)

| Time | Segment | What happens |
|------|---------|--------------|
| 0:00 | Welcome + demo | Show the finished app (or the mockup screenshots). Set expectations: 'by the end of 5 classes, you will have built this yourself.' |
| 0:15 | Install & setup | Python, VS Code, terminal orientation, first 'Hello World' |
| 0:50 | Python crash course | Variables, strings, f-strings, if/else, lists, functions — only what we need |
| 1:30 | Break | 15 minutes |
| 1:45 | What is Streamlit? | Install Streamlit, run the demo app, explain the rerun model |
| 2:10 | Build Chapter 1 | Students type the home page code themselves, line by line |
| 2:50 | Git & GitHub basics | Install Git, init repo, first commit |
| 3:15 | Wrap-up + checkpoint | Everyone's app running, answer questions, preview Class 2 |

---

## 1. Why are we doing this? (5 min talking point)

Open with the mockup screenshots or the finished app running live. Say explicitly: 'You do not need to be a programmer already. By the end of five classes, you will have a real, working website that you built, that you can show people, that helps people learn Japanese.' Beginners need to hear this before anything else — it sets the emotional frame for tolerating early confusion.

## 2. Installing Python

Use the official installer, not a package manager, for beginners — fewer ways to get confused.

- **Windows:** go to python.org/downloads, download the latest installer, and — this matters — check the box that says 'Add Python to PATH' before clicking Install.
- **Mac:** go to python.org/downloads, download the macOS installer, run it normally.
- **Verify it worked:** open a terminal (Command Prompt on Windows, Terminal on Mac) and type:

```bash
python --version
```

They should see something like Python 3.12.x. If they see an error, the most common cause on Windows is forgetting the 'Add to PATH' checkbox — reinstall and check it.

## 3. Installing VS Code

Download from code.visualstudio.com and install with default options. Once installed, open VS Code and install the official 'Python' extension (search the Extensions icon on the left sidebar for 'Python', install the one published by Microsoft).

> **Teaching tip**
>
> Spend 2 minutes just touring the VS Code window: the file explorer on the left, the editor in the middle, and the terminal at the bottom (View > Terminal, or Ctrl+` / Cmd+`). Beginners get lost in unfamiliar software before they ever get lost in code — orient them first.

## 4. Create the project folder

Have every student create one folder that will hold the entire project for all 5 classes. Keeping this consistent now avoids painful 'I can't find my files' moments in Class 3.

1. Create a folder on the Desktop (or Documents) named exactly: jlpt_n5_trainer
2. In VS Code: File > Open Folder > select that folder.
3. Open the built-in terminal (View > Terminal). It should already be 'inside' that folder.

## 5. Python crash course — only what we need

This is not a full Python course. We are teaching exactly the concepts the project will use, in the order it will use them. Have students create a scratch file called practice.py for all of this, and run it with the green Run button or by typing python practice.py in the terminal.

### 5.1 Printing and variables

```python
name = "Riaan"
age = 21

print("Hello!")
print(name)
print(age)
```

Explain: a variable is a labelled box that stores a value. print() shows something in the terminal. Strings (text) go in quotes; numbers don't.

### 5.2 f-strings (we use these constantly)

```python
name = "Riaan"
print(f"Welcome back, {name}!")
```

The f before the quote lets you drop a variable straight into a sentence using curly braces. This single pattern shows up everywhere in the JLPT app — e.g. showing the logged-in user's name, or '1 / 20' on a flashcard.

### 5.3 if / else

```python
logged_in = False

if logged_in:
    print("Welcome back!")
else:
    print("Please log in.")
```

> **Common beginner trap**
>
> Python uses indentation (spaces) instead of curly braces to show what's 'inside' the if. Tell students: everything indented under the if belongs to the if. Getting the indentation wrong is the single most common error they will hit all course — name it now so it's familiar later.

### 5.4 Lists

```python
words = ["school", "book", "water"]
print(words[0])   # school — lists start counting at 0
print(len(words)) # 3 — how many items
```

This is the foundation for flashcards and quiz questions in Classes 4 and 5 — a list of vocabulary words to flip through.

### 5.5 Dictionaries

```python
card = {"kanji": "学校", "romaji": "gakkou", "english": "school"}
print(card["english"])  # school
```

A dictionary stores labelled pieces of information together, like a small form. Every flashcard and every user account will be a dictionary like this.

### 5.6 Functions

```python
def greet(name):
    return f"Welcome back, {name}!"

message = greet("Riaan")
print(message)
```

A function is a reusable recipe: give it ingredients (the inputs in brackets), it hands back a result. We will write functions like load_users() and hash_password() that do one specific job each.

## 6. BREAK (15 minutes)

## 7. What is Streamlit?

Explain in plain language: 'Streamlit is a tool that turns ordinary Python code into a website. You write Python from top to bottom, like a recipe, and Streamlit draws it on a webpage automatically. No HTML, no JavaScript needed.'

### Installing Streamlit

In the VS Code terminal, inside the project folder:

```bash
pip install streamlit
```

If pip is not recognized, try pip3 install streamlit instead — explain that on some systems Python 3's tools are named with a '3'.

### The most important mental model: Streamlit reruns the whole script

> **Teach this now, even though it feels early**
>
> Every time someone clicks a button or types something, Streamlit runs your entire .py file again from the top, not just the part near the button.
>
> This feels strange at first, but it explains almost every confusing thing that happens later, especially session state in Class 3.
>
> A good analogy: imagine a play that restarts from the very first line every time the audience claps, except a few props (session state) are remembered between performances.

## 8. Build Chapter 1: Your First Streamlit App

Goal: a home page with a title, a welcome message, and two buttons (Flashcards, Take a Quiz).

### Step 1 — Create app.py

Inside the jlpt_n5_trainer folder, create a new file named exactly app.py (File > New File in VS Code, save it with that name).

### Step 2 — Type this code

```python
import streamlit as st

st.set_page_config(
    page_title="JLPT N5 Trainer",
    page_icon="🗻",
    layout="centered"
)

st.title("🗻 JLPT N5 Trainer")
st.write("Welcome! Let's learn Japanese step by step.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("📖 Flashcards", use_container_width=True):
        st.info("Flashcards coming soon!")

with col2:
    if st.button("❓ Take a Quiz", use_container_width=True):
        st.info("Quiz coming soon!")
```

Walk through it line by line before running anything:

- import streamlit as st — brings in the Streamlit toolkit and nicknames it st, so every command starts with st.
- st.set_page_config(...) — sets the browser tab title, the little icon, and the page width. Must be the very first Streamlit command in the file.
- st.title(...) and st.write(...) — put text on the page. title is big and bold; write is normal text.
- st.columns(2) — splits the page into 2 side-by-side sections, so the buttons sit next to each other instead of stacking.
- st.button(...) — draws a button. The if around it means 'only do the following if this button was just clicked.'
- st.info(...) — shows a small blue message box.

### Step 3 — Run it

```bash
streamlit run app.py
```

This should open a browser tab automatically at a local address (something like http://localhost:8501). If it doesn't open automatically, the terminal prints the link to click.

> **If something goes wrong**
>
> The two most common Class 1 errors: (1) 'streamlit: command not found' — usually means pip installed it somewhere not on PATH; try python -m streamlit run app.py instead. (2) IndentationError — check that the lines under 'with col1:' are indented consistently with spaces, not a mix of tabs and spaces.

### Step 4 — Make it their own

Have students change the welcome message and try a different page_icon emoji, then rerun. This small act of customizing — and seeing the page update — is what makes the rerun model click for beginners.

## 9. Git & GitHub basics

We introduce git today but don't push to GitHub remotely until Class 2, once there's more to show. Today's goal is just: install git, initialize a repository, make a first commit, understand what a commit is.

### Install Git

- Windows: download from git-scm.com, install with default options.
- Mac: open Terminal and type git --version — macOS will usually prompt to install developer tools if it's missing.

### Initialize the project

```bash
git init
git add .
git commit -m "Chapter 1: First Streamlit app"
```

Explain with an analogy: git init starts tracking the folder like a save-game system. git add . stages every changed file ('these are the changes I want to save'). git commit -m "..." actually takes the snapshot, with a short note describing what changed.

> **First-time git setup**
>
> If this is anyone's first time using git on this machine, they may be prompted to set their identity first:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 10. End-of-class checkpoint

Every student should be able to demonstrate, before leaving:

- streamlit run app.py opens a browser page with the JLPT N5 Trainer title.
- Clicking either button shows a small info message.
- git log shows at least one commit.

> **Homework (optional, light)**
>
> Encourage students to try changing st.info messages to something personalized, and to make sure their VS Code, Python, and git installs work without instructor help — so Class 2 can start moving immediately.

---

# CLASS 2

### Multiple Pages + Dashboard UI

> **Class goal**
>
> By the end of today, every student has a real multi-page app — Home, Flashcards, Quiz — with working sidebar navigation, a dashboard showing progress stats, and their code pushed to GitHub for the first time.

## Before class: instructor checklist

- Confirm each student has a GitHub account created (github.com, free) and remembers their username/password.
- Recap sheet ready: last class's app.py code, in case anyone's setup broke between sessions.

## Timing overview (3.5 hours)

| Time | Segment | What happens |
|------|---------|--------------|
| 0:00 | Recap + recap quiz | Quick verbal review of variables, f-strings, if/else, the rerun model |
| 0:20 | Multi-page apps | Explain the pages/ folder convention, build flashcards.py and quiz.py stubs |
| 1:00 | Navigation | st.switch_page, sidebar behavior, testing navigation flow |
| 1:30 | Break | 15 minutes |
| 1:45 | Dashboard UI (Chapter 3) | st.columns, st.metric, st.container — build the progress dashboard |
| 2:30 | GitHub: first push | Create a GitHub repo, connect it, push code for real |
| 3:00 | Practice + personalize | Students adjust colors, icons, text to make it their own |
| 3:20 | Checkpoint + preview Class 3 | Confirm everyone's navigation + dashboard works |

---

## 1. Recap (10–15 min, verbal, no slides needed)

Ask students to answer out loud, cold-call style, to surface anyone who's lost before new material piles on:

- What does an f-string let you do?
- What's different about code that's indented under an if?
- What happens to your whole Python file when you click a button in Streamlit?

> **If the room is shaky on the rerun model**
>
> Don't move on yet. Re-run last class's app.py live, click a button, and explicitly say: 'See — the whole file just ran again, top to bottom. That's why the title reprinted.' This is the idea multi-page apps and later session state are built on.

## 2. Multi-page apps: the pages/ folder convention

Explain: Streamlit has a built-in rule — any .py file you put inside a folder named pages will automatically appear as its own page, with a sidebar link, with zero extra setup. This is the entire mechanism behind multi-page apps.

### Step 1 — Create the pages folder

In VS Code's file explorer, right-click the jlpt_n5_trainer project folder > New Folder > name it exactly: pages

### Step 2 — Create two files inside pages

- pages/flashcards.py
- pages/quiz.py

### Step 3 — Turn app.py into the Home page only

Replace the entire contents of app.py with this (we will add the dashboard back in shortly, but first let's prove navigation works):

```python
import streamlit as st

st.set_page_config(
    page_title="JLPT N5 Trainer",
    page_icon="🗻",
    layout="wide"
)

st.title("🗻 JLPT N5 Trainer")
st.write("Welcome! Choose an option from the sidebar.")
st.success("Use the sidebar to navigate.")
```

### Step 4 — Add code to pages/flashcards.py

```python
import streamlit as st

st.title("📖 Flashcards")
st.write("This is the Flashcards page.")
```

### Step 5 — Add code to pages/quiz.py

```python
import streamlit as st

st.title("❓ Take a Quiz")
st.write("This is the Quiz page.")
```

### Step 6 — Run and look at the sidebar

```bash
streamlit run app.py
```

Point out: a sidebar appeared automatically on the left, listing 'app', 'flashcards', and 'quiz' as clickable links — nobody wrote any sidebar code. This is Streamlit reading the pages/ folder.

> **Naming note**
>
> Streamlit shows the page names based on the filenames. Capitalization and underscores in filenames affect what's displayed (e.g. 01_Flashcards.py would show as '01 Flashcards'). For this project we're keeping filenames simple and lowercase, and we'll control the displayed titles ourselves using st.title() inside each page instead of relying on the filename.

## 3. Making the buttons actually navigate

Right now the Home page buttons (from Class 1) just show info messages. Let's make them jump to the real pages using st.switch_page.

Replace app.py with:

```python
import streamlit as st

st.set_page_config(
    page_title="JLPT N5 Trainer",
    page_icon="🗻",
    layout="wide"
)

st.title("🗻 JLPT N5 Trainer")
st.write("Welcome! Choose an option from the sidebar.")
st.success("Use the sidebar to navigate.")

col1, col2 = st.columns(2)

with col1:
    if st.button("📖 Flashcards", use_container_width=True):
        st.switch_page("pages/flashcards.py")

with col2:
    if st.button("❓ Take a Quiz", use_container_width=True):
        st.switch_page("pages/quiz.py")
```

st.switch_page("pages/flashcards.py") tells Streamlit: 'stop showing this page, immediately show that one instead.' The path must match the real file path from the project's root folder.

## 4. BREAK (15 minutes)

## 5. Build Chapter 3: the dashboard

Goal: turn the Home page into a real dashboard with progress stats, using st.columns and st.metric — the two workhorse layout tools for the rest of the course.

Replace the content of app.py with:

```python
import streamlit as st

st.set_page_config(
    page_title="JLPT N5 Trainer",
    page_icon="🗻",
    layout="wide"
)

st.title("🗻 JLPT N5 Trainer")
st.write("Welcome back! Let's continue learning.")

st.markdown("### Your Progress")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📖 Words Learned", "0 / 800", "0%")

with col2:
    st.metric("✅ Quizzes Taken", "0 / 100", "0%")

with col3:
    st.metric("漢 Kanji Learned", "0 / 300", "0%")

st.markdown("---")
st.markdown("### Practice")

c1, c2 = st.columns(2)

with c1:
    if st.button("📖 Flashcards", use_container_width=True):
        st.switch_page("pages/flashcards.py")

with c2:
    if st.button("❓ Take a Quiz", use_container_width=True):
        st.switch_page("pages/quiz.py")
```

> **Why st.metric()**
>
> st.metric() is built specifically to show a number, a label, and an optional small delta (the '0%' here) in a clean boxed layout — it's the natural tool any time we display a statistic, which is most of this app's dashboard.

Run it and compare against the mockup's Dashboard screen. The numbers are hardcoded zeros right now — Class 4 and 5 will wire these up to real data.

## 6. GitHub: pushing code for the first time

Last class we made local commits. Today we connect the project to a real GitHub repository so the code is backed up online and shareable.

### Step 1 — Create the repository on GitHub

1. Go to github.com, log in, click the + icon top-right > New repository.
2. Name it jlpt-n5-trainer. Leave it Public (or Private, student's choice). Do NOT initialize with a README — we already have local files.
3. Click Create repository. GitHub will show a page with setup commands — keep that tab open.

### Step 2 — Connect and push

Back in the VS Code terminal:

```bash
git remote add origin https://github.com/YOUR-USERNAME/jlpt-n5-trainer.git
git branch -M main
git add .
git commit -m "Chapter 3: Added dashboard UI"
git push -u origin main
```

Replace YOUR-USERNAME with their actual GitHub username — this is the most common typo, walk the room and check.

> **If push asks for a password and rejects it**
>
> GitHub no longer accepts account passwords for git operations. Students will need to either sign in via a browser popup (VS Code's Git panel can trigger this) or set up a Personal Access Token. For a beginner class, the simplest fix: use VS Code's built-in Source Control panel (the icon in the left sidebar) and let it handle authentication through a browser login popup instead of the raw terminal command.

Once it succeeds, have students refresh their GitHub repo page in the browser and see their files there. This is a genuinely motivating moment for beginners — point it out.

## 7. Practice + personalize (20 min)

Let students freely adjust: page_icon emoji, the welcome text, the target numbers in st.metric (800 words, 100 quizzes, 300 kanji — these can be whatever they like). The goal is ownership, not new concepts.

## 8. End-of-class checkpoint

Every student should be able to demonstrate:

- A sidebar with Home / flashcards / quiz that actually navigates between pages.
- A dashboard on the home page showing 3 metric boxes.
- Their code visible on github.com under their own account.

> **Preview Class 3**
>
> Next class is the biggest conceptual jump: saving data to files, and Streamlit's session_state. Tell students tonight's idea to chew on: 'Right now, if you close the browser tab, the app forgets everything. Next class we fix that two ways — saving to a file, and remembering things during a session.'

---

# CLASS 3

### Saving Data, Login & Signup, Session State

> **Class goal**
>
> By the end of today, every student's app can register new users, save them permanently to a file, log them back in, and remember who's logged in while they click around the app. This is the conceptual heart of the whole course — go slower here than anywhere else.

> **Instructor note: this is the hardest class**
>
> Sessions state and password hashing are the first genuinely new ideas (not just new syntax) students meet. Budget extra time here even if it means trimming polish later. Do the standalone session_state counter demo before touching login — do not skip it to save time.

## Timing overview (3.5 hours)

| Time | Segment | What happens |
|------|---------|--------------|
| 0:00 | Recap | Multi-page navigation, st.metric, what a repo/push is |
| 0:15 | Files & JSON | Reading/writing files in Python, what JSON looks like and why we use it |
| 0:45 | Password hashing | Why we never store plain passwords; hashlib in 10 lines |
| 1:05 | Build auth.py + users.json | load_users, save_users, hash_password |
| 1:35 | Break | 15 minutes |
| 1:50 | session_state standalone demo | A tiny counter app — the single most important demo of the course |
| 2:15 | Build login.py | Sign up tab + login tab, wired to auth.py |
| 2:55 | Wire login into app.py | Logged-out vs logged-in views, sidebar logout |
| 3:25 | Checkpoint | Full signup → logout → login cycle works for everyone |

---

## 1. Recap (10 min)

- What file/folder makes a new page appear automatically?
- What Streamlit function jumps the user to another page?
- What does git push actually do?

## 2. Files and JSON

Explain: so far, everything our app 'remembers' disappears the moment we stop the program, because it only lives in the computer's memory. To remember things permanently — like a list of registered users — we need to save them to a file on disk.

### What is JSON?

JSON (JavaScript Object Notation) is just a text format for storing lists and dictionaries — exactly the Python data structures from Class 1 — in a way any program can read back later. Show this on screen:

```json
[
  {"name": "Riaan", "email": "riaan@example.com"},
  {"name": "Aisha", "email": "aisha@example.com"}
]
```

Point out: that's a list (square brackets) of dictionaries (curly brackets) — students already know both of these from Class 1. JSON is just Python's own data shapes, saved as plain text.

### Reading and writing JSON in Python

```python
import json

data = [{"name": "Riaan"}]

# Writing to a file
with open("test.json", "w") as f:
    json.dump(data, f, indent=2)

# Reading from a file
with open("test.json", "r") as f:
    loaded = json.load(f)

print(loaded)
```

Have students run this as a quick scratch exercise (in practice.py) and then open test.json in VS Code to see the saved file with their own eyes before moving to the real project.

## 3. Why we hash passwords

Ask the room: 'If we save passwords directly into users.json as plain text, and someone opens that file, what happens?' Let them arrive at: anyone who sees the file sees everyone's real password. This is the motivation for hashing.

> **The idea of hashing, in one paragraph**
>
> A hash function takes any text and turns it into a fixed-length scramble of letters and numbers that cannot be reversed back into the original text.
>
> The same input always produces the same hash, so we can still check 'does this password match?' — we just compare hashes instead of comparing real passwords.
>
> We are not building bank-grade security in this course; we are teaching the habit and the reasoning. Mention this honestly to the class.

```python
import hashlib

password = "mypassword123"
hashed = hashlib.sha256(password.encode()).hexdigest()
print(hashed)
# always the same scrambled string for this exact password
```

## 4. Build the data folder and users.json

1. In the project folder, create a new folder named data.
2. Inside data, create a file named users.json with just this content:

```json
[]
```

That's an empty list — no users yet. Our code will add to this file as people sign up.

## 5. Build utils/auth.py

1. Create a folder named utils.
2. Inside it, create auth.py with this code:

```python
import json
import os
import hashlib

USERS_FILE = "data/users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

Walk through each function as a 'recipe with one job':

- load_users() — opens users.json and hands back the list of users. If the file doesn't exist yet, hands back an empty list instead of crashing.
- save_users(users) — takes a list of users and writes it to users.json, overwriting what was there.
- hash_password(password) — turns a plain password into its scrambled hash.

> **Why this lives in its own file**
>
> Putting these in utils/auth.py instead of directly inside login.py means any page that needs to check users — now or in a future chapter — can reuse the exact same functions instead of copy-pasting code. This is the first time the course introduces 'organizing code across files,' which is worth naming explicitly.

## 6. BREAK (15 minutes)

## 7. The most important demo of the course: session_state

Do not skip this. Before touching login.py, build this tiny standalone app together, live, in a throwaway file (e.g. scratch_session.py):

```python
import streamlit as st

st.title("Counter Demo")

if "count" not in st.session_state:
    st.session_state["count"] = 0

st.write(f"Current count: {st.session_state['count']}")

if st.button("Add one"):
    st.session_state["count"] += 1
```

Run it. Click the button several times in front of the class and ask: 'Remember — every click reruns the whole script from the top. So why didn't count reset back to 0 on every click?'

> **The explanation**
>
> st.session_state is a special dictionary that Streamlit does NOT clear when it reruns the script — it survives across reruns, for as long as that browser tab/session stays open.
>
> The line if "count" not in st.session_state only sets it to 0 the very first time — on every later rerun, that line sees it's already there and leaves it alone.
>
> This is exactly the 'props the actors remember between performances' from the Class 1 play analogy.

This is precisely the mechanism that will remember who is logged in. Make that connection explicit before moving on.

## 8. Build pages/login.py

Goal: one page that handles both sign up and login, using tabs.

```python
import streamlit as st
from utils.auth import load_users, save_users, hash_password

st.title("Welcome")

mode = st.session_state.get("auth_mode", "login")
tab1, tab2 = st.tabs(["Login", "Sign Up"])

with tab1:
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        users = load_users()
        user = next((u for u in users if u["email"] == email), None)
        if user and user["password"] == hash_password(password):
            st.session_state["logged_in"] = True
            st.session_state["user"] = user
            st.success("Logged in successfully!")
            st.switch_page("app.py")
        else:
            st.error("Invalid email or password")

with tab2:
    st.subheader("Sign Up")
    name = st.text_input("Full Name")
    email = st.text_input("Email ")
    password = st.text_input("Password ", type="password")
    if st.button("Sign Up"):
        users = load_users()
        if any(u["email"] == email for u in users):
            st.error("Email already exists")
        else:
            users.append({
                "name": name,
                "email": email,
                "password": hash_password(password)
            })
            save_users(users)
            st.success("Account created! Please login.")
            st.session_state["auth_mode"] = "login"
```

Teach this in three passes, not one:

1. Sign Up tab first (it's simpler): collect name/email/password, check the email isn't already taken, hash the password, append a new dictionary to the users list, save it back to the file.
2. Login tab: load the users, try to find one whose email matches what was typed, then compare the hashed version of the typed password against the stored hash.
3. Note the duplicate variable names (email, password) reused in both tabs are fine — st.text_input needs a unique label per widget, which is why the Sign Up tab's labels have a trailing space ("Email ") to make them technically different from the Login tab's labels.

> **Common error to pre-empt**
>
> StreamlitDuplicateElementId or similar errors happen when two widgets on the same page have identical labels with no other distinguishing detail. If students hit this, the fix is giving each st.text_input a key="..." argument with a unique string, which is a cleaner fix than the trailing-space trick above — worth mentioning as the 'proper' way if there's time.

## 9. Wire login state into app.py

Add this near the top of app.py, before anything else is drawn, so the page can decide what to show:

```python
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user" not in st.session_state:
    st.session_state["user"] = None
```

Then, at the bottom of app.py, add a sidebar section that changes depending on login state:

```python
st.sidebar.markdown("---")
if st.session_state.get("logged_in"):
    st.sidebar.success(f"Logged in as {st.session_state['user']['name']}")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.switch_page("app.py")
else:
    st.sidebar.info("Please log in to track your progress.")
    if st.sidebar.button("Login / Sign Up"):
        st.switch_page("pages/login.py")
```

Point out the symmetry: logging in sets session_state values, logging out clears the same values back to their defaults. Nothing else about the app needs to change for this to work everywhere, because every page can check st.session_state['logged_in'] the same way.

## 10. Test the full cycle together

1. Run the app, click Login / Sign Up, switch to the Sign Up tab, create an account.
2. Confirm data/users.json now contains the new user with a long scrambled password — not the real password.
3. Log in with that account, confirm the sidebar shows 'Logged in as ...'.
4. Click Logout, confirm it returns to the logged-out sidebar state.
5. Log in again with the same credentials to prove the data really persisted.

## 11. Commit and push

```bash
git add .
git commit -m "Chapter 5: Login system with session state"
git push
```

## 12. End-of-class checkpoint

- Sign up creates a real entry in data/users.json with a hashed password.
- Login works, and failed login shows an error instead of crashing.
- Logging out and back in correctly updates the sidebar.

> **Preview Class 4**
>
> Tell students: 'Next class, we make the Flashcards page actually teach Japanese — real vocabulary, a real progress counter, and we'll connect it to the account you just built today.'

---

# CLASS 4

### Flashcards Feature, Vocabulary Data & Progress Tracking

> **Class goal**
>
> By the end of today, the Flashcards page shows real Japanese vocabulary, lets students flip through cards with Previous/Next, reveal the answer, and saves 'words learned' permanently to that user's account.

## Timing overview (3.5 hours)

| Time | Segment | What happens |
|------|---------|--------------|
| 0:00 | Recap | session_state, login/logout cycle, why we hash passwords |
| 0:15 | Designing the vocabulary data | What a flashcard 'looks like' as a dictionary; building words.json |
| 0:50 | Loading vocabulary in code | Reading words.json, indexing through a list |
| 1:15 | Tracking position with session_state | current_card index, Previous/Next without losing your place |
| 1:45 | Break | 15 minutes |
| 2:00 | Building the flashcard UI | Card layout, show/hide answer, progress label '1 / 20' |
| 2:45 | Saving progress per user | Marking words as learned, writing it back to users.json |
| 3:15 | Checkpoint | Full flashcard flow works and progress is saved to the right account |

---

## 1. Recap (10 min)

- What does st.session_state remember that a normal variable wouldn't?
- Why do we hash passwords instead of saving them as plain text?
- What's inside users.json right now, structurally — a list of what?

## 2. Designing the vocabulary data

Before writing any UI code, design the data shape together on the whiteboard. Ask: 'What pieces of information does one flashcard need?' Build up to this dictionary shape as a class:

```json
{
  "kanji": "学校",
  "hiragana": "がっこう",
  "romaji": "gakkou",
  "english": "school"
}
```

Then explain: the whole vocabulary list is just many of these dictionaries inside one big list — exactly the same shape as users.json, just storing different information.

### Create data/words.json

Provide students this starter file to type or paste in (about 20 words is enough for a real Class 4 — there's no need to reach 800 words live in class; mention that scaling up the list later is just adding more entries, no new code):

```json
[
  {"kanji": "学校", "hiragana": "がっこう", "romaji": "gakkou", "english": "school"},
  {"kanji": "水", "hiragana": "みず", "romaji": "mizu", "english": "water"},
  {"kanji": "本", "hiragana": "ほん", "romaji": "hon", "english": "book"},
  {"kanji": "食べる", "hiragana": "たべる", "romaji": "taberu", "english": "to eat"},
  {"kanji": "飲む", "hiragana": "のむ", "romaji": "nomu", "english": "to drink"},
  {"kanji": "行く", "hiragana": "いく", "romaji": "iku", "english": "to go"},
  {"kanji": "見る", "hiragana": "みる", "romaji": "miru", "english": "to see"},
  {"kanji": "先生", "hiragana": "せんせい", "romaji": "sensei", "english": "teacher"},
  {"kanji": "友達", "hiragana": "ともだち", "romaji": "tomodachi", "english": "friend"},
  {"kanji": "家", "hiragana": "いえ", "romaji": "ie", "english": "house"}
]
```

> **Teaching tip**
>
> Have students save this in data/words.json (note: ensure_ascii=False, used in save functions, is what allows Japanese characters to be stored and re-read correctly — remind them of this from Class 3's save_users function).

## 3. Loading vocabulary in code

Add a load_words() function. Students can add this directly to a new file utils/words.py, mirroring the pattern from auth.py in Class 3 — explicitly point out the repetition of the pattern, since recognizing repeated patterns is a real programming skill.

```python
import json

WORDS_FILE = "data/words.json"

def load_words():
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
```

## 4. Tracking position with session_state

Ask the room: 'If we click Next and the whole script reruns from the top, how does the app remember which card we were on?' They should now confidently answer: session_state. Let a student explain it before you confirm.

In pages/flashcards.py, set up the index:

```python
import streamlit as st
from utils.words import load_words

st.title("📖 Flashcards")
st.write("Learn new vocabulary with flashcards.")

words = load_words()

if "current_card" not in st.session_state:
    st.session_state["current_card"] = 0
if "show_answer" not in st.session_state:
    st.session_state["show_answer"] = False
```

Explain current_card as 'which position in the list we're looking at' — exactly like the counter demo from last class, just counting through flashcards instead of clicks.

## 5. BREAK (15 minutes)

## 6. Building the flashcard UI

Add this below the session_state setup in pages/flashcards.py:

```python
card = words[st.session_state["current_card"]]
total = len(words)
position = st.session_state["current_card"] + 1

st.markdown(f"**{position} / {total}**")

with st.container(border=True):
    st.markdown(f"<h3 style='text-align:center'>{card['hiragana']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align:center'>{card['kanji']}</h1>", unsafe_allow_html=True)

    if st.session_state["show_answer"]:
        st.markdown(f"<h3 style='text-align:center'>{card['english']}</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Previous", use_container_width=True):
        if st.session_state["current_card"] > 0:
            st.session_state["current_card"] -= 1
            st.session_state["show_answer"] = False

with col2:
    if st.button("👁 Show Answer", use_container_width=True):
        st.session_state["show_answer"] = True

with col3:
    if st.button("Next ➡", use_container_width=True):
        if st.session_state["current_card"] < total - 1:
            st.session_state["current_card"] += 1
            st.session_state["show_answer"] = False
```

Walk through the logic carefully:

- card = words[st.session_state["current_card"]] — grabs the one dictionary at our current position out of the list.
- st.container(border=True) — draws a bordered box, giving us the visual 'card' look from the mockup.
- Previous/Next change current_card by 1, with a guard (> 0 and < total - 1) so we can't go below the first card or past the last one.
- Both Previous and Next reset show_answer back to False — so the next card always starts hidden, matching real flashcard behavior.

> **If position numbers look off**
>
> Remind students lists count from 0, but humans count from 1 — that's exactly why we calculate position = current_card + 1 just for display, while current_card itself still correctly indexes into the list starting at 0.

## 7. Saving progress per user

Goal: when a logged-in student views a card's answer, record that word as 'learned' on their account, so the dashboard (wired up properly in Class 5) can show a real number instead of 0.

Add a helper to utils/auth.py:

```python
def mark_word_learned(user_email, word_kanji):
    users = load_users()
    for u in users:
        if u["email"] == user_email:
            learned = u.get("words_learned", [])
            if word_kanji not in learned:
                learned.append(word_kanji)
            u["words_learned"] = learned
    save_users(users)
```

Explain: u.get("words_learned", []) safely handles accounts created before this feature existed — if the key isn't there yet, it starts as an empty list instead of crashing. This is a useful, realistic pattern: real apps constantly add new fields to old data.

Back in pages/flashcards.py, update the Show Answer button to also save progress, but only for logged-in users:

```python
with col2:
    if st.button("👁 Show Answer", use_container_width=True):
        st.session_state["show_answer"] = True
        if st.session_state.get("logged_in"):
            from utils.auth import mark_word_learned
            mark_word_learned(st.session_state["user"]["email"], card["kanji"])
```

> **Discussion point for the class**
>
> Ask: 'Why check logged_in before saving progress?' Let students reason it through — there's no account to attach the progress to if nobody's logged in. This connects today's feature directly back to Class 3's login system, reinforcing that the chapters build on each other rather than being separate tricks.

## 8. Verify it together

1. Log in with the account created last class.
2. Open Flashcards, click Show Answer on a couple of cards, click Next a few times.
3. Open data/users.json directly in VS Code and confirm a words_learned list has appeared on that user's entry with kanji in it.

## 9. Commit and push

```bash
git add .
git commit -m "Chapters 6-8: Flashcards feature with vocabulary and progress tracking"
git push
```

## 10. End-of-class checkpoint

- Flashcards page shows real vocabulary with kanji, hiragana, and English.
- Previous/Next move through the list correctly and don't crash at either end.
- Show Answer reveals the English meaning and saves progress for logged-in users.

> **Preview Class 5**
>
> Tell students: 'Last class — we build the quiz, wire the dashboard numbers to be real instead of zeros, and spend time making the whole app look polished, closer to the original mockup.'

---

# CLASS 5

### Quiz Feature, Real Dashboard Stats & Visual Polish

> **Class goal**
>
> By the end of today, the Quiz page asks real multiple-choice questions generated from the vocabulary list, the dashboard shows real numbers pulled from the logged-in user's saved progress, and the whole app has a custom color theme closer to the original design — and every student pushes a finished v1 to GitHub.

## Timing overview (3.5 hours)

| Time | Segment | What happens |
|------|---------|--------------|
| 0:00 | Recap | Flashcards data flow, mark_word_learned, why we check logged_in first |
| 0:15 | Designing the quiz | Multiple choice from vocab data; generating wrong answers (distractors) |
| 0:55 | Building the quiz UI | Radio buttons, progress bar, scoring, Next question |
| 1:40 | Break | 15 minutes |
| 1:55 | Wiring the real dashboard | Replacing hardcoded 0s with real counts from users.json |
| 2:30 | Visual polish with CSS | st.markdown + custom CSS to approach the mockup's look |
| 3:05 | Final commit, push, and recap | Tag a v1 release, review the whole 5-class journey |
| 3:25 | Where to go next | What chapters 6-12 (already partly done) and beyond could look like |

---

## 1. Recap (10 min)

- How does the flashcards page know which word is currently being shown?
- Why does u.get("words_learned", []) use .get instead of square brackets?
- Where exactly does mark_word_learned save its data?

## 2. Designing the quiz: multiple choice from vocabulary data

Explain the plan in plain language first: 'For each question, we'll pick one word as the correct answer, then grab a few other random words from the list to use as wrong answers, and shuffle them all together.' Let students see this is just reusing the same words.json from last class — no new data needed.

### A helper function: generating one quiz question

Add this to utils/words.py:

```python
import random

def make_question(words):
    correct = random.choice(words)
    others = [w for w in words if w != correct]
    wrong_answers = random.sample(others, k=min(3, len(others)))

    options = [correct["english"]] + [w["english"] for w in wrong_answers]
    random.shuffle(options)

    return {
        "kanji": correct["kanji"],
        "correct_answer": correct["english"],
        "options": options
    }
```

Walk through it step by step:

- random.choice(words) — picks one random dictionary from the list as the correct answer.
- others — every word except the correct one, so we don't accidentally pick the right answer twice.
- random.sample(others, k=min(3, len(others))) — picks 3 different random wrong answers; the min() guards against crashing if the vocabulary list ever has fewer than 4 words total.
- We build a list of 4 English meanings (1 correct + 3 wrong), shuffle their order, and hand back a clean dictionary describing one quiz question.

> **Why build this as its own function**
>
> Notice the quiz page itself won't need to know anything about random.sample or shuffling — it just asks for 'one question' and gets a ready-to-display dictionary back. This is the same 'recipe that does one job' idea from hash_password and load_users — worth explicitly calling back to Class 3.

## 3. Building the quiz UI

Replace pages/quiz.py with:

```python
import streamlit as st
from utils.words import load_words, make_question

st.title("❓ Take a Quiz")
st.write("Test your knowledge.")

TOTAL_QUESTIONS = 10

if "quiz_question" not in st.session_state:
    words = load_words()
    st.session_state["quiz_question"] = make_question(words)
    st.session_state["quiz_number"] = 1
    st.session_state["quiz_score"] = 0

q_num = st.session_state["quiz_number"]
progress = q_num / TOTAL_QUESTIONS

st.progress(progress, text=f"Question {q_num} of {TOTAL_QUESTIONS}")

question = st.session_state["quiz_question"]

with st.container(border=True):
    st.markdown("**What does this mean?**")
    st.markdown(f"<h2 style='text-align:center'>{question['kanji']}</h2>", unsafe_allow_html=True)
    choice = st.radio("Choose one:", question["options"], index=None, label_visibility='collapsed')

if st.button("Next ➡", use_container_width=True, type="primary"):
    if choice == question["correct_answer"]:
        st.session_state["quiz_score"] += 1
    if q_num >= TOTAL_QUESTIONS:
        st.session_state["quiz_finished"] = True
    else:
        words = load_words()
        st.session_state["quiz_question"] = make_question(words)
        st.session_state["quiz_number"] += 1
    st.rerun()

if st.session_state.get("quiz_finished"):
    score = st.session_state["quiz_score"]
    st.success(f"Quiz complete! You scored {score} / {TOTAL_QUESTIONS}")
    if st.button("Take another quiz"):
        for key in ["quiz_question", "quiz_number", "quiz_score", "quiz_finished"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
```

This is the densest code block of the course — teach it in layers, not all at once:

1. First layer: explain the three new session_state values — which question we're on, our score so far, and the current question itself (so it doesn't regenerate into a different random question every single rerun while the student is still answering it).
2. Second layer: st.progress() draws a progress bar — directly matching the mockup's 'Question 3 of 10' bar.
3. Third layer: the Next button checks the answer, updates the score, and either loads a new question or marks the quiz finished.
4. Fourth layer: st.rerun() forces Streamlit to immediately rerun the script — we use this so the next question appears right away instead of waiting for another click.

> **Common beginner trap here**
>
> If students click Next without selecting an answer, choice will be None, which simply won't match correct_answer — it won't crash, it'll just count as wrong. This is worth demonstrating live so nobody panics when it happens.

## 4. BREAK (15 minutes)

## 5. Wiring the real dashboard

Now replace the hardcoded zeros in app.py's st.metric calls with real numbers. Add a small helper, e.g. directly above the dashboard section in app.py:

```python
words_learned_count = 0
if st.session_state.get("logged_in"):
    user = st.session_state["user"]
    words_learned_count = len(user.get("words_learned", []))
```

Then update the metric to use it:

```python
with col1:
    st.metric("📖 Words Learned", f"{words_learned_count} / 800")
```

> **Discussion point**
>
> Ask the class: 'Why might this number be stale if the user just answered flashcards in another tab?' Lead them toward understanding that st.session_state["user"] is a snapshot taken at login — it won't reflect changes saved to the file afterwards unless we reload it. A simple fix worth showing: re-fetch the user's record from load_users() each time the dashboard runs, instead of trusting the snapshot in session_state.

For students with extra time, repeat the same pattern for Quizzes Taken (track a quizzes_taken count on the user dictionary, incremented inside the quiz's 'finished' branch) and Kanji Learned (can reuse words_learned, since every word already has a kanji field).

## 6. Visual polish with custom CSS

Explain: 'Everything we've built works. Now let's make it look closer to the original design, using a trick — Streamlit lets us inject our own CSS using st.markdown.'

Add near the top of app.py (and optionally repeat at the top of each page):

```python
st.markdown("""
<style>
    .stButton button {
        background-color: #5B21B6;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton button:hover {
        background-color: #4338CA;
        color: white;
    }
    div[data-testid="stMetric"] {
        background-color: #F5F3FF;
        border-radius: 12px;
        padding: 16px;
    }
</style>
""", unsafe_allow_html=True)
```

Explain just enough CSS for this to make sense, not a full CSS course:

- .stButton button targets every button Streamlit draws; background-color, color, and border-radius change its fill color, text color, and corner roundness.
- :hover is a special CSS state meaning 'while the mouse is over this element' — this is how we get the purple-to-indigo hover effect from the mockup.
- div[data-testid="stMetric"] targets the metric boxes specifically — Streamlit gives most of its components these data-testid hooks specifically so they can be styled.

> **If students want to go further**
>
> Mention, without necessarily building it live: the cherry blossom decoration and torii gate artwork on the mockup's login page were custom illustrations, not something CSS generates — those would need an actual image file. Encourage ambitious students to drop a background image into a static/ folder and reference it via CSS as an optional take-home stretch goal.

## 7. Final commit and push

```bash
git add .
git commit -m "Chapters 9-12: Quiz feature, dashboard wiring, and visual polish"
git push
```

If your platform supports it, this is a nice moment to create a GitHub Release or tag (e.g. v1.0) so students have a clear marker of 'this is the version I finished the course with.'

## 8. Course recap (10 min, do this together as a group)

Walk back through all 5 classes quickly, asking students to name the one big idea from each:

- Class 1 — Python basics + a Streamlit app is just Python that draws itself on a webpage.
- Class 2 — files inside a pages/ folder automatically become navigable pages.
- Class 3 — files let data survive after the program closes; session_state lets data survive between reruns while it's open; never store plain passwords.
- Class 4 — real features are built from the same small set of tools (lists, dictionaries, session_state, functions) applied to real data.
- Class 5 — the same small tools generate quiz logic, and a little CSS goes a long way toward making it look professional.

## 9. Where to go next (for the students)

Hand out or display the 'Next Up' chapters from the original build guide as an optional self-study roadmap, now that students have the foundation to tackle it independently:

- Scaling the vocabulary list from ~10-20 words up toward the full 800-word N5 list.
- More detailed progress tracking and streaks.
- A proper quiz history / review-mistakes feature.
- Kanji-specific study mode, separate from vocabulary flashcards.
- Continued UI polish — most realistically achieved by reading Streamlit's own theming documentation and experimenting.

## 10. End-of-course checkpoint

Every student should leave with:

- A working multi-page Streamlit app: Home/Dashboard, Flashcards, Quiz, Login/Signup.
- Real data: a vocabulary file and a users file, both in JSON.
- A working account system with hashed passwords and session-based login state.
- A dashboard showing real, saved progress for the logged-in user.
- Their own GitHub repository containing the whole project, with a commit history showing their progress class by class.

> **Closing note for the instructor**
>
> The single most valuable thing students leave with isn't this specific app — it's having personally experienced the loop of: have an idea, break it into small steps, write code, see it run, hit an error, fix it, see it work. That loop is the actual skill. Say this to them directly at the end.
