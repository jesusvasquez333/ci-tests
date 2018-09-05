#!/usr/bin/env python

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
