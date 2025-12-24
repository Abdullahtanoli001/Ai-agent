# 🤖 AI Weather & News Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**An intelligent AI agent powered by LangChain, Groq AI, and ReAct framework that can search the web and fetch real-time weather data.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [API Keys](#-api-keys-setup)

</div>

---

## ✨ Features

### 🤖 AI Agent
- **ReAct Framework**: Uses reasoning and action to solve complex queries
- **Multi-Tool Integration**: Combines web search and weather APIs intelligently
- **Natural Language Understanding**: Ask questions in plain English
- **Step-by-Step Reasoning**: See how the AI thinks and acts

### ☀️ Weather Lookup
- Real-time weather data from Weatherstack API
- Temperature, humidity, wind speed, and more
- Support for cities worldwide
- Beautiful visual weather cards

### 📰 News Search
- DuckDuckGo search integration
- Real-time web search results
- No API key required for search
- Fast and accurate results

### 🎨 Beautiful UI
- Modern gradient design with animations
- Tabbed interface for easy navigation
- Quick query buttons for instant testing
- Fully responsive and mobile-friendly
- Smooth transitions and loading states

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/weather-news-agent.git
cd weather-news-agent
```

### Step 2: Backend Setup
```bash
cd backend

# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Create a `.env` file in the `backend` folder:
```env
GROQ_API_KEY=your_groq_api_key_here
WEATHER_API_KEY=your_weatherstack_api_key_here
```

### Step 4: Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```
Backend will run on `http://localhost:5002`

**Terminal 2 - Frontend:**
```bash
cd frontend
# Simply open index.html in your browser
# Or use a simple HTTP server:
python -m http.server 8000
```
Then visit `http://localhost:8000`

---

## 🔑 API Keys Setup

### 1. Groq API Key (Required)
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste into `.env` file

### 2. Weatherstack API Key (Required)
1. Visit [weatherstack.com](https://weatherstack.com)
2. Sign up for a free account (1000 requests/month free)
3. Copy your API key from the dashboard
4. Paste into `.env` file

### 3. DuckDuckGo Search (No API Key Needed!)
- DuckDuckGo search works out of the box
- No registration or API key required
- Completely free to use

---

## 💡 Usage

### Example Queries

#### AI Agent Tab:
```
"Find the capital of Pakistan, then get its current weather"
"What is the weather in Karachi today?"
"Search for latest news about AI in Pakistan"
"Tell me about the weather in London and latest news there"
```

#### Weather Tab:
```
Islamabad
Karachi
New York
Tokyo
```

#### News Search Tab: