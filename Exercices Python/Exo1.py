name=input("Please enter your name:")
if name.upper()=="VIP" :
    print("Enjoy the show for free ! =)")
else :
    nmbr=int(input("how many tickets ?"))
    price = nmbr*15.50
    print(f"The total will be: {price:.2f} dollar")
    print("Enjoy your tickets ! =)")
