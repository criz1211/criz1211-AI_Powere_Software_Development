# Write unit tests for the square function using pytest
import pytest
from math_utils import square, cube

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(1.5) == 2.25
    print("test_square passed")

def test_square_negative():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        square(None)
    print("test_square_negative passed")

def test_cube():
    assert cube(2) == 8
    assert cube(-3) == -27
    assert cube(0) == 0
    assert cube(1.5) == 3.375
    print("test_cube passed")

def test_cube_negative():
    with pytest.raises(TypeError):
        cube("string")
    with pytest.raises(TypeError):
        cube(None)
    print("test_cube_negative passed")
