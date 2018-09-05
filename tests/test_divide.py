#!/usr/bin/env python

import pytest
import mathpack.maths as m

def test_division_integers():
    """
    Test the division function
    """
    assert(m.divide(20,8) == 2.5)
