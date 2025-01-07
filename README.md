# AirBnB Clone - The Console

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Examples](#examples)
7. [Unit Testing](#unit-testing)
8. [Contributors](#contributors)
9. [License](#license)

## Introduction
The **AirBnB Clone - The Console** is the first step in a full web application development for managing AirBnB properties. This command-line interface (CLI) application allows users to create, update, delete, and manage different objects related to the AirBnB project, such as Users, Places, Cities, and more. It is built using Python and follows object-oriented programming principles with persistent file storage.

This project will serve as the foundation for future enhancements, including a web interface, database storage, and API integration.

## Features
- Interactive and non-interactive command interpreter.
- Object creation, modification, deletion, and storage.
- Persistent file storage using JSON serialization.
- BaseModel with automatic `id`, timestamps, and dictionary conversion.
- Unit testing to ensure functionality and correctness.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### Clone the Repository
```bash
$ git clone https://github.com/your-username/alu-AirBnB_clone.git
$ cd alu-AirBnB_clone
```

### Make the Console Executable
```bash
$ chmod +x console.py
```

## Usage
You can run the command interpreter in **interactive mode** or **non-interactive mode**.

### Interactive Mode
To start the console in interactive mode:
```bash
$ ./console.py
(hbnb) help
```
You will see a list of available commands:
```
Documented commands (type help <topic>):
========================================
EOF  help  quit
```
To exit the console, use:
```
(hbnb) quit
```

### Non-Interactive Mode
The console can also execute commands from a file or a pipe:
```bash
$ echo "help" | ./console.py
```
Output:
```
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

## Project Structure
```
alu-AirBnB_clone/
│── console.py        # The command interpreter
│── README.md         # Project documentation
│── AUTHORS           # List of contributors
│── models/           # Package for object models
│   │── __init__.py   # Makes models a package
│   │── base_model.py # Defines the BaseModel class
│   └── engine/       # Handles serialization
│       │── __init__.py
│       └── file_storage.py # Handles file storage
│── tests/            # Unit tests directory
└── ...
```

## Examples
### Creating an Object
```bash
(hbnb) create BaseModel
```
Output:
```
1234-5678-91011
```

### Listing All Objects
```bash
(hbnb) all
```
Output:
```
["[BaseModel] (1234-5678-91011) {'id': '1234-5678-91011', ...}"]
```

### Updating an Object
```bash
(hbnb) update BaseModel 1234-5678-91011 name "My Model"
```

### Deleting an Object
```bash
(hbnb) destroy BaseModel 1234-5678-91011
```

## Unit Testing
Unit tests ensure the correctness of the program. To run tests:
```bash
$ python3 -m unittest discover tests
```

## Contributors
- Ntwari Mike Chris Kevin - [GitHub](https://github.com/NtwariMikeCK)
- Ntwari Mike Chris Kevin - [GitHub](https://github.com/NtwariMikeCK)
