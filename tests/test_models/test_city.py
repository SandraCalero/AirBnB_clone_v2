#!/usr/bin/python3
"""Test module city """
from models import city
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """Test class City """

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test if id is a string"""
        new = self.value(state_id='07eeb15f-367c-4312-96fa-8566b8a8cac8')
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test if name is a string"""
        new = self.value(name="cities")
        self.assertEqual(type(new.name), str)

    def testDocumentation(self):
        """Check documentation"""
        self.assertTrue(len(city.__doc__) > 0)
        for method in dir(City):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
