import os
import time
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from colorama import Fore, Style

def main():
    # time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = r"""
     ______   _____  ______       _______ _     _ _______      _______ _____ __   _ ______  _______  ______
     |_____] |     | |_____]         |    |_____| |______      |______   |   | \  | |     \ |______ |_____/
     |_____] |_____| |_____]         |    |     | |______      |       __|__ |  \_| |_____/ |______ |    \_
                                                                                                       
    """

    print(Fore.GREEN + ascii_art)

    phone_number = input("Enter a phone number with the country code: ")

    try:
        # keep the raw input for normalization/printing
        raw_input = phone_number
        phone_number = phonenumbers.parse(raw_input)

        print(f"Country: {geocoder.description_for_number(phone_number, 'en')}")
        print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
        print(f"Timezone: {timezone.time_zones_for_number(phone_number)}")

        # Additional useful details
        is_valid = phonenumbers.is_valid_number(phone_number)
        is_possible = phonenumbers.is_possible_number(phone_number)
        print(f"Valid: {is_valid}")
        print(f"Possible: {is_possible}")

        # Number type (mobile, fixed-line, toll-free, etc.)
        nt = phonenumbers.number_type(phone_number)
        try:
            nt_name = phonenumbers.PhoneNumberType(nt).name
        except Exception:
            nt_name = str(nt)
        print(f"Number type: {nt_name}")

        # Common formats
        print("Formats:")
        print(f"  E164: {phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"  International: {phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"  National: {phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")

        # Region and normalized input
        print(f"Region code: {phonenumbers.region_code_for_number(phone_number)}")
        print(f"Normalized input digits: {phonenumbers.normalize_digits_only(raw_input)}")
    except Exception:
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