import code
import datetime

from mutator import Mutator
from person import Person

# 
class MiniRepl:
    """ A simple wrapper for the mutator """
    def __init__(self, mutant):
        self.size = 50
        self._mutant = mutant
    
    # Run the command string passed in
    def command(self, command):
        return self._mutant.command(command)

    def __repr__(self):
        return f"Final core object: {str(self._mutant)}"

def interact(manipulatee):
    """ Handle interactive command input """
    mutant = Mutator(manipulatee)

    start = "Input commands to interact with your object, for example GET name, SET name=Will, GET *, exit"
    end = "\nExiting interactive shell\n"
    print(start)
    # Prompt, Read, Parse, Validate, Execute, in a while loop
    while True:
        outcome = ''
        txt = input("")
        if txt == 'exit' or txt == 'exit()':
            break
        try:
            outcome = mutant.command(txt)
        except ValueError:
            print('Invalid command syntax.')
        except AttributeError:
            print('Getting an attribute that does not exist yet does not allow me a valid response.')
        print(outcome)

    print(end)
    return mutant.render()

#Execute the mini-repl on a person
if __name__ == "__main__":
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com",
    )
    result = interact(person)
    print(f"Final result: {result}")
    