# Author    : Harshith S R
# Date      : 22/08/2018

class Sensor:

    def __init__(self):

        self.temperature = ""

    @property
    def get_temperature(self):
        return self.temperature

    @get_temperature.setter
    def set_temperature(self, temp):
        self.temperature = temp

