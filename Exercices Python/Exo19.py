def main():
    unique_words = set()
    total_words = 0  

    print("Unique Word Counter")
    print("Enter words one at a time. The program will stop when you enter a duplicate word.\n")

    while True:
        word = input("Enter a word: ").strip()  
        total_words += 1

        if word.lower() in (w.lower() for w in unique_words): 
            print(f"\nYou typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words}")
            print("Unique words (sorted alphabetically):", sorted(unique_words, key=str.lower))
            
            save = input("\nWould you like to save the unique words to a file? (yes/no): ").strip().lower()
            if save == "yes":
                filename = input("Enter filename to save unique words: ").strip()
                try:
                    with open(filename, 'w') as file:
                        file.writelines(f"{word}\n" for word in sorted(unique_words, key=str.lower))
                    print(f"Unique words saved to {filename}.")
                except IOError:
                    print("Error saving unique words to file.")
            break
        else:
            unique_words.add(word)
            print(f"Word '{word}' added. You typed in {len(unique_words)} unique words.")

if __name__ == "__main__":
    main()