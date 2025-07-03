import sys
import pandas as pd
import json
import re

def normalize_header(header):
    if not isinstance(header, str):
        return ""
    header = header.lower().strip()
    header = re.sub(r'[^a-z0-9]', '', header)
    return header

# Possible header names for each field
PO_HEADERS = ["ponumber", "po", "purchaseorder"]
VENDOR_HEADERS = ["vendor", "supplier", "payee"]
AMOUNT_HEADERS = ["amount", "total", "amt", "invoiceamount"]


def find_column(columns, possible_headers):
    for col in columns:
        norm = normalize_header(col)
        if norm in possible_headers:
            return col
    return None

def parse_file(file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path, engine="openpyxl")
    else:
        raise ValueError("Unsupported file type")

    columns = list(df.columns)
    po_col = find_column(columns, PO_HEADERS)
    vendor_col = find_column(columns, VENDOR_HEADERS)
    amount_col = find_column(columns, AMOUNT_HEADERS)

    # Fallback: try fuzzy matching if not found
    if not po_col:
        for col in columns:
            if "po" in normalize_header(col):
                po_col = col
                break
    if not vendor_col:
        for col in columns:
            if "vendor" in normalize_header(col) or "supplier" in normalize_header(col):
                vendor_col = col
                break
    if not amount_col:
        for col in columns:
            if "amount" in normalize_header(col) or "total" in normalize_header(col):
                amount_col = col
                break

    result = []
    for _, row in df.iterrows():
        entry = {
            "PO Number": row.get(po_col, None),
            "Vendor": row.get(vendor_col, None),
            "Amount": row.get(amount_col, None)
        }
        result.append(entry)
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_invoice.py <file.csv|file.xlsx>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        data = parse_file(file_path)
        print(json.dumps(data, indent=2, default=str))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1) 