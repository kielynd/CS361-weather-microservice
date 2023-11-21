# CS361-weather-microservice
Weather Microservice project

This microservice receives a request for weather information, acquires the weather information for the current day and next 2 days, and outputs the information into a text file.

The microservice will continually scan for a request file in the same directory (request.txt).
To REQUEST data, place appropriate request.txt file in same directory.
The only information in request.txt should be a 6-digit zip code corresponding to place where you want to receive weather information about.
  ex. 21146

The microservice will respond by outputting the weather information to a file (response.txt). If this file does not exist in the same directory, it will be created.
Example information for one day below
  <DailyForecast date=datetime.date(2023, 11, 20) astronomy=<Astronomy moon_phase="Phase.FIRST_QUARTER" sun_rise=datetime.time(6, 55) sun_set=datetime.time(16, 49)> temperature=44>
  <HourlyForecast time=datetime.time(0, 0) temperature=47 description='Clear' kind=Kind.SUNNY>
  <HourlyForecast time=datetime.time(3, 0) temperature=43 description='Clear' kind=Kind.SUNNY>
  <HourlyForecast time=datetime.time(6, 0) temperature=40 description='Clear' kind=Kind.SUNNY>
  <HourlyForecast time=datetime.time(9, 0) temperature=39 description='Sunny' kind=Kind.SUNNY>
  <HourlyForecast time=datetime.time(12, 0) temperature=45 description='Sunny' kind=Kind.SUNNY>
  <HourlyForecast time=datetime.time(15, 0) temperature=47 description='Cloudy' kind=Kind.CLOUDY>
  <HourlyForecast time=datetime.time(18, 0) temperature=46 description='Overcast' kind=Kind.VERY_CLOUDY>
  <HourlyForecast time=datetime.time(21, 0) temperature=47 description='Clear' kind=Kind.SUNNY>

