# 🚀 Build Your First AI Agent Web App Workshop

## Welcome, Future Developers! 👋

In this hands-on workshop, you'll build a real AI-powered web application from scratch! By the end, you'll have created an **Assignment Helper** that uses Google's Gemini AI to generate academic content.

---

## 📚 What You'll Learn

| Skill | Description |
|-------|-------------|
| 🐍 **Python Basics** | Writing backend code with Flask |
| 🤖 **AI Integration** | Using Google Gemini API |
| 🌐 **Web Development** | HTML, CSS, and JavaScript |
| 🔗 **APIs** | How frontend talks to backend |
| 🚢 **Deployment** | Running your app for the world to see |

---

## 🎯 Prerequisites

Before we start, make sure you have:

- [ ] Python installed (version 3.9 or higher)
- [ ] A code editor (VS Code recommended)
- [ ] A Google account (for API key)
- [ ] Basic understanding of what programming is

**Don't worry if you're new!** We'll explain everything step by step. 🎓

---

## 🗂️ Project Structure

Here's what we'll build:

```
Workshop/
├── agent.py           # 🧠 The AI brain
├── main.py            # 🖥️ The server
├── requirements.txt   # 📦 Dependencies list
├── .env               # 🔑 Secret keys (don't share!)
└── static/
    └── index.html     # 🎨 The user interface
```

---

# 🛠️ WORKSHOP STEPS

## Step 1: Setting Up Your Project (10 mins)

### 1.1 Create a new folder
```bash
mkdir Workshop
cd Workshop
```

### 1.2 Create a virtual environment (keeps your project clean)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 1.3 Create requirements.txt
Create a file called `requirements.txt` with these contents:
```
flask
google-genai
python-dotenv
```

### 1.4 Install dependencies
```bash
pip install -r requirements.txt
```

✅ **Checkpoint:** Run `pip list` - you should see flask, google-genai, and python-dotenv installed!

---

## Step 2: Get Your AI API Key (5 mins)

### 2.1 Go to Google AI Studio
1. Visit: https://aistudio.google.com/
2. Sign in with your Google account
3. Click **"Get API Key"** → **"Create API Key"**
4. Copy the key (it looks like: `AIzaSy...`)

### 2.2 Create your .env file
Create a file called `.env` in your project folder:
```env
GOOGLE_API_KEY=paste_your_api_key_here
```

⚠️ **IMPORTANT:** Never share this file or commit it to GitHub!
                this file will be added to the variable and secret tab
---

## Step 3: Build the AI Agent (20 mins)

### 3.1 Understanding the concept
Think of the **agent** as the brain of our app. It:
1. Takes a topic from the user
2. Creates a detailed prompt for the AI
3. Sends it to Gemini
4. Returns the AI's response

### 3.2 Create agent.py
✅ **Checkpoint:** You should see AI-generated content about climate change!

---

## Step 4: Build the Backend Server (15 mins)

### 4.1 Understanding APIs
An **API** is like a waiter in a restaurant:
- Frontend (customer) → Makes a request
- API (waiter) → Takes the order to the kitchen
- Backend (kitchen) → Prepares the food
- API (waiter) → Brings the food back

### 4.2 Create main.py


### 🎯 Key Concepts Explained:
| Code | What it does |
|------|--------------|
| `@app.route("/...")` | Creates a URL endpoint |
| `methods=["POST"]` | Accepts POST requests (sending data) |
| `request.get_json()` | Gets JSON data from the request |
| `jsonify({...})` | Converts Python dict to JSON response |

---

## Step 5: Build the Frontend (25 mins)

### 5.1 Create the static folder
```bash
mkdir static
```


### 🎨 Understanding the HTML Structure:
```
┌─────────────────────────────────────┐
│           HEADER (Title)            │
├─────────────────────────────────────┤
│  ┌─────────────────────────────┐    │
│  │  Topic Input                │    │
│  ├─────────────────────────────┤    │
│  │  Word Limit Input           │    │
│  ├─────────────────────────────┤    │
│  │  Generate Button            │    │
│  ├─────────────────────────────┤    │
│  │  Output Area (hidden first) │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
```

---

## Step 6: Run Your Application! 🎉 (5 mins)

### 6.1 Start the server
```bash
python main.py
```

### 6.2 Open in browser
Go to: **http://localhost:8080**

### 6.3 Test it!
1. Enter a topic: "The importance of renewable energy"
2. Set word limit: 1500
3. Click "Generate Assignment"
4. Wait for the AI magic! ✨

✅ **Congratulations!** You just built your first AI-powered web application! 🎊

---

## 🔄 How Data Flows

```
┌──────────────────────────────────────────────────────────────────┐
│                        YOUR APPLICATION                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────────┐    │
│  │   BROWSER   │     │   FLASK     │     │   GOOGLE        │    │
│  │  (Frontend) │────▶│  (Backend)  │────▶│   GEMINI AI     │    │
│  │             │◀────│             │◀────│                 │    │
│  └─────────────┘     └─────────────┘     └─────────────────┘    │
│       │                    │                      │              │
│       │                    │                      │              │
│   index.html          main.py +              Cloud API           │
│                       agent.py                                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Flow:
1. User enters topic →
2. JavaScript sends POST request → 
3. Flask receives and calls agent →
4. Agent calls Gemini AI →
5. AI returns response →
6. Flask sends JSON back → 
7. JavaScript displays result
```

---

### AI Concepts
| Concept | Meaning |
|---------|---------|
| **Prompt** | Instructions you give to AI |
| **Model** | The AI brain (Gemini) |
| **API Key** | Your password to use the AI |


### Medium
- [ ] Add a "Clear" button to reset the form
- [ ] Show a word count of the generated content
- [ ] Add a dropdown to select assignment type (Essay, Report, etc.)


## 📖 Resources to Learn More

- **Python:** [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- **Flask:** [Flask Quickstart](https://flask.palletsprojects.com/quickstart/)
- **HTML/CSS:** [MDN Web Docs](https://developer.mozilla.org/)
- **JavaScript:** [JavaScript.info](https://javascript.info/)
- **Gemini AI:** [Google AI Documentation](https://ai.google.dev/)

---

## 🎓 Workshop Summary

Today you learned:
1. ✅ How to set up a Python project
2. ✅ How to use AI APIs (Google Gemini)
3. ✅ How to build a web server with Flask
4. ✅ How to create a beautiful frontend
5. ✅ How frontend and backend communicate

## if you Complete all the todos
**You are now an AI developer!** 🚀
---

*Happy Coding! 🎉*
