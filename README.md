
---

# SWE30011 IoT Project

This repository contains the project files for the IoT project developed by Le Minh Long for the course SWE30011. The project showcases the integration of various IoT technologies, including both backend and frontend components.

## Project Overview

The project aims to demonstrate the practical applications of Internet of Things (IoT) technologies. It involves collecting, processing, and visualizing data from IoT devices, focusing on environmental monitoring and control.

## Contents

1. [Summary](#summary)
2. [Conceptual Design](#conceptual-design)
   - [Block Diagrams](#block-diagrams)
   - [UML Diagrams](#uml-diagrams)
3. [Implementation](#implementation)
   - [Sensors](#sensors)
   - [Actuators](#actuators)
   - [Software/Libraries](#software-libraries)
4. [Resources](#resources)
5. [Appendix](#appendix)
   - [Sketches](#sketches)
   - [Scripts](#scripts)

## Summary

The objective of this individual assignment project is to utilize practical knowledge gained during tutorial sessions and self-learning to rapidly prototype an IoT proof-of-concept. The chosen IoT system is an environmental monitoring and control system designed to monitor indoor climate conditions and implement control actions based on sensor data. The system includes sensors to measure temperature, distance, and fire detection, along with alert systems. A Raspberry Pi 3 is integrated into the system to serve as the edge device, facilitating data storage, simple edge analytics, and user interface functionalities. The project aims to demonstrate the practical application of IoT principles in developing an environmental monitoring and control system, showcasing its potential in enhancing environmental awareness, safety, and sustainability.

## Conceptual Design

### Block Diagrams

The IoT environmental monitoring and control system consists of the following components:
- **Arduino Uno**: The central microcontroller unit responsible for interfacing with sensors and actuators.
- **Sensors**: Including temperature sensor, ultrasonic sensor for distance measurement, and flame sensor for fire detection.
- **Actuators**: Consisting of an LED indicator, buzzer for audible alerts, and a motor controlled by an L298N driver module.
- **Raspberry Pi 3**: Serving as the edge device for data storage, analytics, and user interface.
- **Communication Interface**: UART serial communication between Arduino Uno and Raspberry Pi 3 for data exchange.
- **Database**: SQLite database integrated into Raspberry Pi 3 for storing sensor data.
- **Web Interface**: A web application hosted on Raspberry Pi 3 for data visualization and user interaction.

### UML Diagrams

- **Use case diagram**: The primary use cases include data collection from sensors, data storage in the database, data visualization through the web interface, and control actions based on sensor readings.
- **Activity diagram**: Illustrates the sequence of actions involved in sensor data acquisition, database operations, and user interaction with the web interface.
- **Class diagram**: Represents the classes and their relationships in the system, such as sensor, actuator, database handler, and web server.

## Implementation

### Sensors

- **HC-SR04 Ultrasonic Sensor**: Measures distance by emitting ultrasonic waves and calculating the time taken for the waves to return after hitting an object. It provides real-time distance data, enabling the system to assess spatial constraints and detect obstacles or obstructions.
- **Flame Sensor**: Detects the presence of fire or flames by analyzing changes in infrared radiation. It serves as an early warning system for fire detection, alerting users to potential hazards.

### Actuators

- **LED (Light Emitting Diode)**: Serves as a visual indicator for system status or detected events.
- **Buzzer**: Provides auditory notifications in response to critical events or conditions.
- **L298N Motor Driver Module and Motor**: Facilitates physical control actions based on sensor inputs. The motor's operation is controlled by commands from the Arduino.

### Software/Libraries

- **Arduino Programming with Arduino IDE**: Used for programming the Arduino Uno microcontroller board. Arduino sketches define the behavior of the IoT system, including sensor data acquisition, actuator control, and serial communication protocols.
- **Raspberry Pi Programming with Python and Geany**: Python scripts leverage the Flask framework to create a web application for data visualization and system control. SQLite3 is used for database management, and PySerial enables serial communication with the Arduino.
- **Database Management with SQLite3**: Facilitates efficient storage and retrieval of sensor data.
- **Web Development with Flask**: Develops a web server on the Raspberry Pi for real-time data visualization and user interaction.

## Resources

- [How to install Raspberry Pi OS ‘RASPBIAN’](https://www.youtube.com/watch?v=h6GOb07FjG0)
- [Using the serial Plotter Tool](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-serial-plotter/)
- [RealVNC](https://www.realvnc.com/en/)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Appendix

### Sketches

![IOT Node Sketches](path/to/sketch-image)

### Scripts

All scripts are uploaded to this [Google Drive folder](https://drive.google.com/drive/u/0/folders/1x0u4qIex74hq06mrMND7y7tcCb2Fz4WS):

- **ASG1.ino**: Code for Arduino to run the IoT Node.
- **Serial_read_and_save.py**: Code running on Raspberry Pi to get data from Arduino and save it to the database.
- **App.py**: Code using Flask library to fetch data from the database and update it in real-time to the index.html file in the templates folder.

## License

This project is licensed under the MIT License.

---

Feel free to customize the content to better fit your project's specifics or any additional details you want to include.
