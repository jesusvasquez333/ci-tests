#!/usr/bin/env python

import pytest
import maths

def test_sum_integers():
    """
    Test the addition of integers
    """
    assert(maths.addition(3,5) == 8)

def test_sum_floats():
    """
    Test the addition of floats
    """
    assert(maths.addition(15.3,27.8) == 43.1)

def test_subtract_integers():
    """
    Test the substraction function
    """
    asser(maths.subtract(15,7) == 8)

def test_multiply_integers():
    """
    Test the multiplication function
    """
    asset(maths.multiply(8,7) == 56)

def test_division_integers():
    """
    Test the division function
    """
    assert(maths.divide(20,8) == 2.5)
