
# 🛠 Ops Tech Builder – Python + AI Integration Challenge

Welcome! This short technical challenge is designed to evaluate your ability to work with Python, APIs, and structured data — the core of our day-to-day automation and integration work. We’re less focused on flashy frontends, and more interested in clean, working backend logic.

---

## 🔍 About the Role

This test simulates what you’ll be doing in the role:
- Building API endpoints that call AI models (e.g., OpenAI, Claude)
- Parsing Excel/CSV documents for real-world operations
- Thinking clearly about how to process, transform, and extract useful information
- Comparing prompt performance across different LLMs

---

## ✅ What You’ll Build

### 📦 Part 1: LLM API Endpoint (30 mins)
- Build a Flask or FastAPI app with one POST endpoint: `/summarize`
- Accepts input like: `{ "text": "some input" }`
- Calls the OpenAI API (real or mocked)
- Returns only: `{ "summary": "..." }`
- **Bonus**: Allow switching between OpenAI and Claude via a parameter

---

### 📂 Part 2: Excel/CSV Parser (20 mins)
- Write a script or API that:
  - Accepts a `.csv` or `.xlsx` file (simulate it if needed)
  - Extracts key fields (e.g., PO Number, Vendor, Amount)
  - Returns a clean JSON list
  - Handles missing headers and odd formatting

---

### 🧠 Part 3 (Bonus): Prompt Comparison (10 mins)
- Write one or two prompts that extract names, dates, and locations from a paragraph
- Run the same prompts on GPT and Claude (or describe expected differences)
- Briefly explain how you’d normalize the outputs

---

## 🛠 Optional Add-on (Part 4): SQL Query (5 mins)
Write a SQL query:
> Given a table `invoices(id, vendor, amount, status, created_at)`,  
> return the top 5 vendors by **total amount paid** in the last 30 days.

---

## 📤 Submission Instructions
1. Fork this repo or upload your scripts to a public GitHub repo
2. Organize into folders: `/api`, `/parser`, `/prompts`, `/sql`
3. Submit your repo link via the Google Form
4. Optionally record a Loom video to walk through your thought process

---

## 🧪 Evaluation Criteria
- Python fluency and code clarity
- Ability to work with files and external APIs
- Understanding of prompt design and LLM output handling
- Practical logic and documentation
- Bonus for flexibility, abstraction, or multi-model support

---

### Tech You'll Likely Use
- Python (Flask or FastAPI, Pandas, OpenAI API)
- Excel/CSV handling (openpyxl, csv, pandas)
- Optional SQL (Postgres dialect preferred)
- Mock or real AI model access

We look forward to seeing how you approach real-world automation problems!
