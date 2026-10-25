
from drone_data.observation import DroneObservation
from drone_data.specialized_sensors import (
    TemperatureReading,
    HumidityReading,
)

temperature = TemperatureReading(28.5)
humidity = HumidityReading(65)

observation = DroneObservation(
    "OBS-002",
    "DRONE-01",
    "Test Field A",
)

observation.add_sensor_reading(temperature)
observation.add_sensor_reading(humidity)

observation.display_observation()
