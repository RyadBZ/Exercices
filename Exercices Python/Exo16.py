 
    numbers = [1, 2, 3, 4, 5]

    while True:
        x
        try:
            index = int(input("Enter index (-1 to quit): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        
        if index == -1:
            print("Exiting...")
            break

        if index < 0 or index >= len(numbers):
            print(f"Invalid index. Please enter a number between 0 and {len(numbers) - 1}.")
            continue

        try:
            new_value = int(input("Enter new value: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        numbers[index] = new_value
        print("Updated list:", numbers)

if __name__ == "__main__":
    main()
