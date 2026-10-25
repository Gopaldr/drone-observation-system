
from drone_data.sensor import SensorReading


class TemperatureReading(SensorReading):
    def __init__(self, value):
        super().__init__("Temperature", value, "°C")


class HumidityReading(SensorReading):
    def __init__(self, value):
        super().__init__("Humidity", value, "%")
