
import unittest

from drone_data import (
    SensorReading,
    DroneObservation,
    TemperatureReading,
    HumidityReading,
    InvalidSensorReadingError,
    InvalidObservationError,
)


class TestDroneObservation(unittest.TestCase):

    def test_sensor_reading(self):
        sensor = SensorReading("Temperature", 28.5, "°C")
        self.assertEqual(sensor.display_reading(), "Temperature: 28.5 °C")

    def test_invalid_sensor_value(self):
        with self.assertRaises(InvalidSensorReadingError):
            SensorReading("Temperature", "hello", "°C")

    def test_add_sensor_readings(self):
        observation = DroneObservation("OBS-001", "DRONE-01", "Field A")
        observation.add_sensor_reading(TemperatureReading(28.5))
        observation.add_sensor_reading(HumidityReading(65))

        self.assertEqual(len(observation.sensor_readings), 2)

    def test_reject_invalid_sensor_object(self):
        observation = DroneObservation("OBS-001", "DRONE-01", "Field A")

        with self.assertRaises(InvalidObservationError):
            observation.add_sensor_reading("not a sensor")

    def test_invalid_observation_id(self):
        with self.assertRaises(InvalidObservationError):
            DroneObservation("", "DRONE-01", "Field A")


if __name__ == "__main__":
    unittest.main()
