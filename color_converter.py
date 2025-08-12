"""
Core color conversion functions for 25-pair color code.

This module provides the main functionality for converting between:
- Pair numbers (1-25) and their corresponding color combinations
- Color combinations and their corresponding pair numbers

The conversion follows the telecommunications industry standard where
each pair number maps to a unique combination of major and minor colors.
"""

from color_constants import MAJOR_COLORS, MINOR_COLORS


def get_color_from_pair_number(pair_number):
    """
    Convert a pair number to its corresponding major and minor colors.
    
    Args:
        pair_number (int): The pair number (1-25)
        
    Returns:
        tuple: A tuple containing (major_color, minor_color)
        
    Raises:
        Exception: If pair_number is out of valid range (1-25)
    """
    # Convert to zero-based indexing for array access
    zero_based_pair_number = pair_number - 1
    
    # Calculate major color index using integer division
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    
    # Calculate minor color index using modulo operation
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise Exception('Minor index out of range')
    
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
    """
    Convert major and minor colors to their corresponding pair number.
    
    Args:
        major_color (str): The major color name
        minor_color (str): The minor color name
        
    Returns:
        int: The pair number (1-25)
        
    Raises:
        Exception: If either color is not found in the valid color lists
    """
    # Find the index of the major color in the major colors list
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    
    # Find the index of the minor color in the minor colors list
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    
    # Calculate pair number: (major_index * minor_colors_count) + minor_index + 1
    return major_index * len(MINOR_COLORS) + minor_index + 1
