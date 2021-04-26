import random
import time



numbers = [2950250215, 7684930221, 5308495843, 3509853958, 8578375385, 2545817474, 4347104810, 7463908493, 2374981290]
pay_bill = []
account_number = True
result_token = random.choice(numbers)
while True:
    pay_bill_input = int(input("Enter Paybill number: "))
    if pay_bill_input == pay_bill:
        continue

    try:
        account_number = int(input("Enter account number: "))
    except ValueError:
        print("You have to Type A/C no.")
        continue
    print("Procedure successful \n" + "Paybill Number: "+str(pay_bill_input)+"\n"+ "A/C No:"+str(account_number)+"\n"+ "Your Token is: "+ str(result_token))
    for seconds in range(31, 1, -1):
        print(seconds)
        time.sleep(1)
    print("Token Overdue!!")
    input_again = input("Do you need token? (yes/no)").lower()
    if input_again != "yes":
        break
print("Bye! Have a great day!")