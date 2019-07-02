#! /usr/bin/env python3

from colorama import Fore, Back
from twilio.rest import Client
import time

print(Fore.RED + "################################################################################################",end='')
print(Back.YELLOW +"Auto Dialer & SMS",end='')
print(Back.RESET +"",end='')
print(Fore.RED + "################################################################################################")
print(Fore.BLUE+"")


#Authentication Variables

ACCOUNT_SID = None
AUTH_TOKEN = None

#Variables

FROM = None
TO = None
LIMIT = None
URL = None



#Initialization - Initialize here

ACCOUNT_SID ="Your twilio account_sid "
AUTH_TOKEN = "Your twilio auth_token"

FROM = "+country_codenumber"

URL = "https://www.dropbox.com/s/089m3tf616fc5ie/voice.xml"

###################################





client=Client(ACCOUNT_SID,AUTH_TOKEN)






#Functions


def dialer():

	TO = input('Enter the number of the person you wish to call (starting with +country_code) : ')

	print(Fore.CYAN + "")

	LIMIT = int(input('Enter the limit : '))

	print(Fore.BLUE +"")

	for i in range(LIMIT):

		print("Calling ................... \n")

		time.sleep(1)

		call = client.calls.create(to = TO, from_ = FROM , url = URL)

	print(Fore.BLUE+"")


	
def sms():

	TO = input('Enter the number of the person you wish to message (starting with +country_code) : ')

	print(Fore.CYAN + "")

	LIMIT = int(input('Enter the limit : '))

	print(Fore.BLUE +"")

	for i in range(LIMIT):

		print("Sending SMS ................... \n")

		time.sleep(1)

		message = client.messages \
				.create(
					 body="Join Earth's deadliest heroes. Like DevilsCake.",
					 from_=FROM,
					 to=TO
				 )

	print("")
   


################################################################

def main():
	while(1):
		print('Select an option : ')
		print(Fore.RED + '1.Dialer')
		print(Fore.YELLOW + '2.SMS')
		a=input()
		print(Fore.BLUE+"")
		if(a=='1'):
			dialer()
		else:
			sms()

main()