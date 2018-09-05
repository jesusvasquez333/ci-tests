#!/usr/bin/env python

import mathpack.maths as m

def test_subtract_integers():
    """
    Test the substraction function
    """
    if m.subtract(15,7) != 8:
        raise AssertionError()
