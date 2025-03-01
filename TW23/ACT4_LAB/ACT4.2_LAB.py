file = open("currency.csv", "a+")

file.seek(0)
lines = file.readlines()

if len(lines) == 0:
    file.write("Currency\n") 
    file.write("PHP,57.94\n")
    file.flush() 
    file.seek(0) 
    lines = file.readlines() 

file.close()

exchange_rates = {} 
currencies = set() 

for i in range(1, len(lines)):
    row = lines[i].strip() 
    if row:
        parts = row.split(",")  
        currency = parts[0].strip().upper() 
        rate = float(parts[1].strip()) 
        exchange_rates[currency] = rate 
        currencies.add(currency) 

dollars = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").strip().upper()

if currency in currencies:
    converted_amount = dollars * exchange_rates[currency]
    print("\nDollar:", dollars, "USD")
    print("Philippine Peso:", converted_amount)
else:
    print("Currency not available.")
