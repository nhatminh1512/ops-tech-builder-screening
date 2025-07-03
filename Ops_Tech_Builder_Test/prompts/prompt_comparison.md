# Prompt Comparison: Extracting Names, Dates, and Locations

## Prompt 1 (Direct Extraction)

"Extract all PERSON NAMES, DATES, and LOCATIONS mentioned in the following paragraph. Return them as a JSON object with keys: 'names', 'dates', 'locations'. Only include the extracted values, no explanation. Paragraph: <paragraph>"

## Prompt 2 (Step-by-Step)

"Given the following paragraph, first list all the PERSON NAMES you find, then all the DATES, then all the LOCATIONS. Present your answer as a JSON object with three arrays: 'names', 'dates', 'locations'. Paragraph: <paragraph>"

---

## Expected Differences: GPT vs Claude
- **GPT (OpenAI):**
  - Tends to follow JSON formatting well, but may sometimes add explanations or miss edge cases (e.g., ambiguous names/locations).
  - May hallucinate or infer locations/dates if context is vague.
- **Claude (Anthropic):**
  - Often more verbose, sometimes adds explanations even when asked not to.
  - May be more conservative in extraction, sometimes omitting less obvious entities.

---

## Output Normalization Approach
- Use a JSON schema: `{ "names": [], "dates": [], "locations": [] }`
- Strip whitespace, deduplicate entries, and standardize date formats (e.g., YYYY-MM-DD).
- Use libraries like `dateutil` for date parsing and `geopy` or similar for location normalization if needed. 