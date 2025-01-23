pnmbr=int(input("How many people need a ride??"))
taxi=int(input("How many people fit in one tax? "))
cmpt = pnmbr // taxi
if pnmbr % taxi != 0: 
    cmpt += 1

print(f"Number of taxis needed: {cmpt}")