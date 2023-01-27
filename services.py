"""Helpers for calling the external weather service"""

import os
import requests

from responses import ZipTranslateResponse, WeatherDataResponse


class ApiServiceError(RuntimeError):
    pass


class NotFoundError(ValueError):
    pass


OPENWX_GEO_API = "https://api.openweathermap.org/geo/1.0/zip"
OPENWX_DATA_API = "https://api.openweathermap.org/data/2.5/forecast"


def _call_service(url: str, params: dict) -> requests.Response:
    """Make the HTTPS request to the API provider"""

    # ensure environment is configured
    appid = os.environ.get("OPENWX_API_KEY")

    if not appid:
        raise ApiServiceError("Missing API key, see README.md file")

    # every service call needs an API key attached, add it here
    params["appid"] = appid

    # send a GET request to the endpoint
    response = requests.get(url, params=params)

    # if the service returns a status code of something other than 200
    # then it means that the call failed in some way
    if response.status_code == 404:
        raise NotFoundError("Value not found")

    if response.status_code != 200:
        error_message = f"Service call failed with status code: {response.status_code}"
        raise ApiServiceError(error_message)

    return response


def get_latlong(zipcode: int) -> ZipTranslateResponse:
    """Call the API service to translate a zip code to a lat/long pair"""

    # the service call requires a zip code as an input
    params = {"zip": f"{zipcode},US"}

    # call the service and parse the reponse
    json = _call_service(OPENWX_GEO_API, params).json()

    # instantiate an object for the caller to use
    response = ZipTranslateResponse(json)

    return response


def get_weather(lat: float, long: float) -> WeatherDataResponse:
    """Call the API service to fetch the weather data for a lat/long pair"""

    # the service call requires a lat/long pair as input
    params = {"lat": str(lat), "lon": str(long), "units": "imperial"}

    # call the service and parse the response
    json = _call_service(OPENWX_DATA_API, params).json()

    # instantiate an object for the caller to use
    response = WeatherDataResponse(json)

    return response
