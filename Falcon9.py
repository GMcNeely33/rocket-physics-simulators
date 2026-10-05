import requests

TRIGGER = "Start launch ignition sequence"

rocket_name = "Falcon 9"
rocket_fuel = "RP-1 kerosene and liquid oxygen"
rocket_fuel_level = 100  # percentage


def get_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 28.39,
            "longitude": -80.61,
            "current": "temperature_2m,weather_code",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["current"]
def launch():
    if rocket_fuel_level < 50:
        print(f"Fuel must be at least 50% ({rocket_fuel_level}%).")
        return
    try:
        weather = get_weather()
        print(f"Current temperature: {weather['temperature_2m']} °C")
        print(f"Weather code: {weather['weather_code']}")
    except (requests.RequestException, KeyError) as error:
        print(f"Could not retrieve weather: {error}")
    print(f"{rocket_name} is ready to launch.")

if __name__ == "__main__":
    user_input = input("Type command: ")
    if " ".join(user_input.split()).casefold() == TRIGGER.casefold():
        launch()
    else:
        print("Command not recognized.")
