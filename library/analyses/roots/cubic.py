from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value
from library.errors.scalars import four_scalars, positive_integer

def cubic_roots(first_constant, second_constant, third_constant, fourth_constant, precision):
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    positive_integer(precision)
    roots = []
    xi = (-1 + (-3)**(1/2)) / 2
    delta_first = second_constant**2 - 3 * first_constant * third_constant
    delta_second = 2 * second_constant**3 - 9 * first_constant * second_constant * third_constant + 27 * first_constant**2 * fourth_constant
    discriminant = delta_second**2 - 4 * delta_first**3
    zeta_first = ((delta_second + discriminant**(1/2)) / 2)**(1/3)
    zeta_second = ((delta_second - discriminant**(1/2)) / 2)**(1/3)
    zeta = 0
    if zeta_first == 0:
        zeta = zeta_second
    else:
        zeta = zeta_first
    first_root = (-1 / (3 * first_constant)) * (second_constant + zeta * xi**0 + delta_first / (zeta * xi**0))
    second_root = (-1 / (3 * first_constant)) * (second_constant + zeta * xi**1 + delta_first / (zeta * xi**1))
    third_root = (-1 / (3 * first_constant)) * (second_constant + zeta * xi**2 + delta_first / (zeta * xi**2))
    first_real = first_root.real
    second_real = second_root.real
    third_real = third_root.real
    first_imag = first_root.imag
    second_imag = second_root.imag
    third_imag = third_root.imag
    size_first_imag = (first_imag**2)**(1/2)
    size_second_imag = (second_imag**2)**(1/2)
    size_third_imag = (third_imag**2)**(1/2)
    if size_first_imag < 0.0001:
        first_root = first_real
        roots.append(first_root)
    if size_second_imag < 0.0001:
        second_root = second_real
        roots.append(second_root)
    if size_third_imag < 0.0001:
        third_root = third_real
        roots.append(third_root)
    unique_roots = list(set(roots))
    if not unique_roots:
        unique_roots = [None]
    sorted_roots = sorted_list(unique_roots)
    result = []
    for number in sorted_roots:
        result.append(rounded_value(number, precision))
    return result