import sys
import datetime

import pytest

sys.path.insert(0, "src")
from minirepl import MiniRepl
from mutator import Mutator


class TestMiniRepl:
    """ Just a simple smoke test that the minirepl will work """

    def test_can_pass_person(self):
        # Simple dummy class
        class Dummy:
            def __init__(self):
                self.name = 'Martha'
        
        mini = MiniRepl(Mutator(Dummy()))
        assert len(str(mini)) > 20

