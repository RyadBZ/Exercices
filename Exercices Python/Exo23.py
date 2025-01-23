while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")


for i in range(-n, n + 1):
    if i != 0:
        print(i)