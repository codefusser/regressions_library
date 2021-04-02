from math import asin, pi
from library.errors.scalars import four_scalars, positive_integer
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value

def sinusoidal_roots(first_constant, second_constant, third_constant, fourth_constant, precision):
    """
    Calculates the roots of a sinusoidal function

    Parameters
    ----------
    first_constant : int or float
        Vertical stretch factor of the original sine function
    second_constant : int or float
        Horizontal stretch factor of the original sine function
    third_constant : int or float
        Horizontal shift of the original sine function
    fourth_constant : int or float
        Vertical shift of the original sine function
    precision : int
        Maximum number of digits that can appear after the decimal place of the resultant roots

    Raises
    ------
    TypeError
        First four arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    roots : list
        List of the x-coordinates of all of the x-intercepts of the original function; if the function never crosses the x-axis, then it will return a list of `None`

    Examples
    --------
    Calculate the roots of a sinusoidal function with coefficients 2, 3, 5, and 7 (and round roots to four decimal places)
        >>> test = sinusoidal_roots(2, 3, 5, 7, 4)
    Print the roots
        >>> print(test)
        [None]
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    positive_integer(precision)
    roots = []
    ratio = -1 * fourth_constant / first_constant
    if ratio > 1 or ratio < -1:
        roots = [None]
    else:
        radians = asin(ratio)
        periodic_radians = radians / second_constant
        if ratio == 0:
            periodic_unit = pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        elif ratio == 1 or ratio == -1:
            periodic_unit = 2 * pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, general_form]
        else:
            periodic_unit = 2 * pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            alternative_initial_value = third_constant + pi / second_constant - periodic_radians
            alternative_first_value = alternative_initial_value + 1 * periodic_unit
            alternative_second_value = alternative_initial_value + 2 * periodic_unit
            rounded_alternative_initial_value = rounded_value(alternative_initial_value, precision)
            alternative_general_form = str(rounded_alternative_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, alternative_initial_value, alternative_first_value, alternative_second_value, general_form, alternative_general_form]
    if not roots:
        roots = [None]
    numerical_roots = []
    other_roots = []
    for item in roots:
        if isinstance(item, (int, float)):
            numerical_roots.append(item)
        else:
            other_roots.append(item)
    sorted_roots = sorted_list(numerical_roots)
    rounded_roots = []
    for number in sorted_roots:
        rounded_roots.append(rounded_value(number, precision))
    result = rounded_roots + other_roots
    return result