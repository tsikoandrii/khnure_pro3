'''
    Інвентаризація продуктів.
    Створіть словник, де ключі - це назви продуктів, а значення - їх кількість на складі.
    Напишіть функцію, яка приймає назву продукту та кількість, і оновлює словник відповідно до
    додавання або видалення продуктів. Додатково: створіть список продуктів, в яких кількість менше ніж 5.
'''

products = {
    'banana': 10,
    'apple': 3,
    'orange': 7,
    'pear': 2,
    'grape': 12,
    'strawberry': 17
}

def update_stock(product_name, qty):
    if product_name in products:
        products[product_name] += qty
    else:
        products[product_name] = qty

    if products[product_name] < 0:
        products[product_name] = 0

def get_products_with_low_stock(stock):
    low_stock_products = []

    for product, quantity in stock.items():
        if quantity < 5:
            low_stock_products.append(product)

    return low_stock_products

update_stock('banana', 100)
update_stock('grape', -15)
update_stock('orange', 4)

low_stock = get_products_with_low_stock(products)

print(products)
print(low_stock)