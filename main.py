"""Main module for The Weather Report"""

import os

from services import get_latlong, get_weather
from display import print_prompt, print_weather_report, print_welcome_banner
from dotenv import load_dotenv

load_dotenv()


# clear the screen
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
os.system('cls' if os.name == 'nt' else 'clear')


def validate_zip(zipcode: str):
    """Validate and typecast user-supplied zip code to integer"""

    # ensure that the value is a valid integer
    zipint = int(zipcode)

    # ensure that the value is within the approximate range of a zip code
    if zipint < 10000 or zipint > 99999:
        raise ValueError(f"{zipcode} is not a valid US zip code")

    return zipint


def main():
    """Main program flow"""

    print_welcome_banner()

    for loop_tries in range(1, 4):

        try:

            # accept the input from the user
            print_prompt()
            user_entered_zipcode = input()

            # validate the user's input
            zipcode = validate_zip(user_entered_zipcode)

            # translate the zip code to a lat/long pair
            zip_response = get_latlong(zipcode)

            # fetch the weather for the given location
            wx_response = get_weather(zip_response.lat, zip_response.long)

            # print the results to the screen
            print_weather_report(zip_response, wx_response)

            # exit program
            exit(0)

        except ValueError as e:
            print("\n⚠️  Invalid zip code")

        except Exception as e:
            print("💥 Error:\n", repr(e))
            exit(1)


main()

print("\n\nUnable to continue, please try again later.\n")
exit(1)
