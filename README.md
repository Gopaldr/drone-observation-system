# Drone Observation System

## Overview

The Drone Observation System is a Python project that demonstrates Object-Oriented Programming (OOP) and modular code organization. It models drone observations and manages sensor readings, including temperature and humidity measurements.

The project focuses on reusable classes, inheritance, composition, custom exceptions, and unit testing.

## Features

- Create and manage drone observations.
- Store observation IDs, drone IDs, and locations.
- Add multiple sensor readings to an observation.
- Support temperature and humidity sensor readings.
- Validate sensor values and observation details.
- Handle invalid data using custom exceptions.
- Organize code into reusable Python modules.
- Test application functionality using Python's built-in `unittest` framework.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python modules and packages
- Exception handling
- Unit testing with `unittest`

## Project Structure


drone-observation-system/
├── drone_data/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── observation.py
│   ├── sensor.py
│   └── specialized_sensors.py
├── tests/
│   └── test_observation.py
├── main.py
├── README.md
└── .gitignore


## OOP Concepts Demonstrated

### 1. Classes and Objects

The `SensorReading` class represents a sensor measurement, while the `DroneObservation` class represents a drone observation containing its identification details and sensor readings.

### 2. Inheritance

The `TemperatureReading` and `HumidityReading` classes inherit from `SensorReading`. They reuse its functionality while providing specific sensor types and measurement units.

### 3. Composition

A `DroneObservation` object contains a collection of sensor reading objects. This demonstrates composition by combining multiple objects to represent a complete observation.

### 4. Exception Handling

Custom exceptions, `InvalidSensorReadingError` and `InvalidObservationError`, handle invalid sensor values, missing observation details, and unsupported objects.

### 5. Modular Programming

The project separates sensor models, observations, specialized sensors, and exceptions into different modules within the `drone_data` package. This improves readability, reuse, and maintainability.

## Requirements

- Python 3 installed on your system.
- A terminal or command prompt.

No external Python packages are required.

## How to Run

1. Clone the repository:

  
   git clone https://github.com/Gopaldr/drone-observation-system.git
  

2. Navigate to the project directory:


   cd drone-observation-system


3. Run the application:


   py main.py
 

   On systems where `py` is unavailable, use:

  
   python main.py
  

## Expected Output


Observation ID: OBS-002
Drone ID: DRONE-01
Location: Test Field A
Sensor readings:
- Temperature: 28.5 °C
- Humidity: 65 %


## Running Unit Tests

Run the following command from the project root:


py -m unittest discover -s tests -v


Alternatively, use `python` instead of `py` if needed.

The tests cover sensor reading creation, invalid sensor values, adding sensor readings, rejection of invalid sensor objects, and observation ID validation.

## Project Status

- Application execution: Passed
- Automated unit tests: Passed (5 tests)
- Git status: Clean
- Source code: Uploaded to GitHub

## Repository

[Drone Observation System on GitHub](https://github.com/Gopaldr/drone-observation-system)
