# Ops Tech Builder Test

## Overview
This project demonstrates a multi-part technical solution:
- **Part 1:** LLM API Endpoint (FastAPI) for text summarization using OpenAI or Claude (mock)
- **Part 2:** Excel/CSV parser script for extracting invoice data
- **Part 3:** Prompt comparison for entity extraction (names, dates, locations)
- **Part 4:** SQL query for top vendors by amount paid

---

## Part 1: LLM API Endpoint

A FastAPI app exposes a `/summarize` POST endpoint that accepts:
```json
{
  "text": "some input",
  "provider": "openai" | "claude" // optional, defaults to openai
}
```
- **OpenAI:** Uses real API if `OPENAI_API_KEY` is set, otherwise returns a mock summary.
- **Claude:** Returns a mock summary.

### Setup & Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=sk-...
   ```
3. Start the API:
   ```bash
   uvicorn api.llm_api:app --reload
   ```
4. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
  -H "Content-Type: application/json" \
  -d '{"text": "Summarize this text.", "provider": "openai"}'
```

---

## Part 2: Excel/CSV Parser

A script to extract PO Number, Vendor, and Amount from `.csv` or `.xlsx` files, handling missing headers and odd formatting.

### Usage
1. Place your file in the `parser/` directory (or provide the path).
2. Run:
   ```bash
   python parser/parse_invoice.py parser/sample_invoices.csv
   ```
3. Output: Clean JSON list of extracted fields.

---

## Part 3: Prompt Comparison

See `prompts/prompt_comparison.md` for:
- Two human-friendly prompts for extracting names, dates, and locations
- Notes on expected differences between GPT and Claude
- Output normalization tips

To use, paste a prompt and your paragraph into any LLM interface (ChatGPT, Claude, etc.) or use the API.

---

## Part 4: SQL Query

See `sql/top_vendors.sql` for a query to get the top 5 vendors by total amount paid in the last 30 days:
```sql
SELECT vendor, SUM(amount) AS total_paid
FROM invoices
WHERE status = 'paid'
  AND created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY vendor
ORDER BY total_paid DESC
LIMIT 5;
```

---

## Notes
- You can switch LLM providers by changing the `provider` parameter in your API request.
- For any issues, check your API keys and dependencies in `requirements.txt`. 