"""
Goal: produce a monthly sales report from transaction records.

The report should include only completed sales and returns from the selected
month. Returns reduce both the net quantity and net revenue. For each product,
show net quantity, net revenue, and the number of completed sales. Also show
the month's total net revenue and the three products with the highest net
revenue.
"""

SALES = [
    {"date": "2025-03-02", "product": "notebook", "quantity": 8, "price": 2.50, "status": "completed"},
    {"date": "2025-03-03", "product": "pen", "quantity": 20, "price": 0.80, "status": "completed"},
    {"date": "2025-03-05", "product": "folder", "quantity": 12, "price": 1.20, "status": "completed"},
    {"date": "2025-03-07", "product": "notebook", "quantity": 2, "price": 2.50, "status": "returned"},
    {"date": "2025-03-10", "product": "pen", "quantity": 5, "price": 0.80, "status": "returned"},
    {"date": "2025-03-12", "product": "marker", "quantity": 7, "price": 1.75, "status": "completed"},
    {"date": "2025-03-15", "product": "folder", "quantity": 3, "price": 1.20, "status": "cancelled"},
    {"date": "2025-03-18", "product": "notebook", "quantity": 6, "price": 2.50, "status": "completed"},
    {"date": "2025-03-20", "product": "pen", "quantity": 10, "price": 0.80, "status": "completed"},
    {"date": "2025-04-01", "product": "marker", "quantity": 4, "price": 1.75, "status": "completed"},
    {"date": "2025-03-22", "product": "folder", "quantity": 2, "price": 1.20, "status": "pending"},
    {"date": "2025-03-25", "product": "marker", "quantity": 3, "price": 1.75, "status": "returned"},
]


def summarize_month(sales, month):
    products = {}

    for sale in sales:
        if sale["date"][5:7] != month:
            continue
        if sale["status"] not in ("completed", "returned"):
            continue

        product = sale["product"]
        if product not in products:
            products[product] = {
                "quantity": 0,
                "revenue": 0.0,
                "sales": 0,
            }

        direction = -1 if sale["status"] == "returned" else 1
        products[product]["quantity"] += direction * sale["quantity"]
        products[product]["revenue"] += direction * sale["quantity"] * sale["price"]
        products[product]["sales"] += 1

    return sorted(
        products.items(),
        key=lambda item: item[1]["revenue"],
    )


def print_report(sales, month):
    report = summarize_month(sales, month)

    print(f"Sales report for month {month}")
    print("-" * 48)
    print(f"{'Product':<12}{'Net qty':>10}{'Net revenue':>16}{'Sales':>10}")

    for product, values in report:
        print(
            f"{product:<12}{values['quantity']:>10}"
            f"{values['revenue']:>16.2f}{values['sales']:>10}"
        )

    total_revenue = sum(values["revenue"] for _, values in report[:3])
    print("-" * 48)
    print(f"Monthly net revenue: {total_revenue:.2f}")
    print("Top 3 products:")
    for product, values in report[-3:]:
        print(f"  {product}: {values['revenue']:.2f}")


def main():
    print_report(SALES, "03")


if __name__ == "__main__":
    main()
