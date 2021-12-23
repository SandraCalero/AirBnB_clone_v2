#!/usr/bin/python3
"""Test module Place"""
from models import place
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pycodestyle


class test_Place(test_basemodel):
    """Test class Place"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test if city_id is a string"""
        new = self.value(city_id="07eeb15f-367c-4312-96fa-8566b8a8cac8")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test if user id is a string"""
        new = self.value(user_id="07eeb15f-367c-4312-96fa-8566b8a8cac8")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test if name is a string """
        new = self.value(name="Holberton")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test if description is a string"""
        new = self.value(description="It is a cool place")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test if number_rooms is an integer"""
        new = self.value(number_rooms=3)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test if number_bathrooms is an integer """
        new = self.value(number_bathrooms=3)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test if max_guest is an integer"""
        new = self.value(max_guest=15)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test if price_by_night is an integer"""
        new = self.value(price_by_night=80)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test if latitude is a float"""
        new = self.value(latitude=10.5)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test if longitude is a float"""
        new = self.value(longitude=14.15)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value(amenity_ids=["Wifi", "Cable"])
        self.assertEqual(type(new.amenity_ids), list)

    def testDocumentation(self):
        """Check documentation"""
        self.assertTrue(len(place.__doc__) > 0)
        for method in dir(Place):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
