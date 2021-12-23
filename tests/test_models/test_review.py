#!/usr/bin/python3
"""Test module Review"""
from sqlalchemy.sql.expression import text
from models import review
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pycodestyle


class test_review(test_basemodel):
    """Test class Review"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test if place_id is a string"""
        new = self.value(place_id="07eeb15f-367c-4312-96fa-8566b8a8cac8")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test if user_id is a string"""
        new = self.value(user_id="07eeb15f-367c-4312-96fa-8566b8a8cac8")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test if text is a string"""
        new = self.value(text="It is a good place")
        self.assertEqual(type(new.text), str)

    def testDocumentation(self):
        """Check documentation"""
        self.assertTrue(len(review.__doc__) > 0)
        for method in dir(Review):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
