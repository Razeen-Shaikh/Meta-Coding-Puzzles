"""ABCs"""

def get_sum(a: int, b: int, c: int) -> int:
    """
    Given three integers A, B, and C, determine their sum.
    Your task is to implement the function getSum(A, B, C) which returns the sum A+B+C.

    Args:
        a: integer
        b: integer
        c: integer
    
    Returns:
        integer
    """
    return a + b + c


get_sum(1, 2, 3)
get_sum(100, 100, 100)
get_sum(85, 16, 93)
