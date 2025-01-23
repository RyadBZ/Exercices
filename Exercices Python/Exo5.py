runner1 = input("first runner's name: ")
runner1_time = float(input(f"Time of {runner1} in seconds: "))

runner2 = input(second runner's name: ")
runner2_time = float(input(f"Time of {runner2} in seconds: "))

if runner1_time < runner2_time:
    print(f"{runner1} is faster with a time of {runner1_time} seconds.")
elif runner2_time < runner1_time:
    print(f"{runner2} is faster with a time of {runner2_time} seconds.")
else:
    print(f"{runner1} and {runner2} have the same time of {runner1_time} seconds.")