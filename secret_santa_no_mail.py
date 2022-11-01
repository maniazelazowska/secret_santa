#please note: works for manual input only
#possible feature: work with data imported from .txt or .xlsx files

#for randomly assigning a giftee to a participant
import random

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
    
for f in range (amount_of_participants):
    print(f"{participants[f]} gives a gift to {recipients[f]}")
 
 #feature: as to not spoil the fun, print recipient name in base64 for participants to decode
 #(as person operating the script will be the admin that is also participating)