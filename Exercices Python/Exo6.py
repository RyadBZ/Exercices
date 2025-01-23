price = float(input("Enter the price in dinars (e.g., 123.45): "))


dinars = int(price)  
centimes = int(round((price - dinars) * 100)) 

print(f"The price consists of {dinars} dinars and {centimes} centimes.")