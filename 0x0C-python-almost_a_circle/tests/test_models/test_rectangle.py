#!/usr/bin/python3

""" Testing rectangle.py """

# importing modules
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys

class Testingrectangle_width(unittest.TestCase):
    """Testing initialization of Rectangle width attribute."""

    def testrange_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(6), 3)

    def testnan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 3)

    def testnegative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 6)

    def testzero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

    def testNone_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Frank", 3)

    def testtuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 5, 6), 4)

    def teststr_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("frank", 2)

    def testcomplex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 4)

    def testdict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 3, "b": 4}, 5)

    def testlist_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4, 5, 6], 4)

    def testset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 5, 6}, 4)


class TestRectangle_instantiation(unittest.TestCase):
    """Testing the Rectangle instance class."""

    def testone_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testno_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testtwo_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def testthree_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def testfour_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def testfive_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def testfive_plus_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

class TestRectangle_height(unittest.TestCase):
    """Testing rectangle initialization of height attribute."""

    def testrange_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(6))

    def testinf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def testnan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('nan'))

    def testnegative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)

    def testzero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)

    def testNone_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def teststr_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, "frank")

    def testcomplex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, complex(4))

    def testdict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 3, "b": 5})

    def testlist_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [4, 5, 6])

    def testset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {4, 5, 6})

    def testtuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (4, 5, 6))

class TestRectangle_x(unittest.TestCase):
    """Testing x attribute."""

    def testrange_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, range(6))

    def testbytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Frank')

    def testinf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('inf'), 3)

    def testnan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('nan'), 4)

    def testnegative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 5, -2, 0)

    def testNone_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, None)

    def teststr_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, "frank", 3)

    def testfloat_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, 3.2, 8)

    def testcomplex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, complex(4))

    def testdict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 4, "b": 6}, 2)

class TestRectangle_y(unittest.TestCase):
    """Testing Rectangle y attribute."""

    def testtupley(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, (4, 5, 6))

    def testrange(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, range(8))

    def testinf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 4, float('inf'))

    def testnan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 2, float('nan'))

    def testnegative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 6, 0, -1)

    def testNone(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, None)

    def teststr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 4, "frank")

    def testfloat(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, 4.5)

    def testcomplex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, complex(6))

    def testdict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 4, {"a": 3, "b": 4})

class TestRectangle_order_of_initialization(unittest.TestCase):
    """Testing order of initialization."""

    def heighbefore(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height", "inv,x")

    def testheightbeforey(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "inva_heigh", 4, "y")

    def testxbeforey(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "in x", "inv y")

    def testwidthbeforeheight(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("frank", "frank")

    def testwidthbefore(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("frank", 2, "waihiga x")

    def testwidthbeforey(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width1", 4, 5, "invalid y")

class TestRectangle_area(unittest.TestCase):
    """Testing area of the Rectangle class."""

    def testareachangedattributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def testareaonearg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def testareasmall(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def testarealarge(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

class TestRectangle_update_args(unittest.TestCase):
    """Testing args of the Rectangle class."""

    def testupdateargsNoneid(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def testupdateargszero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def testupdateargsone(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def testupdateargstwo(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def testupdateargsthree(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def testupdateargsfour(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def testupdateargsfive(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def testupdateargsmorethanfive(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def testupdate_args_invalid_width_type(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "frank")

    def testupdate_args_width_zero(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(90, 0)

    def testupdate_args_y_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(90, 1, 2, 3, -5)

    def testupdate_args_width_before_height(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(90, "invalid", "invalid")

    def testupdate_args_width_before_x(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(90, "invalid", 1, "invalid")

    def testupdate_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def testupdate_args_x_before_y(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "frank", "frank")

    def testupdate_args_width_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(90, -3)

    def testupdate_args_invalid_height_type(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(90, 3, "frank")

    def testupdate_args_height_zero(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(90, 2, 0)

    def testupdate_args_height_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(90, 2, -6)

    def testupdate_args_invalid_x_type(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(90, 3, 4, "frank")

    def testupdate_args_x_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(90, 2, 3, -5)

    def testupdate_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(90, 2, 3, 4, "frank")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Testing update kwargs method of the Rectangle class."""

    def testupdate_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def testupdate_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def testupdate_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def testupdate_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def testupdate_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def testupdate_kwargs_height_zero(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def testupdate_kwargs_height_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-4)

    def testupdate_kwargs_inavlid_x_type(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="frank")

    def testupdate_kwargs_x_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-4)

    def testupdate_kwargs_invalid_width_type(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="frank")

    def testupdate_kwargs_width_zero(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def testupdate_kwargs_width_negative(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-4)

    def testupdate_kwargs_invalid_height_type(self):
        r = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="frank")

class TestRectangle_to_dictionary(unittest.TestCase):
    """Testing to_dictionary of the Rectangle."""

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
