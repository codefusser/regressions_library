from math import asin, pi
from library.statistics.sort import sort
from library.statistics.rounding import rounding

def sinusoidal(first_constant, second_constant, third_constant, fourth_constant, precision):
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
            rounded_initial_value = rounding(initial_value, precision)
            rounded_periodic_unit = rounding(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        elif ratio == 1 or ratio == -1:
            periodic_unit = 2 * pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounding(initial_value, precision)
            rounded_periodic_unit = rounding(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, general_form]
        else:
            periodic_unit = 2 * pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounding(initial_value, precision)
            rounded_periodic_unit = rounding(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            alternative_initial_value = third_constant + pi / second_constant - periodic_radians
            alternative_first_value = alternative_initial_value + 1 * periodic_unit
            alternative_second_value = alternative_initial_value + 2 * periodic_unit
            rounded_alternative_initial_value = rounding(alternative_initial_value, precision)
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
    sorted_roots = sort(numerical_roots)
    rounded_roots = []
    for number in sorted_roots:
        rounded_roots.append(rounding(number, precision))
    result = rounded_roots + other_roots
    return result

test_case = sinusoidal(3, 2, 1, 1, 4)
print(test_case)
# [0.8301, 2.7407, 3.9717, 5.8823, 7.1133, 9.0239, '0.8300815452729391 + 3.141592653589793k', '2.7407147815219575 + 3.141592653589793k']