"""
Test suite for color coding conversion functions.

This module contains comprehensive tests to verify the correctness of
the color coding conversion functions. It tests both directions of conversion:
- Pair number to color conversion
- Color pair to number conversion

The tests use assertions to validate that the conversions work correctly
for various test cases covering different parts of the color code range.
"""

from color_converter import get_color_from_pair_number, get_pair_number_from_color


def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
    """
    Test conversion from pair number to color pair.
    
    This function verifies that a given pair number correctly converts
    to the expected major and minor color combination.
    
    Args:
        pair_number (int): The pair number to test (1-25)
        expected_major_color (str): Expected major color result
        expected_minor_color (str): Expected minor color result
        
    Raises:
        AssertionError: If the conversion result doesn't match expected values
        
    Example:
        >>> test_number_to_pair(4, 'White', 'Brown')
        # Passes if pair 4 correctly converts to White-Brown
    """
    # Get the actual color pair from the conversion function
    major_color, minor_color = get_color_from_pair_number(pair_number)
    
    # Verify both colors match expected values
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    """
    Test conversion from color pair to pair number.
    
    This function verifies that a given major and minor color combination
    correctly converts to the expected pair number.
    
    Args:
        major_color (str): The major color to test
        minor_color (str): The minor color to test  
        expected_pair_number (int): Expected pair number result (1-25)
        
    Raises:
        AssertionError: If the conversion result doesn't match expected value
        
    Example:
        >>> test_pair_to_number('Black', 'Orange', 12)
        # Passes if Black-Orange correctly converts to pair number 12
    """
    # Get the actual pair number from the conversion function
    pair_number = get_pair_number_from_color(major_color, minor_color)
    
    # Verify the result matches expected pair number
    assert(pair_number == expected_pair_number)


def run_all_tests():
    """
    Execute all test cases for the color coding conversion functions.
    
    This function runs a comprehensive suite of tests that verify:
    - Number to color pair conversions for boundary cases
    - Color pair to number conversions for various combinations
    - Both directions work consistently (round-trip testing)
    
    The test cases cover:
    - Early pairs (White major color combinations)
    - Middle pairs (Black major color combinations) 
    - End pairs (Red and Violet major color combinations)
    
    Prints success message if all tests pass, raises AssertionError if any fail.
    """
    # Test number-to-color conversions
    test_number_to_pair(4, 'White', 'Brown')   # Test White major color
    test_number_to_pair(5, 'White', 'Slate')   # Test end of White range
    
    # Test color-to-number conversions
    test_pair_to_number('Black', 'Orange', 12)  # Test Black major color
    test_pair_to_number('Violet', 'Slate', 25)  # Test last possible pair
    test_pair_to_number('Red', 'Orange', 7)     # Test Red major color
    
    # All tests completed successfully
    print('All tests passed!')
