from pyowm.owm import OWM

API_KEY = "c23aa314613b303de222c1f3a0fb7206"

location = input("What city and coutry are you in? ")

owm =  OWM(API_KEY)
weather_manager = owm.weather_manager()
observation = weather_manager.weather_at_place(location)
w = observation.weather


weather_status = w.detailed_status
weather_wind = w.wind()
weather_humidity = w.humidity
weather_temp = w.temperature('celsius')

print(
    f" \n"
    f"Good morning! Welcome to your local weather forecast for today, [Date].\n"
    f"we have {weather_status} towering us today"
    f"And we're starting the day off at {weather_temp['temp']} degrees although it feels like {weather_temp['feels_like']}.\n" 
    f"Winds are moving at {weather_wind['speed']} meters per second\n"

    
    )