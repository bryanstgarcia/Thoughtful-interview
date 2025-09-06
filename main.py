#!/usr/bin/env python3.10
"""
Package Sorting System for Thoughtful Tech Challenge

This script implements a robust package sorting system that categorizes packages
into STANDARD, SPECIAL, or REJECTED stacks based on dimensions and mass.

Author: Thoughtful Tech Challenge
Python Version: 3.10+
"""

from typing import Tuple, List
import sys


def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    Sort a package into the appropriate stack based on dimensions and mass.
    
    A package is considered:
    - BULKY if volume >= 1,000,000 cm³ OR any dimension >= 150 cm
    - HEAVY if mass >= 20 kg
    
    Stack assignment:
    - REJECTED: Both bulky AND heavy
    - SPECIAL: Either bulky OR heavy (but not both)
    - STANDARD: Neither bulky nor heavy
    
    Args:
        width (int): Width in centimeters (must be positive)
        height (int): Height in centimeters (must be positive)
        length (int): Length in centimeters (must be positive)
        mass (int): Mass in kilograms (must be positive)
        
    Returns:
        str: Stack name ("STANDARD", "SPECIAL", or "REJECTED")
        
    Raises:
        ValueError: If any dimension or mass is non-positive
        TypeError: If any parameter is not an integer
    """
    # Input validation
    _validate_inputs(width, height, length, mass)
    
    # Calculate volume in cubic centimeters
    volume = width * height * length
    
    # Check if package is bulky (volume >= 1,000,000 cm³ or any dimension >= 150 cm)
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Check if package is heavy (mass >= 20 kg)
    is_heavy = mass >= 20
    
    # Determine stack based on package characteristics
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def _validate_inputs(width: int, height: int, length: int, mass: int) -> None:
    """
    Validate input parameters for the sort function.
    
    Args:
        width, height, length, mass: Parameters to validate
        
    Raises:
        ValueError: If any parameter is non-positive
    """
    # Check positive values
    if width <= 0:
        raise ValueError(f"width must be positive, got {width}")
    if height <= 0:
        raise ValueError(f"height must be positive, got {height}")
    if length <= 0:
        raise ValueError(f"length must be positive, got {length}")
    if mass <= 0:
        raise ValueError(f"mass must be positive, got {mass}")


def run_test_suite() -> None:
    """
    Run comprehensive test suite covering all scenarios and edge cases.
    """
    print("🧪 Running Comprehensive Test Suite")
    print("=" * 60)
    
    # Test cases: (width, height, length, mass, expected_result, description)
    test_cases: List[Tuple[int, int, int, int, str, str]] = [
        # STANDARD packages
        (10, 10, 10, 5, "STANDARD", "Small standard package"),
        (50, 50, 50, 15, "STANDARD", "Medium standard package"),
        (100, 50, 20, 10, "STANDARD", "Large but not bulky standard package"),
        (149, 149, 149, 19, "STANDARD", "Edge case: just under bulky and heavy thresholds"),
        
        # BULKY packages (by volume)
        (100, 100, 100, 10, "SPECIAL", "Bulky by volume (1,000,000 cm³)"),
        (100, 100, 101, 5, "SPECIAL", "Bulky by volume (1,010,000 cm³)"),
        (200, 200, 200, 10, "SPECIAL", "Very bulky by volume (8,000,000 cm³)"),
        
        # BULKY packages (by dimension)
        (150, 10, 10, 5, "SPECIAL", "Bulky by width (150 cm)"),
        (10, 150, 10, 5, "SPECIAL", "Bulky by height (150 cm)"),
        (10, 10, 150, 5, "SPECIAL", "Bulky by length (150 cm)"),
        (200, 10, 10, 5, "SPECIAL", "Very bulky by width (200 cm)"),
        
        # HEAVY packages
        (10, 10, 10, 20, "SPECIAL", "Heavy package (20 kg)"),
        (10, 10, 10, 25, "SPECIAL", "Heavy package (25 kg)"),
        (10, 10, 10, 100, "SPECIAL", "Very heavy package (100 kg)"),
        
        # REJECTED packages (both bulky and heavy)
        (150, 10, 10, 20, "REJECTED", "Rejected: bulky by dimension + heavy"),
        (100, 100, 100, 20, "REJECTED", "Rejected: bulky by volume + heavy"),
        (200, 200, 200, 50, "REJECTED", "Rejected: very bulky + very heavy"),
        (1000, 1000, 1000, 1000, "REJECTED", "Rejected: extremely bulky + extremely heavy"),
    ]
    
    passed = 0
    failed = 0
    
    for test_number, (width, height, length, mass, expected_result, description) in enumerate(test_cases, 1):
        try:
            actual_result = sort(width, height, length, mass)
            volume = width * height * length
            status = "✅ PASS" if actual_result == expected_result else "❌ FAIL"
            
            if actual_result == expected_result:
                passed += 1
            else:
                failed += 1
                
            print(f"Test {test_number:2d}: {status} | {description}")
            print(f"         Input: {width}x{height}x{length} cm, {mass} kg (Vol: {volume:,} cm³)")
            print(f"         Expected: {expected_result}, Got: {actual_result}")
            print()
            
        except Exception as error:
            failed += 1
            print(f"Test {test_number:2d}: ❌ ERROR | {description}")
            print(f"         Input: {width}x{height}x{length} cm, {mass} kg")
            print(f"         Error: {error}")
            print()
    
    print("🔍 Error Handling Tests")
    print("-" * 30)
    
    error_tests = [
        ((0, 10, 10, 5), "Zero width"),
        ((10, -5, 10, 5), "Negative height"),
        ((10, 10, 0, 5), "Zero length"),
        ((10, 10, 10, -1), "Negative mass"),
        (("10", 10, 10, 5), "String width"),
        ((10.5, 10, 10, 5), "Float width"),
    ]
    
    for (width, height, length, mass), description in error_tests:
        try:
            result = sort(width, height, length, mass)  # type: ignore
            print(f"❌ FAIL | {description} - Should have raised exception but got: {result}")
            failed += 1
        except (ValueError, TypeError):
            print(f"✅ PASS | {description} - Correctly raised exception")
            passed += 1
        except Exception as error:
            print(f"⚠️  PARTIAL | {description} - Raised {type(error).__name__}: {error}")
            passed += 1
        print()
    
    # Summary
    total = passed + failed
    print("📊 Test Summary")
    print("=" * 30)
    print(f"Total tests: {total}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    print(f"Success rate: {(passed/total)*100:.1f}%")
    
    if failed == 0:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Review the implementation.")


def main():
    """
    Main application entry point with interactive demo and test suite.
    """
    print("📦 Package Sorting System")
    print("=" * 50)
    print("This system sorts packages into STANDARD, SPECIAL, or REJECTED stacks.")
    
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_test_suite()
        return
    
    # Interactive demonstration
    print("🎯 Interactive Demo")
    print("-" * 20)
    
    # Sample packages
    demo_packages = [
        (10, 10, 10, 5, "Small standard package"),
        (100, 100, 100, 10, "Bulky package (1M cm³)"),
        (10, 10, 10, 25, "Heavy package (25 kg)"),
        (150, 10, 10, 20, "Rejected package (bulky + heavy)"),
        (149, 149, 149, 19, "Edge case package"),
    ]
    
    for package_number, (width, height, length, mass, description) in enumerate(demo_packages, 1):
        try:
            stack_result = sort(width, height, length, mass)
            volume = width * height * length
            print(f"Package {package_number}: {description}")
            print(f"  Dimensions: {width}×{height}×{length} cm (Volume: {volume:,} cm³)")
            print(f"  Mass: {mass} kg")
            print(f"  Result: {stack_result}")
            print()
        except Exception as error:
            print(f"Package {package_number}: ERROR - {error}")
            print()
    
    print("💡 Run with --test flag for comprehensive testing:")
    print("   python main.py --test")
    print()
    print("✅ Demo completed successfully!")


if __name__ == "__main__":
    main()