"""Loop control Statements = is the change of a loop execution from its normal sequence

    break => it is used to terminate the loop entirely
    continue +> skip to the next iteration of the loop
    pass => does nothing, acts as a placeholder"""

#BREAK
"""while True:
    name = input("Enter your name: ")
    if name != "":
        break"""

#   CONTINUE
"""phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")"""

#PASS
for i in range(1, 11):
    if i == 6:
        pass
    else:
        print(i)