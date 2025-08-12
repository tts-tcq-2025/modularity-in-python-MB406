
"""
Main entry point for the 25-pair color code application.

This application provides functionality for working with the 25-pair color code
used in telecommunications cables. It demonstrates the modular design by:
1. Running comprehensive tests to verify functionality
2. Generating a printable reference manual for field technicians

The application serves as both a validation tool and a practical utility
for telecommunications wiring personnel.
"""

from test_color_coding import run_all_tests
from color_manual import format_color_reference_manual


if __name__ == '__main__':
    """
    Main execution block that orchestrates the application workflow.
    
    This block executes when the script is run directly (not imported).
    It performs the following operations in sequence:
    1. Validates all conversion functions through comprehensive testing
    2. Generates and displays the color reference manual
    3. Confirms successful completion
    """
    # Execute all test cases to ensure functionality works correctly
    # This validates both number-to-color and color-to-number conversions
    run_all_tests()
    
    # Generate and display the color reference manual for printing
    # This provides a practical tool for field technicians
    print("\n" + format_color_reference_manual())
    
    # Indicate successful completion of all operations
    print('Done :)')
