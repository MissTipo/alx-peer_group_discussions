#!/usr/bin/env bash
# Create the structure of the project

# Create the directories
mkdir -p models tests/test_models
if [ $? -ne 0 ]; then
    echo "Error: could not create the directories"
    exit 1
fi
echo "Created the directories for models and tests"
touch models/__init__.py models/base.py models/rectangle.py models/square.py
if [ $? -ne 0 ]; then
    echo "Error: could not create the files"
    exit 1
fi
echo "Created the files for models"
