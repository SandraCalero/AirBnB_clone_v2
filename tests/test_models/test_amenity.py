#!/usr/bin/python3
"""Test module Amenity"""
from models import amenity
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle


class test_Amenity(test_basemodel):
    """Test class amenity"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests amenities attribute name"""
        new = self.value(name="Amenities")
        self.assertEqual(type(new.name), str)

    def testDocumentation(self):
        """Check documentation"""
        self.assertTrue(len(amenity.__doc__) > 0)
        for method in dir(Amenity):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
