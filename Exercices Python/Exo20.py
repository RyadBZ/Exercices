import statistics

def main():
    user_list = []

    print("Sorted List Builder")
    print("Enter numbers to build a list. Enter 0 to stop.\n")

    while True:
        try:
            user_input = input("Enter a number (or 0 to quit): ").strip()
            number = float(user_input) 
            
            if number == 0:
                if user_list: 
                    print("\nFinal List Statistics:")
                    print(f"Mean: {statistics.mean(user_list):.2f}")
                    print(f"Median: {statistics.median(user_list):.2f}")
                    
                    # Save to a file
                    save = input("Would you like to save the list to a file? (yes/no): ").strip().lower()
                    if save == "yes":
                        filename = input("Enter filename to save the list: ").strip()
                        try:
                            with open(filename, 'w') as file:
                                file.write("Numbers in the order added:\n")
                                file.writelines(f"{num}\n" for num in user_list)
                                file.write("\nNumbers in ascending order:\n")
                                file.writelines(f"{num}\n" for num in sorted(user_list))
                                file.write("\nNumbers in descending order:\n")
                                file.writelines(f"{num}\n" for num in sorted(user_list, reverse=True))
                            print(f"List saved to {filename}.")
                        except IOError:
                            print("Error saving the list to the file.")
                else:
                    print("No numbers entered. Exiting.")
                break
            
            
            user_list.append(number)
            print(f"Current List: {user_list}")
            print(f"Sorted List (Ascending): {sorted(user_list)}")
            print(f"Sorted List (Descending): {sorted(user_list, reverse=True)}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()