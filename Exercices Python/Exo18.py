import json

def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Save list to a file")
    print("9. Load list from a file")
    print("10. Quit")

def main():
    numbers = [1, 2, 3, 4, 5]
    print("Initial List:", numbers)

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        if choice == 1:
            try:
                value = int(input("Enter value to append: "))
                numbers.append(value)
                print("Updated List:", numbers)
            except ValueError:
                print("Invalid value. Please enter an integer.")

        elif choice == 2:
            try:
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                    print("Updated List:", numbers)
                else:
                    print("Index out of range.")
            except ValueError:
                print("Invalid input. Please enter integers for value and index.")

        elif choice == 3:
            try:
                index = int(input("Enter index to pop (or leave empty for last element): ") or -1)
                if index == -1:
                    popped_value = numbers.pop()
                elif 0 <= index < len(numbers):
                    popped_value = numbers.pop(index)
                else:
                    print("Index out of range.")
                    continue
                print(f"Popped value: {popped_value}")
                print("Updated List:", numbers)
            except IndexError:
                print("List is empty, cannot pop.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == 4:
            try:
                value = int(input("Enter value to remove: "))
                numbers.remove(value)
                print("Updated List:", numbers)
            except ValueError:
                print("Value not found in the list or invalid input.")

        elif choice == 5:
            numbers.sort()
            print("List sorted:", numbers)

        elif choice == 6:
            numbers.reverse()
            print("List reversed:", numbers)

        elif choice == 7:
            try:
                value = int(input("Enter value to search: "))
                if value in numbers:
                    print(f"Value {value} found at index {numbers.index(value)}.")
                else:
                    print(f"Value {value} not found in the list.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == 8:
            filename = input("Enter filename to save the list: ")
            try:
                with open(filename, 'w') as file:
                    json.dump(numbers, file)
                print("List saved successfully.")
            except IOError:
                print("Error saving the list.")

        elif choice == 9:
            filename = input("Enter filename to load the list from: ")
            try:
                with open(filename, 'r') as file:
                    numbers = json.load(file)
                print("List loaded successfully.")
                print("Updated List:", numbers)
            except (IOError, json.JSONDecodeError):
                print("Error loading the list.")

        elif choice == 10:
            # Quit
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()