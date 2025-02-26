import csv
import os

def load_currency_rates(filename):
    rates = {}
    
    if not os.path.exists(filename): 
        print(f"Error: The file '{filename}' was not found.")
        return rates

    try:
        with open(filename, mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if len(row) >= 2:
                    currency, rate = row[0].strip(), row[2].strip()
                    try:
                        rates[currency] = float(rate)
                    except ValueError:
                        print(f"Skipping invalid rate for {currency}: {rate}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return rates

def convert_currency(amount, currency, rates):
    return amount * rates.get(currency, 0)  
def main():
    filename = r"C:\Users\John John\OneDrive\Documents\GitHub\Currency\currency.csv"  

    rates = load_currency_rates(filename)
    
    if not rates:
        print("No exchange rates available. Exiting program.")
        return
    
    try:
        dollar_amount = float(input("How much dollar do you have? "))
        currency = input("What currency you want to have? ").strip().upper()
        
        converted_amount = convert_currency(dollar_amount, currency, rates)
        
        if converted_amount > 0:
            print(f"\nDollar: {dollar_amount} USD")
            print(f"{currency}: {converted_amount:.2f}")  
            print("Currency not found in the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
