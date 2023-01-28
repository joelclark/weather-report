"""Display routines"""

from termcolor import colored
from responses import ZipTranslateResponse, WeatherDataResponse


def format_temperature(t: int, include_emoji=False) -> str:

    # add unit of measure to output
    output = f"{t}°F"

    # set color of output based on the supplied temperature
    if t > 85:
        output = colored(output, "red")
    if t >= 60:
        output = colored(output, "green")
    else:
        output = colored(output, "light_cyan")

    # add emojis to some, but not all, temperature ranges
    if include_emoji:
        if t >= 95:
            output = "🔥 " + output
        elif t <= 0:
            output = "🥶 " + output
        elif t <= 32:
            output = "⛸️ " + output

    return output


def print_weather_report(z: ZipTranslateResponse, w: WeatherDataResponse):

    # show the location
    location = colored(z.location, "white", attrs=["bold"])
    print(f"\n\nReport For: {location}\n")

    # print wind information
    f = w.latest
    winds = f"winds from the {f.wind_dir()} at {f.wind_speed} mph"
    gusts = f"gusting to {f.wind_gust} mph"
    print(f"🔵 {f.weather}, with {winds}, {gusts}.")

    # print temperature information
    current_temperature = format_temperature(f.temperature)
    feels_like_temperature = format_temperature(f.temperature_feels_like, True)
    current = f"Current temperature is {current_temperature}"
    feels_like = f"and it feels like {feels_like_temperature}"
    print(f"🔵 {current}, {feels_like}.\n")


def print_welcome_banner():
    """Print the welcome banner for the program"""
    print("Welcome to the Weather Report!")
    print("By Joel Clark, 2023")
    print("Sophia Learning, Intro to Python")


def print_prompt():
    """Print the prompt for the user to enter the zip code"""
    print("\nPlease enter a US Zip Code below, ", end="")
    print("some interesting values to try are:\n")
    print("\tKey West, FL:\t\t33040")
    print("\tPaducah, KY:\t\t42003")
    print("\tPhoenix, AZ:\t\t85032")
    print("\tBeverly Hills, CA:\t90210")
    print("\tBarrow, AK:\t\t99723")
    print("\nEnter Zip Code: ", end="")
