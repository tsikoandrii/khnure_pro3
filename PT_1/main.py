# 1. Отримати курси евро за попередній тиждень, вивести на екран дату + курс ||| DONE
# 2. З отриманого словника побудувати графк зміни курсу за тиждень ||| DONE
# URL for request https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json

import json
import requests
import matplotlib.pyplot as plt

nbu_response = requests.get(
    "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250321&end=20250327&valcode=eur&json"
)
converted_response = json.loads(nbu_response.content)

# Функція виводу курсу в форматі "DATE: RATE"
def print_rates(rates):
    for date, rate in rates:
        print(f"{date}: {rate}")

# Функція отримання необхідних даних з відповіді API
def get_euro_rates(rates_object):
    rates = []
    for rate_object in rates_object:
        date = rate_object["exchangedate"]
        rate = rate_object["rate"]
        rates.append([date, rate])
    return rates

# Функція для побудови графіка
def create_graph(rates):
    dates = []
    values = []

    for date_str, value in rates:
        dates.append(date_str)
        values.append(value)

        print(dates, values)

    plt.plot(dates, values)

    plt.show()

euro_rates = get_euro_rates(converted_response)
print_rates(euro_rates)
create_graph(euro_rates)
