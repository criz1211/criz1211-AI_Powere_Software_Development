# Write unit tests for the square function using pytest   
import pytest
from math_utils import square
def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(1.5) == 2.25
def test_square_negative():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        square(None)
