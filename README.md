\# Drone Observation System



\## Overview



A Python project demonstrating object-oriented programming and modular design for storing drone observations and sensor readings.



\## Features



\- Store sensor type, measurement value, and unit.

\- Validate sensor and observation data.

\- Group multiple sensor readings within a drone observation using composition.

\- Use inheritance to create specialized temperature and humidity sensor classes.

\- Handle invalid data using custom exceptions.

\- Run automated tests with Python's `unittest` framework.



\## Project Structure



\- `drone\_data/sensor.py` — base sensor reading class.

\- `drone\_data/specialized\_sensors.py` — temperature and humidity subclasses.

\- `drone\_data/observation.py` — drone observation class.

\- `drone\_data/exceptions.py` — custom exceptions.

\- `main.py` — example application.

\- `tests/test\_observation.py` — automated tests.



\## Requirements



Python 3.10 or later recommended. No third-party packages are required.



\## Run the Application





py main.py





\## Run Tests





py -m unittest discover -s tests -v





\## OOP Concepts Demonstrated



\- Classes and objects

\- Attributes and methods

\- Inheritance and `super()`

\- Composition

\- Exception handling

\- Modular packages and imports

\- Automated testing

