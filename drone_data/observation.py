
from drone_data.sensor import SensorReading
from drone_data.exceptions import InvalidObservationError


class DroneObservation:
    def __init__(self, observation_id, drone_id, location):
        if not isinstance(observation_id, str) or not observation_id.strip():
            raise InvalidObservationError("Observation ID cannot be empty.")

        if not isinstance(drone_id, str) or not drone_id.strip():
            raise InvalidObservationError("Drone ID cannot be empty.")

        if not isinstance(location, str) or not location.strip():
            raise InvalidObservationError("Location cannot be empty.")

        self.observation_id = observation_id
        self.drone_id = drone_id
        self.location = location
        self.sensor_readings = []

    def add_sensor_reading(self, sensor_reading):
        if not isinstance(sensor_reading, SensorReading):
            raise InvalidObservationError(
                "Only SensorReading objects can be added."
            )

        self.sensor_readings.append(sensor_reading)

    def get_sensor_reading_count(self):
        return len(self.sensor_readings)

    def display_observation(self):
        print(f"Observation ID: {self.observation_id}")
        print(f"Drone ID: {self.drone_id}")
        print(f"Location: {self.location}")
        print("Sensor readings:")

        for reading in self.sensor_readings:
            print(f"- {reading.display_reading()}")
