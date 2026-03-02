import os
import time
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from colorama import Fore, Style

def main():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = r"""
     ______   _____  ______       _______ _     _ _______      _______ _____ __   _ ______  _______  ______
     |_____] |     | |_____]         |    |_____| |______      |______   |   | \  | |     \ |______ |_____/
     |_____] |_____| |_____]         |    |     | |______      |       __|__ |  \_| |_____/ |______ |    \_
                                                                                                       
    """

    print(Fore.GREEN + ascii_art)

    phone_number = input("Enter a phone number with the country code: ")

    try:
        phone_number = phonenumbers.parse(phone_number)
        print(f"Country: {geocoder.description_for_number(phone_number, 'en')}")
        print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
        print(f"Timezone: {timezone.time_zones_for_number(phone_number)}")
    except:
        print("Invalid phone number!")
    
    quit_handler = input("Type q to quit or any other key to continue: ")
    if quit_handler.lower() == 'q':
        print("Goodbye!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()
    
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    main()