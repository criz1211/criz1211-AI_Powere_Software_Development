# Write unit tests for the square function using pytest   
import pytest
from math_utils import square
def test_square():
    try:
        assert square(2) == 4
        print("✓ Test passed: square(2) == 4")
        
        assert square(-3) == 9
        print("✓ Test passed: square(-3) == 9")
        
        assert square(0) == 0
        print("✓ Test passed: square(0) == 0")
        
        assert square(1.5) == 2.25
        print("✓ Test passed: square(1.5) == 2.25")
        
        print("✓ All basic square tests passed!")
    except AssertionError as e:
        print(f"✗ Test failed in test_square: {e}")
        raise
def test_square_negative():
    try:
        with pytest.raises(TypeError):
            square("string")
        print("✓ Test passed: square('string') correctly raises TypeError")
        
        with pytest.raises(TypeError):
            square(None)
        print("✓ Test passed: square(None) correctly raises TypeError")
        
        print("✓ All negative test cases passed!")
    except Exception as e:
        print(f"✗ Test failed in test_square_negative: {e}")
        raise
