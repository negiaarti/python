from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_receipt(transaction_details, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.drawString(100, height - 50, "Transaction Receipt")
    c.drawString(100, height - 100, f"Date: {transaction_details['date']}")
    c.drawString(100, height - 150, f"Customer Name: {transaction_details['customer_name']}")
    c.drawString(100, height - 200, f"Transaction ID: {transaction_details['transaction_id']}")
    c.drawString(100, height - 250, "Items Purchased:")

    y = height - 300
    for item, price in transaction_details['items'].items():
        c.drawString(100, y, f"{item}: ${price}")
        y -= 50

    c.drawString(100, y, f"Total Amount: ${transaction_details['total_amount']}")
    c.save()

transaction_details = {
    "date": "2024-07-18",
    "customer_name": "Aarti Negi",
    "transaction_id": "123456789",
    "items": {
        "Item A": 50.00,
        "Item B": 30.00,
        "Item C": 20.00
    },
    "total_amount": 100.00
}

create_receipt(transaction_details, "receipt.pdf")
