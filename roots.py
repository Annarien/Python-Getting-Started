"""Following the work done on exceptions in the course Core Python: Getting Started @
https://app.pluralsight.com/course-player?clipId=3d633e59-17e3-47ff-8063-6c1bf4e1f8ab"""

# imports
import sys

def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x.
    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError(f"Cannot compute the square root of a negative number {x}")
    guess = x
    i = 0
    while guess * guess != x and i < 20:        # 'and' operator tests that both conditions are met
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))                           # raises a zero division error (-1 + (-1/-1))/2.0 = (-1+1)/2.0 = 0/2
    except ValueError as e:                       # catches ValueError
        print(e, file = sys.stderr)               # print the exception

    print("Program executes normally here")


if __name__ == '__main__':
    main()