"""Service response classes and helpers"""


class ZipTranslateResponse:
    """Encapsulation of the zip translation service's response"""

    def __init__(self, json):

        # break out the fields needed for display

        self.lat = float(json['lat'])
        self.long = float(json['lon'])
        self.location = json['name']


class WeatherDataForecast:

    def __init__(self, json):

        # break out the fields needed for display

        main = json['main']
        weather = json['weather'][0]
        wind = json['wind']

        self.temperature = int(main['temp'])
        self.temperature_feels_like = int(main['feels_like'])
        self.weather = str(weather['description']).capitalize()
        self.wind_speed = int(wind['speed'])
        self.wind_deg = wind['deg']
        self.wind_gust = int(wind['gust'])

    def wind_dir(self):
        """Convert the wind direction from degrees to a compass direction"""

        # use a ladder of if statements to determine which direction the
        # degrees are mapped to

        if self.wind_deg > 348.75:
            return "N"
        elif self.wind_deg > 326.25:
            return "NNW"
        elif self.wind_deg > 303.75:
            return "NW"
        elif self.wind_deg > 281.25:
            return "WNW"
        elif self.wind_deg > 258.75:
            return "W"
        elif self.wind_deg > 236.35:
            return "WSW"
        elif self.wind_deg > 213.75:
            return "SW"
        elif self.wind_deg > 191.25:
            return "SSW"
        elif self.wind_deg > 168.75:
            return "S"
        elif self.wind_deg > 146.25:
            return "SSE"
        elif self.wind_deg > 123.75:
            return "SE"
        elif self.wind_deg > 101.25:
            return "ESE"
        elif self.wind_deg > 78.75:
            return "E"
        elif self.wind_deg > 56.25:
            return "ENE"
        elif self.wind_deg > 33.75:
            return "NE"
        elif self.wind_deg > 11.25:
            return "NNE"
        else:
            return "N"


class WeatherDataResponse:
    """Encapsulation of the weather service's response"""

    def __init__(self, json):
        self.latest_raw = json['list'][0]
        self.latest = WeatherDataForecast(self.latest_raw)
