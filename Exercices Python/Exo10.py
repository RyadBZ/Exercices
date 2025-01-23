word = input("Enter a word: ")
is_palindrome = True 

for i in range(len(word) // 2):
   
    if word[i] != word[-(i + 1)]:
        is_palindrome = False 
        break 

if is_palindrome:
    print("Yes, it's a palindrome. ( Good job, you can flex in front of others )")
else:
    print("No, it's not a palindrome. ( Try 'Bob' next time )")