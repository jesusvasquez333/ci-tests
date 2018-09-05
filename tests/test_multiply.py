#!/usr/bin/env python

import mathpack.maths as m

def test_multiply_integers():
    """
    Test the multiplication function
    """
    if m.multiply(8,7) != 56:
        raise AssertionError()
