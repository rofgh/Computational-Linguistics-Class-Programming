# penelope
Python cli for testing and state manipulation.


# Install
Check that you have python3 installed, this project was coded with 3.7.2:

    python3 --version
    Python 3.7.2

Create some virtual environments:

    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt

# Build
The build step could be useful for building lambda requirements in the future, but can be skipped for now.

# Test

  pytest


# Run

To get the benefits of the mutator directly, you'll want to run it from within your own code, to mutate a class of your own creation. For example:

    from minirepl import interact

    ...
    result = interact(YourObjectInstanceHere)

To try a console session with a pre-made object, run the command:

    python3 src/minirepl.py

