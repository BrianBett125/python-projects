"""
functional_utils.py

A collection of functional-style utilities that demonstrate
clean, reusable, and testable function design.

Written in a "senior-level" style: 
- clear type hints
- docstrings
- functional programming concepts
- error handling
- immutability emphasis
"""

from typing import Callable, Iterable, TypeVar, List, Any

T = TypeVar("T")
R = TypeVar("R")


def safe_apply(func: Callable[[T], R], value: T, default: Any = None) -> R:
    """
    Safely apply a function to a value.
    
    Args:
        func: The function to apply.
        value: The input value.
        default: Fallback if func raises an exception.
    
    Returns:
        Result of func(value) or the default if an error occurs.
    """
    try:
        return func(value)
    except Exception as e:
        print(f"⚠️ safe_apply caught error: {e}")
        return default


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Compose multiple functions into a single callable.
    
    Example:
        >>> f = compose(str.strip, str.upper)
        >>> f("  hello ")
        'HELLO'
    
    Args:
        *functions: Functions to compose, executed left-to-right.
    
    Returns:
        A function that applies all given functions in order.
    """
    def composed(value: Any) -> Any:
        for func in functions:
            value = func(value)
        return value
    
    return composed


def filter_and_map(
    data: Iterable[T], 
    condition: Callable[[T], bool], 
    transform: Callable[[T], R]
) -> List[R]:
    """
    Filter an iterable by a condition and map a transformation.
    
    Args:
        data: The iterable input.
        condition: A predicate function to filter elements.
        transform: A function to transform the filtered elements.
    
    Returns:
        A list of transformed results.
    """
    return [transform(item) for item in data if condition(item)]


# Example usage when running this file directly
if __name__ == "__main__":
    numbers = [1, -2, 3, -4, 5]

    # Safe apply example
    print(safe_apply(lambda x: 10 / x, 0, default="Division by zero"))

    # Compose example
    pipeline = compose(abs, float, lambda x: x ** 0.5)
    print(pipeline(-16))  # sqrt(16.0) → 4.0

    # Filter & map example
    result = filter_and_map(numbers, condition=lambda n: n > 0, transform=lambda n: n * 10)
    print(result)  # [10, 30, 50]

