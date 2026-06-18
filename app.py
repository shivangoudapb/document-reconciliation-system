import os
import json
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException

from extractor import extract_document
from comparator import compare_documents

app = FastAPI(
    title="Document Reconciliation API",
    description="Compare Purchase Orders and Delivery Receipts",
    version="1.0.0"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def health_check():
    return {
        "message": "Document Reconciliation API is running"
    }


@app.post("/compare")
async def compare_documents_api(
    purchase_order: UploadFile = File(...),
    delivery_receipt: UploadFile = File(...)
):

    try:

        po_path = UPLOAD_DIR / purchase_order.filename
        dr_path = UPLOAD_DIR / delivery_receipt.filename

        with open(po_path, "wb") as buffer:
            shutil.copyfileobj(
                purchase_order.file,
                buffer
            )

        with open(dr_path, "wb") as buffer:
            shutil.copyfileobj(
                delivery_receipt.file,
                buffer
            )

        po_data = extract_document(
            str(po_path)
        )

        delivery_data = extract_document(
            str(dr_path)
        )

        mismatches = compare_documents(
            po_data,
            delivery_data
        )

        report = {
            "order_number":
                po_data["order_number"],

            "mismatches_found":
                len(mismatches),

            "mismatches":
                mismatches
        }

        return report

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )