total_amount = float(input("Enter the total amount of the purchase: $"))
number = int(input("Enter the number of items: "))
day = input("Enter the day of the week: ").strip().lower()
discount = 0.0

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    discount += 0.10  

elif day in ["saturday", "sunday"]:
    discount += 0.20  


if number > 5:
    discount += 0.05 

discount_amount = total_amount * discount
final_price = total_amount - discount_amount

print(f"The total price after discount: ${final_price:.2f}")