import random
from datetime import datetime

class Horoscope:
    list_of_possible_weathers = ['Good day', 'Bad day', 'Wonderful day', 'Terrible day']
    def __init__(self):
        self.weather_forecast_in_string = 'Horoscope forecast -------------\n'

    def generate_horoscope(self, zodiacsign):
        timestamp = datetime.now().strftime("%Y/%m/%d")
        self.weather_forecast_in_string += ('Horoscope for ' + zodiacsign + '. You will have a ' +
                                            self.list_of_possible_weathers[random.randint(0, len(self.list_of_possible_weathers) - 1)].lower()
                                            + ' today ' + timestamp + '.\n------------------------------\n\n')

        return self.weather_forecast_in_string