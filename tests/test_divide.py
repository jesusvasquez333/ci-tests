#!/usr/bin/env python

import mathpack.maths as m

def test_division_integers():
    """
    Test the division function
    """
    if m.divide(20,8) != 2.5:
        raise AssertionError()
