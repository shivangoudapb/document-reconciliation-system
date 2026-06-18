def compare_documents(po_data, delivery_data):

    mismatches = []

    delivery_items = {
        item["sku"]: item
        for item in delivery_data["items"]
    }

    for po_item in po_data["items"]:

        sku = po_item["sku"]

        delivery_item = delivery_items.get(sku)

        if delivery_item is None:

            mismatches.append({
                "sku": sku,
                "issue": "Missing Item",
                "ordered_quantity": po_item["quantity"],
                "delivered_quantity": 0
            })

            continue

        if po_item["quantity"] != delivery_item["quantity"]:

            mismatches.append({
                "sku": sku,
                "issue": "Quantity Mismatch",
                "ordered_quantity": po_item["quantity"],
                "delivered_quantity": delivery_item["quantity"]
            })

        if po_item["unit_price"] != delivery_item["unit_price"]:

            mismatches.append({
                "sku": sku,
                "issue": "Price Mismatch",
                "ordered_price": po_item["unit_price"],
                "delivered_price": delivery_item["unit_price"]
            })

        if po_item["description"] != delivery_item["description"]:

            mismatches.append({
                "sku": sku,
                "issue": "Description Mismatch",
                "ordered_description": po_item["description"],
                "delivered_description": delivery_item["description"]
            })

    return mismatches