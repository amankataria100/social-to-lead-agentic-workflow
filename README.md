# 🚀 Social-to-Lead Agentic Workflow

## 📌 Overview

This project implements a **GenAI-powered conversational agent** for a fictional SaaS product **AutoStream** — an automated video editing platform for content creators.

The agent is designed to:

* Understand user intent
* Answer product-related queries using **RAG (Retrieval-Augmented Generation)**
* Identify **high-intent users**
* Capture leads via **tool execution**

This mimics a real-world **social-to-lead conversion system**, similar to AI agents used in marketing automation platforms.

---

## 🧠 Key Features

* ✅ **Intent Detection**

  * Greeting
  * Product/Feature Queries
  * High-Intent Lead Detection

* ✅ **RAG-based Knowledge Retrieval**

  * Answers dynamically from a local knowledge base (`knowledge_base.json`)
  * Covers pricing, features, and policies

* ✅ **Multi-turn Conversation Memory**

  * Maintains state across multiple user inputs
  * Tracks lead collection progress

* ✅ **Lead Capture Tool**

  * Collects:

    * Name
    * Email
    * Platform
  * Triggers backend function only after all inputs are received

---

## 🏗️ Architecture

The system follows a **modular agent design inspired by agentic workflows (LangGraph-style)**:

1. **Intent Layer**

   * Classifies incoming user queries using rule-based NLP

2. **RAG Layer**

   * Retrieves relevant information from a structured JSON knowledge base

3. **Memory Layer**

   * Maintains conversation state (intent, lead stage, user details)

4. **Execution Layer (Tool)**

   * Executes lead capture function after validation

This separation ensures:

* Clean logic
* Easy extensibility
* Real-world deployability

---

## 🔄 Conversation Workflow

1. User starts with a query (e.g., pricing)
2. Agent retrieves information using RAG
3. User shows high intent (e.g., “I want to try Pro plan”)
4. Agent initiates lead capture
5. Collects:

   * Name → Email → Platform
6. Executes backend tool:

   ```
   Lead captured successfully
   ```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone <https://github.com/amankataria100/social-to-lead-agentic-workflow>
cd social-to-lead-agentic-workflow
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# OR
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the agent

```bash
python main.py
```

---

## 💬 Example Demo Flow

```
Hi
Can you tell me about your pricing plans?
That sounds good, I want to try the Pro plan for my YouTube channel
Aman
aman@gmail.com
YouTube
```

---

## 📁 Project Structure

```
social-to-lead-agent/
│── main.py              # Entry point
│── agent.py             # Core agent logic
│── intent.py            # Intent classification
│── rag.py               # Knowledge retrieval
│── memory.py            # State management
│── tools.py             # Lead capture tool
│── knowledge_base.json  # RAG data source
│── requirements.txt     # Dependencies
│── README.md
```

---

## 📲 WhatsApp Integration (Webhook Design)

To deploy this agent on WhatsApp:

1. Use WhatsApp Business API (via Meta or Twilio)
2. Create a webhook using Flask/FastAPI
3. Incoming messages → forwarded to agent
4. Agent processes input → generates response
5. Response sent back via WhatsApp API

### 🔁 Flow:

```
User (WhatsApp)
   ↓
Webhook (Flask/FastAPI)
   ↓
Agent (Intent + RAG + Memory)
   ↓
Response API
   ↓
User
```

### 📦 Production Enhancements:

* Replace in-memory storage with Redis/Database
* Add authentication & rate limiting
* Use LLM APIs for better intent detection

---

## 🎥 Demo Video

👉 Add your Loom / Screen Recording link here

---

## ⚙️ Tech Stack

* **Language:** Python 3.9+
* **Concepts:** RAG, Agentic Workflow, State Management
* **Libraries:** LangChain (optional), JSON, standard Python

---

## 🚀 Future Improvements

* 🔥 Integrate LLM (GPT/Gemini) for smarter responses
* 🔥 Upgrade to LangGraph for node-based workflow
* 🔥 Add Streamlit UI for better interaction
* 🔥 Store leads in a real database (MongoDB/PostgreSQL)

---

## 👤 Author

**Aman Kataria**
B.Tech CSE | Data Science & AI Enthusiast

* GitHub: https://github.com/amankataria100
* LinkedIn: https://linkedin.com/in/aman-kataria

---

## ⭐ Conclusion

This project demonstrates how a **GenAI-powered agent can convert conversations into business leads**, combining:

* Intelligence (Intent + RAG)
* Context (Memory)
* Action (Tool execution)

A practical step toward real-world AI automation systems.
