#Variables

validPin = 9999
pinNo = 0
balance = 100
amount = 0
attempt = 0
valid = False

while attempt < 3:
    attempt = attempt + 1 #Attempt +1
    pinNo = int(input("Enter Pin: "))
    if pinNo != validPin:
        print("Invalid Re-Enter")
    else:
        amount = int(input("Enter Amount :"))
        if amount > 300:
            print("Maximum Withdraw is £300")
        elif amount > balance:
            print("Insufficient amount")
        elif amount / 10 != amount //10:
            print ("Not a multiple of 10")
        else:
            valid = True
#End If
#If pin correct finish user input and remove an attempt. attempts wont matter after pin input is correct
if valid == True:
    balance = balance - amount
    print("Withdrawn £", amount)
    print("New balance £", balance)
    attempt = attempt - 1 #To stop the program counting attempt 3 keeping card if pin correct


if attempt == 3:
    print("card retained, contact your local branch")

