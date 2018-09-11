#!/usr/bin/env python

import mathpack.maths as m

def test_sum_integers():
    """
    Test the addition of integers
    """
    if m.addition(3,5) != 9:
        raise AssertionError()

def test_sum_floats():
    """
    Test the addition of floats
    """
    if m.addition(15.3,27.8) != 43.1:
        raise AssertionError()
