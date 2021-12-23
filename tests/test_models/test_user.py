#!/usr/bin/python3
"""Test module User"""
from models import user
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pycodestyle


class test_User(test_basemodel):
    """Test class User"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test if first_name is a string"""
        new = self.value(first_name="Betty")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test if last_name is a string"""
        new = self.value(last_name="Holberton")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test if email is a string"""
        new = self.value(email="bettyholberton@gmail.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test if password is a string"""
        new = self.value(password="BettyH123")
        self.assertEqual(type(new.password), str)

    def testDocumentation(self):
        """Check documentation"""
        self.assertTrue(len(user.__doc__) > 0)
        for method in dir(User):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
