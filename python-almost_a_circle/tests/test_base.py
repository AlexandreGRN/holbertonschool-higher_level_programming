#!/usr/bin/python3
""" tests """


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """ Tests for different parts """
    
    # ---------- ID
    def test_id_as_positive(self):
        """ ID is positive """
        base_instance = Base(110)
        self.assertEqual(base_instance.id, 110)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)

    def test_id_as_negative(self):
        """ ID is negative """
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

    def test_id_as_none(self):
        """ ID is None """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    # ---------- JSON
    def test_to_json_string(self):
        """ Basic test to_json_string """
        rect_instance = Rectangle(10, 17, 2, 8, 70)
        rect_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """ to_json_string an empty_data """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")
        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_to_json_string(self):
        """ Test a normal to_json_string functionality """
        rect_data = {'id': 31, 'x': 14, 'y': 10, 'width': 5, 'height': 5}
        json_data = Base.to_json_string([rect_data])
        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(json_data,'{["id": 31, "x": 14, "y": 10, "width": 5, "height": 5]}')

    def test_wrong_to_json_string(self):
        """ Test a wrong functionality of to_json_string (Stolen from someone (thanks)) """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("Base.to_json_string() missing 1 required positional argument: " + "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "Base.to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    # ---------- Save_to_file method
    """     NEED SAVE TO FILE UNITTEST     """ #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ---------- Create method
    def test_create(self):
        """ Test create method """
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Monty Python')
        self.assertEqual("Base.create() takes 1 positional argument but 2 were given", str(msg.exception))

if __name__ == '__main__':
    unittest.main()
