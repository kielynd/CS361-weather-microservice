import python_weather
import asyncio
import os.path
import time
import errno

file_path = 'request.txt'

async def getweather():

    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            request = f.read()
            print(request)
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            weather = await client.get(request)

            with open('response.txt', 'w') as n:
                for forecast in weather.forecasts:
                    n.writelines(str(forecast) + '\n')
                    print(forecast)
                    for hourly in forecast.hourly:
                        n.writelines(str(hourly) + '\n')
                        print(hourly)
    
    else:
        raise ValueError("%s isn't the right type of file!" % file_path)

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: 
        if e.errno != errno.ENOENT: 
            raise 

n = True  
while n == True:
    asyncio.run(getweather())
    silentremove(file_path)