'''
    Статистика продажів.
    Створіть список словників, де кожен словник представляє продаж з ключами:
    "продукт", "кількість", "ціна".
    Напишіть функцію, яка обчислює загальний дохід для кожного продукту та повертає словник,
    де ключі - це назви продуктів, а значення - загальний дохід. Створіть список продуктів,
    що принесли дохід більший ніж 1000.
'''

sales = [
    { "product": "Sony PS5", "qty": 2, "price": 1000 },
    { "product": "Sony PS5", "qty": 1, "price": 1000 },
    { "product": "iPhone 14", "qty": 5, "price": 800 },
    { "product": "Samsung TV", "qty": 3, "price": 600 },
    { "product": "iPhone 14", "qty": 1, "price": 800 }
]

def calculate_total_revenue(sales):
    revenue_by_product = {}

    for sale in sales:
        product = sale["product"]
        qty = sale["qty"]
        price = sale["price"]
        total = qty * price

        if product in revenue_by_product:
            revenue_by_product[product] += total
        else:
            revenue_by_product[product] = total

    return revenue_by_product

revenue = calculate_total_revenue(sales)

high_revenue_products = [product for product, total in revenue.items() if total > 1000]

print("Загальний дохід по продуктах:", revenue)
print("Продукти з доходом понад 1000:", high_revenue_products)