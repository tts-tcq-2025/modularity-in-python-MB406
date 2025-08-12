"""
Color reference manual generator for telecommunications wiring personnel.

This module provides functionality to generate a printable reference manual
that maps pair numbers to their corresponding color combinations. This is
useful for field technicians and wiring personnel who need a quick reference
guide for identifying wire pairs in telecommunications cables.
"""

from color_converter import get_color_from_pair_number


def format_color_reference_manual():
    """
    Format the complete 25-pair color coding as a reference manual for printing.
    
    This function generates a formatted table showing all 25 possible color
    pair combinations with their corresponding pair numbers. The output is
    designed to be easily readable and suitable for printing as a reference
    card for field technicians.
    
    Returns:
        str: A formatted string containing the complete color reference manual
             with headers, separators, and aligned columns
             
    Example output:
        Color Coding Reference Manual
        ==============================
        Pair Number | Major Color | Minor Color
        ------------------------------
         1          | White       | Blue
         2          | White       | Orange
        ...
    """
    # Initialize manual with title and header formatting
    manual = "Color Coding Reference Manual\n"
    manual += "=" * 30 + "\n"  # Title underline
    manual += "Pair Number | Major Color | Minor Color\n"
    manual += "-" * 30 + "\n"  # Column separator
    
    # Generate entries for all 25 pair numbers
    for pair_number in range(1, 26):
        # Get the color pair for current number
        major_color, minor_color = get_color_from_pair_number(pair_number)
        
        # Format each line with consistent column alignment
        # :2d formats pair number with 2 digits, :<11 left-aligns major color in 11 chars
        manual += f"{pair_number:2d}          | {major_color:<11} | {minor_color}\n"
    
    return manual
