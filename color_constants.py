"""
Color constants for 25-pair color code used in telecommunications cables.

This module defines the color combinations used in the 25-pair color code
standard for identifying wires in telecommunications and electrical cables.
Each wire pair consists of a major color and a minor color.

For more details, refer to: https://en.wikipedia.org/wiki/25-pair_color_code
"""

# Major colors used in the 25-pair color code (5 colors total)
# These form the primary color identification for wire pairs
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']

# Minor colors used in the 25-pair color code (5 colors total)  
# These form the secondary color identification for wire pairs
# Combined with major colors, they create 25 unique pairs (5 x 5 = 25)
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
