#!/usr/bin/python3
""" This module is a unittest for the Rectangle class """

import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle class """
    def setUp(self):
        """Set up test method"""
        print("Rectangle setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.rectangle = Rectangle(1, 1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0
        # print(f"Base.__nb_objects after reset: {Base._Base__nb_objects}")

    def tearDown(self):
        """Tear down test method"""
        print("Rectangle tearDown")

        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    # test id assignment and if it increments correctly
    def test_id(self):
        """Test __init__ method:
        id assignment in the Rectangle class.
        """
        print(f"Actual id: {self.rectangle.id}")
        self.assertEqual(self.rectangle.id, 1)
        rectangle2 = Rectangle(50, 50)
        print(f"Actual id: {rectangle2.id}")
        self.assertEqual(rectangle2.id, 1)
        rectangle3 = Rectangle(1, 1)
        print(f"Actual id: {rectangle3.id}")
        self.assertEqual(rectangle3.id, 2)

    # test to many args to init method
    def test_too_many_args(self):
        """
        test too many args to init
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1, 1)

    def test_rectangle_creation(self):
        """ Test Rectangle creation """
        # basic rectangle
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        # rectangle with x
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

        # rectangle with y
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

        # rectangle with id
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

         # rectangle with negative width
         with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)

        # rectangle with negative height
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)

        # rectangle with negative x
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)

        # rectangle with negative y
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)

        # rectangle with zero width
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, 5)

        # rectangle with zero height
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 3, 4, 5)

        # rectangle with string width
        with self.assertRaises(TypeError):
            r = Rectangle("string", 2, 3, 4, 5)

        # rectangle with string height
        with self.assertRaises(TypeError):
            r = Rectangle(1, "string", 3, 4, 5)

        # rectangle with string x
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "string", 4, 5)

        # rectangle with string y
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "string", 5)

    def test_width(self):
        """ Test width getter and setter:
        width must be an integer, positive and non-zero """
        # test width getter
        self.assertEqual(self.rectangle.width, 1)
        # test width setter
        self.rectangle.width = 50
        # test width getter after setter
        self.assertEqual(self.rectangle.width, 50)
        # test width setter with negative value
        with self.assertRaises(ValueError):
            self.rectangle.width = -1
        # test width setter with zero
        with self.assertRaises(ValueError):
            self.rectangle.width = 0
        # test width setter with string
        with self.assertRaises(TypeError):
            self.rectangle.width = "string"
        # test width setter with list
        with self.assertRaises(TypeError):
            self.rectangle.width = [1, 2, 3]
        # test width setter with tuple
        with self.assertRaises(TypeError):
            self.rectangle.width = (1, 2, 3)
        # test width setter with dict
        with self.assertRaises(TypeError):
            self.rectangle.width = {"key": 1, "key2": 2}

    def test_height(self):
        """ Test height getter and setter:
        height must be an integer, positive and non-zero """
        # test height getter
        self.assertEqual(self.rectangle.height, 1)
        # test height setter
        self.rectangle.height = 50
        # test height getter after setter
        self.assertEqual(self.rectangle.height, 50)

        # test height setter with negative value
        with self.assertRaises(ValueError):
            self.rectangle.height = -1
        # test height setter with zero
        with self.assertRaises(ValueError):
            self.rectangle.height = 0
        # test height setter with string
        with self.assertRaises(TypeError):
            self.rectangle.height = "string"
        # test height setter with list
        with self.assertRaises(TypeError):
            self.rectangle.height = [1, 2, 3]
        # test height setter with tuple
        with self.assertRaises(TypeError):
            self.rectangle.height = (1, 2, 3)
        # test height setter with dict
        with self.assertRaises(TypeError):
            self.rectangle.height = {"key": 1, "key2": 2}

    def test_x(self):
        """ test x getter and setter:
        x must be an integer, positive and zero """
        # test x getter
        self.assertEqual(self.rectangle.x, 0)
        # test x setter
        self.rectangle.x = 50
        # test x getter after setter
        self.assertEqual(self.rectangle.x, 50)
