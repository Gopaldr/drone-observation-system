
from drone_data.exceptions import InvalidSensorReadingError


class SensorReading:
    def __init__(self, sensor_type, value, unit):
        if not sensor_type.strip():
            raise InvalidSensorReadingError("Sensor type cannot be empty.")

        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise InvalidSensorReadingError("Sensor value must be a number.")

        if not unit.strip():
            raise InvalidSensorReadingError("Sensor unit cannot be empty.")

        self.sensor_type = sensor_type
        self.value = value
        self.unit = unit

    def display_reading(self):
        return f"{self.sensor_type}: {self.value} {self.unit}"
