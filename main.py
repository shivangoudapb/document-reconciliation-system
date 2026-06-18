import json
from pathlib import Path

from extractor import extract_document
from comparator import compare_documents


PO_PATH = "data/order_form_scanned.pdf"
DELIVERY_PATH = "data/delivery_receipt_scanned.pdf"


print("Extracting Purchase Order...")

po_data = extract_document(
    PO_PATH
)

with open(
    "extracted/po.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        po_data,
        f,
        indent=4
    )

print("Extracting Delivery Receipt...")

delivery_data = extract_document(
    DELIVERY_PATH
)

with open(
    "extracted/delivery.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        delivery_data,
        f,
        indent=4
    )

print("Comparing Documents...")

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

with open(
    "reports/reconciliation_report.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )

print("\n")
print("=" * 50)
print("DOCUMENT RECONCILIATION REPORT")
print("=" * 50)

print(
    f"\nOrder Number: {po_data['order_number']}"
)

print(
    f"Mismatches Found: {len(mismatches)}\n"
)

for index, mismatch in enumerate(
    mismatches,
    start=1
):

    print(
        f"\n{index}. "
        f"{mismatch['issue']}"
    )

    print(
        f"   SKU: "
        f"{mismatch['sku']}"
    )

    for key, value in mismatch.items():

        if key in [
            "issue",
            "sku"
        ]:
            continue

        label = (
            key.replace("_", " ")
            .title()
        )

        print(
            f"   {label}: "
            f"{value}"
        )

print("\nDone.")