Package Structure
-----------------
AirBnB_clone/
|_ __init__.py
|_ models/
	|_base_model.py, 
	|_ __init__.py,
    |_ /engine
        |_ __init__.py
        |_file_storage.py
|_tests/
	|_test_base_model.py
	|_ __init__.py

# AirBnB Clone Project - Phase 1

## A command interpreter to manage our AirBnB objects.
This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
3. create the first abstracted storage engine of the project: File storage.
4. create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
A shell limited to the specific use-case of managing the server side of our AirBnB clone in debugg mode. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object