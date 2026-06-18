# Intelligent Document Reconciliation System

A prototype system that automatically reconciles a Purchase Order (PO) against a Delivery Receipt by extracting structured information from scanned PDF documents and identifying discrepancies.

## Problem Statement

Businesses often need to verify whether delivered goods match the original purchase order. Manual reconciliation is time-consuming and error-prone, especially when documents are received as scanned PDFs.

This project automates the process by:

1. Reading scanned PDF documents.
2. Extracting structured information using Gemini.
3. Comparing line items across documents.
4. Generating a reconciliation report highlighting discrepancies.

---

## Features

* Extracts structured data directly from scanned PDF documents.
* Identifies:

  * Quantity mismatches
  * Price mismatches
  * Description mismatches
  * Missing items
* Generates machine-readable JSON reports.
* Exposes functionality through a FastAPI endpoint.
* Works without traditional OCR pipelines.

---

## Architecture

```text
Purchase Order PDF
        │
        ▼
 Gemini Extraction
        │
        ▼
 Structured JSON

Delivery Receipt PDF
        │
        ▼
 Gemini Extraction
        │
        ▼
 Structured JSON

        ▼
 Comparison Engine
        │
        ▼
 Reconciliation Report
```

---

## Technology Stack

* Python
* Google Gemini 2.5 Flash
* FastAPI
* Python Dotenv

---

## Project Structure

```text
document-reconciliation-system/

├── data/
│   ├── order_form_scanned.pdf
│   └── delivery_receipt_scanned.pdf
│
├── extractor.py
├── comparator.py
├── main.py
├── app.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd document-reconciliation-system
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the CLI Version

```bash
python main.py
```

Example output:

```text
==================================================
DOCUMENT RECONCILIATION REPORT
==================================================

Order Number: BSC-PO-2024-0871

Mismatches Found: 4

1. Quantity Mismatch
   SKU: MKB-TKL-BRN
   Ordered Quantity: 30
   Delivered Quantity: 28

2. Price Mismatch
   SKU: HUB-7IN1-UC
   Ordered Price: 850
   Delivered Price: 800

3. Description Mismatch
   SKU: EDP-BLK-9040
   Ordered Description: Ergonomic Desk Pad (Black) - 90x40 cm
   Delivered Description: Ergonomic Desk Mat (Black) - 90x40 cm

4. Missing Item
   SKU: CMT-STL-UND
   Ordered Quantity: 10
   Delivered Quantity: 0
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Upload:

* Purchase Order PDF
* Delivery Receipt PDF

The API returns a JSON reconciliation report.

---

## Design Decisions

### Why Gemini Instead of OCR?

I evaluated both OCR-based extraction and Gemini-based extraction.

The OCR approach introduced SKU recognition errors and lost table structure, requiring additional parsing logic.

Gemini was able to directly extract accurate structured JSON from scanned PDFs, significantly simplifying the pipeline and improving extraction quality for this prototype.

---

## Future Improvements

For a production deployment, potential enhancements include:

* Standardized mismatch schemas for downstream systems
* Extraction confidence scores
* Severity levels for discrepancies
* Database persistence
* Audit logging
* Human-in-the-loop review workflows
* ERP integration
* Batch document processing

---

## Author

Shivangouda P B
