import csv

# Function to load exchange rates from the CSV file
def load_exchange_rates(filename):
    exchange_rates = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            exchange_rates[row['code']] = float(row['rate'])
    return exchange_rates

# Function to convert USD to the desired currency
def convert_currency(amount, currency, exchange_rates):
    if currency in exchange_rates:
        return amount * exchange_rates[currency]
    else:
        print(f"Currency '{currency}' not found in exchange rates.")
        return None

def main():
    # Load exchange rates from the CSV file
    exchange_rates = load_exchange_rates('currency.csv')
    
    # Input from the user
    usd_amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency you want to have? ").upper()
    
    # Convert USD to the target currency
    converted_amount = convert_currency(usd_amount, target_currency, exchange_rates)
    
    if converted_amount is not None:
        print(f"Dollar: {usd_amount} USD")
        print(f"{target_currency}: {converted_amount:.2f}")

if __name__ == "__main__":
    main()