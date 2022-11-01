#for sending an email
from sender_privacy import sender
from sender_privacy import password
import smtplib
#for randomly assigning a giftee to a participant
import random
#for email validation
import re

class secretSanta:
    
    #create dictionary
    def __init__(person):
        person.information = dict()
        person.selection = dict()
        person.participants = 0
        
    #get: amount of participants, name and email for each, check whether correct
    def get_information(person):
        flag = 0
        while(flag == 0):
            try:
                person.participants = int(input("Enter a number of participants: "))
                if person.participants < 2:
                    print("Number of participants has to be 2 or greater.")
                else:
                    flag = 1
            except ValueError:
                print("Please enter a valid integer number.")
                
        #for email validation
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        print("Input participant information.")
        for i in range (1, person.participants+1):
            #dont really care about possible name exceptions, to be checked later
            name = str(input(f'Enter the name of participant {i}: '))
            flag = 0
            while(flag == 0):
                email = str(input(f'Enter the e-mail of participant {i}: '))
                if(re.search(regex, email)):
                    flag = 1
                else:
                    print("Please use a valid e-mail format.")
            person.information[name] = [email]
            
    #assign a giftee at random
    def assignment(person):
        giftee = [name for name in person.information]
        for gifter in person.information:
            secret_gifter = random.choice(giftee)
            #prevent someone getting left out
            while secret_gifter == gifter or secret_gifter in person.selection: 
                secret_gifter = random.choice(giftee)
                if secret_gifter in person.selection and person.selection[secret_gifter] == gifter:
                    continue
                elif secret_gifter == gifter:
                    continue
                break
            person.selection[gifter] = secret_gifter
            #ind as in index 
            ind = giftee.index(secret_gifter)
            giftee.pop(ind)
            
    #send out an email to each participant about their assigned giftee 
    def send_email(person):
        #import gmail port number (using gmail for the sake of this secret santa)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender,password)
        print("Succesfully logged in. ")      
        for gifter,sp in person.selection.items():
            receiver = person.information[gifter][0]
            message = "SUBJECT: Secret Santa\n" \
                      "Hello {},\n\n" \
                      "Top secret information ahead! Your secret santa person is {}\n\n" \
                      "Have a jolly Chritsmtas!".format(gifter,sp)
            server.sendmail(sender,receiver,message)
            print("{} has been sent their secret person.".format(person))
        server.quit()
            

    def start(person):
            person.get_information()
            person.assignment()
            person.send_email()


if __name__ == '__main__':
    secret_santa = secretSanta()
    secret_santa.start()
