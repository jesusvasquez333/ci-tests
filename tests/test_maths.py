#!/usr/bin/env python

import pytest
import mathpack.maths as m

def test_sum_integers():
    """
    Test the addition of integers
    """
    assert(m.addition(3,5) == 8)

def test_sum_floats():
    """
    Test the addition of floats
    """
    assert(m.addition(15.3,27.8) == 43.1)

def test_subtract_integers():
    """
    Test the substraction function
    """
    assert(m.subtract(15,7) == 8)

def test_multiply_integers():
    """
    Test the multiplication function
    """
    assert(m.multiply(8,7) == 56)

def test_division_integers():
    """
    Test the division function
    """
    assert(m.divide(20,8) == 2.5)
