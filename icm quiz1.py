
while True:
    name = input("Enter Your Customer's name: ")
    car_size = input("Enter the size of car(small,medium,large): ")

    waxed_polish = input("Do you need waxing and polishing? (yes/no)").lower()
    wax_and_polish = 3.00

    interior_cleaning = input("Do you need interior cleaning? (yes/no)").lower()
    interior_clean = 4.50

    air_fresheners = input("Purchase Air Fresheners? (yes/no)").lower()
    air_fresh = 0.50

    if car_size == "small":
        small_wash = 4.00
        total_small = small_wash + wax_and_polish + interior_clean + air_fresh
        print("customer's name: "+name)
        print("Your total is: "+str(float(total_small)))
    elif car_size == "medium":
        medium_wash = 5.00
        total_medium = medium_wash + wax_and_polish + interior_clean + air_fresh
        print("customer's name: " + name)
        print("Your total is: " + str(float(total_medium)))
    elif car_size == "large":
        large_wash = 5.50
        total_large = large_wash + wax_and_polish + interior_clean + air_fresh
        print("customer's name: " + name)
        print("Your total is: " + str(float(total_large)))

    run_again = input("Next Customer? (yes/no)").lower()
    if run_again != "yes":
        break
print("Thank you for Your Service")


