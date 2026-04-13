#!/bin/bash

# 1. Activate the project virtual environment
source venv/bin/activate

# 2. Execute the test suite
python3 -m pytest data/test_app.py

# Capture the exit code of the pytest command
TEST_EXIT_CODE=$?

# 3. Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "Success: All tests passed!"
    exit 0
else
    echo "Error: Test suite failed."
    exit 1
fi