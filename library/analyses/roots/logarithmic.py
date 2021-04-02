from math import exp
from library.errors.scalars import two_scalars, positive_integer
from library.statistics.rounding import rounded_value

def logarithmic_roots(first_constant, second_constant, precision):
    """
    Calculates the roots of a logarithmic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the logarithmic term of the original logarithmic function
    second_constant : int or float
        Coefficient of the constant term of the original logarithmic function
    precision : int
        Maximum number of digits that can appear after the decimal place of the resultant roots

    Raises
    ------
    TypeError
        First two arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    roots : list
        List of the x-coordinates of all of the x-intercepts of the original function

    Examples
    --------
    Calculate the roots of a logarithmic function with coefficients 2 and 3 (and round roots to four decimal places)
        >>> test = logarithmic_roots(2, 3, 4)
    Print the roots
        >>> print(test)
        [0.2231]
    """
    two_scalars(first_constant, second_constant)
    positive_integer
    root = exp(-1 * second_constant / first_constant)
    result = [rounded_value(root, precision)]
    return result