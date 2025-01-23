nmbr=int(input("enter a number:"))
if nmbr % 3 == 0 and nmbr % 5 == 0:
    print("FizzBuzz")
elif nmbr%3==0 :
    print("Fizz")
elif nmbr%5==0:
    print("Buzz")
else : 
    print("FizzBuzz ( Some child game originally, used in interviews )")