#please note: works for manual input only

#for randomly assigning a giftee to a participant
import random
import base64

participants = []
recipients = []
 
flag = 0
while(flag == 0):
    try:
        amount_of_participants = int(input("Enter a number of participants: "))
        if amount_of_participants < 2:
            print("Number of participants has to be 2 or greater.")
        else:
            flag = 1
    except ValueError:
        print("Please enter a valid integer number.")
                
print("Input participant information.")
for i in range (1, amount_of_participants+1):
    #dont really care about possible name exceptions, to be checked later
    name = str(input(f'Enter the name of participant {i}: '))
    participants.append(name)

#create another list for gift receivers
recipients = participants.copy()
while any(participants[i] == recipients[i] for i in range (amount_of_participants)):
    random.shuffle(recipients)
    
encoded_recipients = [base64.b64encode(name.encode('utf-8')).decode('utf-8') for name in recipients]

for f in range(amount_of_participants):
    print(f"{participants[f]} gives a gift to {encoded_recipients[f]}")