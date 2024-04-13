#Currency convertion program
from currency_converter import CurrencyConverter
try:
    cr = CurrencyConverter()
    amount = float(input("Please enter the amount you want to convert: "))
    from_currency = input("Please enter the currency code that has to be converted: ").upper()
    to_currency = input("Please enter the currency code to convert: ").upper()
    print(f"You are converting {amount} {from_currency} to {to_currency}.")
    output = cr.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} equals {output} {to_currency}")
except ValueError:
    print("Invalid input! Please enter a correct currency code.")
except Exception as error:
    print(f"An error occurred: {error}")
