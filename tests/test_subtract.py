#!/usr/bin/env python

import pytest
import mathpack.maths as m
def test_subtract_integers():
    """
    Test the substraction function
    """
    assert(m.subtract(15,7) == 8)
