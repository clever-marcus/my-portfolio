#nested loops => it is "The Inner" loop that finishes all its iterations before finishing one iteration of the "outer loop"

rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("Enter a suitable symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()