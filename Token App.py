import random
import time
import threading



numbers = [
            2950250215, 7684930221, 5308495843, 3509853958,
            8578375385, 2545817474, 4347104810, 7463908493,
            2374981290, 9483499449, 5342928112, 7295729201]

pay_bill = 215550
account_number = True
result_token = random.choice(numbers)

while True:
    pay_bill_input = int(input("Enter PayBill number: "))
    if pay_bill_input != pay_bill:
        print("Incorrect PayBill Number!")
        break
    try:
        account_number = int(input("Enter account number: "))
    except ValueError:
        print("You have to Type A/C no.")
        break
    amount = float(input("Enter amount you wish to buy: "))
    if amount == 50:
        print("Procedure successful \n"+ "Amount spent is: "+str(amount) + "\n"+ "PayBill Number: "+str(
            pay_bill_input)+"\n"+ "A/C No:"+str(account_number)+"\n"+ "Your Token is: "+ str(result_token))
        def timer():
            time.sleep(86400)
    elif amount == 100:
        print("Procedure successful \n" + "Amount spent is: " + str(amount) + "\n" + "PayBill Number: " + str(
            pay_bill_input) + "\n" + "A/C No:" + str(account_number) + "\n" + "Your Token is: " + str(result_token))
        def timer():
            time.sleep(172800)
    elif amount == 150:
        print("Procedure successful \n" + "Amount spent is: " + str(amount) + "\n" + "PayBill Number: " + str(
            pay_bill_input) + "\n" + "A/C No:" + str(account_number) + "\n" + "Your Token is: " + str(result_token))
        def timer():
            time.sleep(259200)
    elif amount == 200:
        print("Procedure successful \n" + "Amount spent is: " + str(amount) + "\n" + "PayBill Number: " + str(
            pay_bill_input) + "\n" + "A/C No:" + str(account_number) + "\n" + "Your Token is: " + str(result_token))
        def timer():
            time.sleep(345600)
    elif amount == 250:
        print("Procedure successful \n" + "Amount spent is: " + str(amount) + "\n" + "PayBill Number: " + str(
            pay_bill_input) + "\n" + "A/C No:" + str(account_number) + "\n" + "Your Token is: " + str(result_token))
        def timer():
            time.sleep(432000)
    elif amount == 300:
        print("Procedure successful \n" + "Amount spent is: " + str(amount) + "\n" + "PayBill Number: " + str(
            pay_bill_input) + "\n" + "A/C No:" + str(account_number) + "\n" + "Your Token is: " + str(result_token))
        def timer():
            time.sleep(518400)
    else:
        print("Insufficient Funds to Complete Process!")
        break


    x = threading.Thread(target=timer, args=())
    x.start()
    timer()
    print("Token Overdue!!")
    input_again = input("Do you need token? (yes/no)").lower()
    if input_again != "yes":
        break
print("Bye! Have a great day!")