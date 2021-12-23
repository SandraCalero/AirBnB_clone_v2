#!/usr/bin/python3
"""Test module State """
from models import state
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pycodestyle


class test_state(test_basemodel):
    """Test class State"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test if name is a string"""
        new = self.value(name="California")
        self.assertEqual(type(new.name), str)

    def testDocumentation(self):
        """Check documentation"""
        self.assertTrue(len(state.__doc__) > 0)
        for method in dir(State):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
