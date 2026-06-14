#!/usr/bin/env python3

# Imports
import pyfiglet
import logging
import os
import sys
import time

# Class Imports
from Instagram import SearchInsta
#from Search import WebSearch
#from PhoneLookup import Lookup
from IpLookup import IpLookup
from SearchUsername import SearchUsername
#from EmailLookup import EmailLookup

# Author
author = "Deadshot0x7"


# Main function
if  __name__=="__main__":
    # Print the banner
    nameOfTheScript = "007-The Bond"
    banner = pyfiglet.figlet_format(nameOfTheScript, font = "slant")
    # a simple typewriter effect
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)
    print()

    # Information of the project and the author
    print(f"\t Script by {author} V.3.0 \n \n") 
    print(f"This script is for educational purpose only \n{author} will not responsible for any misuse or damage caused by this script")
    print("Press Y to continue or any other key to exit")

    # Input from the user to continue
    choice = input(">>> ").lower()

    if choice == 'y' or choice == 'yes':
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info("Yes I will be responsible for any damage caused by this script")
        logging.info("Starting the script")

        # Use 'cls' for Windows and 'clear' for Unix/Linux/MacOS
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        print(f"\t Script by {author} V.3.0 \n \n") 

        while True:

            print("1. Instagram    \t 2. Web Search")
            print("3. Phone Lookup \t 4. Ip Address Lookup")
            print("5. Email Lookup \t 6. Search username in all platforms")
            print("7. Update       \t 8. Exit")

            option = input(">>> ")

            if option == '1':
                username = input("Enter the Instagram username: ")
                SearchInsta(username)

            elif option == '2':
                query = input("Search here: ")
                WebSearch(query)

            elif option == '3':
                phoneNo = input("Enter the phone no (with country code) : ")
                Lookup(phoneNo)

            elif option == '4':
                ip = input("Enter the ip address: ")
                IpLookup(ip)
            
            elif option == '5':
                email = input("Enter the email address: ")
                EmailLookup(email)

            
            elif option == '6':
                username = input("Enter the username: ")
                SearchUsername(username)
            
            elif option == '7':
                try:
                    os.system("git pull")
                except:
                    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                    logging.info("Error while updating the script")
                    exit()

            elif option == '8':
                logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("Exiting the script")
                exit()
            
            else:
                logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("Invalid option")
                exit()  

        
    else:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info("You have choosen not to continue")
        exit()
