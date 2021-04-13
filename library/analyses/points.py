from library.errors.analyses import select_equations
from library.errors.scalars import scalar_value, compare_scalars, positive_integer
from library.errors.vectors import vector_of_scalars
from library.errors.matrices import allow_none_matrix
from library.statistics.rounding import rounded_value
from library.statistics.sort import sorted_list
from library.vectors.unify import unite_vectors
from .equations.linear import linear_equation
from .equations.quadratic import quadratic_equation
from .equations.cubic import cubic_equation
from .equations.hyperbolic import hyperbolic_equation
from .equations.exponential import exponential_equation
from .equations.logarithmic import logarithmic_equation
from .equations.logistic import logistic_equation
from .equations.sinusoidal import sinusoidal_equation
from .intercepts import intercept_points
from .extrema import extrema_points
from .inflections import inflection_points

def key_coordinates(equation_type, coefficients, precision = 4):
    """
    Calculates the key points of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which key points must be determined (e.g., 'linear', 'quadratic')
    coefficients : list
        Coefficients to use to generate the equation to investigate
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points['roots'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a root; second elements of those lists will be 0; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but general forms will also be included; if the function has no roots, then it will return a list of `None`
    points['maxima'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a relative maximum; second elements of those lists will be the y-coordinate of that maximum; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form will also be included; if the function has no maxima, then it will return a list of `None`
    points['minima'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a relative minimum; second elements of those lists will be the y-coordinate of that minimum; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form will also be included; if the function has no minima, then it will return a list of `None`
    points['inflections'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has an inflection; second elements of those lists will be the y-coordinate of that inflection; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form will also be included; if the function has no inflection points, then it will return a list of `None`

    See Also
    --------
    - Roots for key functions: :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`
    - Graphical analysis: :func:`~library.analyses.criticals.critical_points`, :func:`~library.analyses.intervals.sign_chart`, :func:`~library.analyses.maxima.maxima_points`, :func:`~library.analyses.minima.minima_points`, :func:`~library.analyses.extrema.extrema_points`, :func:`~library.analyses.inflections.inflection_points`

    Notes
    -----
    - Key points include x-intercepts, maxima, minima, and points of inflection
    - |intercepts|
    - |extrema|
    - |inflections|

    Examples
    --------
    Calculate the key points of a cubic function with coefficients 1, -15, 63, and -7
        >>> points_cubic = key_coordinates('cubic', [1, -15, 63, -7])
        >>> print(points_cubic['roots'])
        [[0.1142, 0]]
        >>> print(points_cubic['maxima'])
        [[3.0, 74.0]]
        >>> print(points_cubic['minima'])
        [[7.0, 42.0]]
        >>> print(points_cubic['inflections'])
        [[5.0, 58.0]]
    Calculate the key points of a sinusoidal function with coefficients 2, 3, 5, and 1
        >>> points_sinusoidal = key_coordinates('sinusoidal', [2, 3, 5, 1])
        >>> print(points_sinusoidal['roots'])
        [[4.8255, 0], [6.2217, 0], [6.9199, 0], [8.3161, 0], [9.0143, 0], [10.4105, 0], ['4.8255 + 2.0944k', 0], ['6.2217 + 2.0944k', 0]]
        >>> print(points_sinusoidal['maxima'])
        [[5.5236, 3.0], [7.618, 3.0], [9.7124, 3.0], ['5.5236 + 2.0944k', 3.0]]
        >>> print(points_sinusoidal['minima'])
        [[6.5708, -1.0], [8.6652, -1.0], ['6.5708 + 2.0944k', -1.0]]
        >>> print(points_sinusoidal['inflections'])
        [[5, 1.0], [6.0472, 1.0], [7.0944, 1.0], [8.1416, 1.0], [9.1888, 1.0001], ['5 + 1.0472k', 1.0]]
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    positive_integer(precision)
    intercepts_inputs = intercept_points(equation_type, coefficients, precision)
    equation = lambda x : x
    if equation_type == 'linear':
        equation = linear_equation(*coefficients)
    elif equation_type == 'quadratic':
        equation = quadratic_equation(*coefficients)
    elif equation_type == 'cubic':
        equation = cubic_equation(*coefficients)
    elif equation_type == 'hyperbolic':
        equation = hyperbolic_equation(*coefficients)
    elif equation_type == 'exponential':
        equation = exponential_equation(*coefficients)
    elif equation_type == 'logarithmic':
        equation = logarithmic_equation(*coefficients)
    elif equation_type == 'logistic':
        equation = logistic_equation(*coefficients)
    elif equation_type == 'sinusoidal':
        equation = sinusoidal_equation(*coefficients)
    extrema_inputs = extrema_points(equation_type, coefficients, precision)
    maxima_inputs = extrema_inputs['maxima']
    minima_inputs = extrema_inputs['minima']
    inflections_inputs = inflection_points(equation_type, coefficients, precision)
    intercepts_outputs = []
    maxima_outputs = []
    minima_outputs = []
    inflections_outputs = []
    intercepts_coordinates = []
    maxima_coordinates = []
    minima_coordinates = []
    inflections_coordinates = []
    if intercepts_inputs[0] == None:
        intercepts_coordinates = [None]
    else:
        for intercept in intercepts_inputs:
            intercepts_outputs.append(0.0)
        intercepts_coordinates = unite_vectors(intercepts_inputs, intercepts_outputs)
    if maxima_inputs[0] == None:
        maxima_coordinates = [None]
    else:
        for i in range(len(maxima_inputs)):
            if isinstance(maxima_inputs[i], (int, float)):
                output = equation(maxima_inputs[i])
                rounded_output = rounded_value(output, precision)
                maxima_outputs.append(rounded_output)
            else:
                periodic_unit = 2 * float(maxima_inputs[i][:-1])
                initial_value = maxima_inputs[0]
                general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
                maxima_inputs[i] = general_form
                maxima_outputs.append(maxima_outputs[0])
        maxima_coordinates = unite_vectors(maxima_inputs, maxima_outputs)
    if minima_inputs[0] == None:
        minima_coordinates = [None]
    else:
        for i in range(len(minima_inputs)):
            if isinstance(minima_inputs[i], (int, float)):
                output = equation(minima_inputs[i])
                rounded_output = rounded_value(output, precision)
                minima_outputs.append(rounded_output)
            else:
                periodic_unit = 2 * float(minima_inputs[i][:-1])
                initial_value = minima_inputs[0]
                general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
                minima_inputs[i] = general_form
                minima_outputs.append(minima_outputs[0])
        minima_coordinates = unite_vectors(minima_inputs, minima_outputs)
    if inflections_inputs[0] == None:
        inflections_coordinates = [None]
    else:
        for inflection in inflections_inputs:
            if isinstance(inflection, (int, float)):
                output = equation(inflection)
                rounded_output = rounded_value(output, precision)
                inflections_outputs.append(rounded_output)
            else:
                inflections_outputs.append(inflections_outputs[0])
        inflections_coordinates = unite_vectors(inflections_inputs, inflections_outputs)
    result = {
        'roots': intercepts_coordinates,
        'maxima': maxima_coordinates,
        'minima': minima_coordinates,
        'inflections': inflections_coordinates
    }
    return result

def points_within_range(coordinates, minimum, maximum, interval, precision = 4):
    allow_none_matrix(coordinates, 'first')
    compare_scalars(minimum, maximum, 'second', 'third')
    scalar_value(interval, 'fourth')
    positive_integer(precision)
    final_points = []
    if coordinates[0] is not None:
        general_points = []
        for point in coordinates:
            if isinstance(point[0], str):
                general_points.append(point[0])
        optional_points = []
        for point in general_points:
            initial_value_index = point.find(' + ')
            initial_value = float(point[:initial_value_index])
            periodic_unit_index = initial_value_index + 3
            periodic_unit = float(point[periodic_unit_index:-1])
            if periodic_unit > 0:
                while initial_value > maximum:
                    initial_value -= periodic_unit
                while initial_value < minimum:
                    initial_value += periodic_unit
            else:
                while initial_value > maximum:
                    initial_value += periodic_unit
                while initial_value < minimum:
                    initial_value -= periodic_unit
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            optional_points += [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        numerical_points = []
        other_points = []
        for point in optional_points:
            if isinstance(point, (int, float)):
                numerical_points.append(point)
            else:
                other_points.append(point)
        sorted_points = sorted_list(numerical_points)
        selected_points = [x for x in sorted_points if x >= sorted_points[0] and x <= sorted_points[0] + interval]
        rounded_points = []
        for point in selected_points:
            rounded_points.append(rounded_value(point, precision))
        sorted_other_points = []
        if len(other_points) > 0:
            if len(other_points) == 1:
                sorted_other_points = other_points
            else:
                first_index = other_points[0].find(' + ') - 1
                first_value = float(other_points[0][:first_index])
                second_index = other_points[1].find(' + ') - 1
                second_value = float(other_points[1][:second_index])
                if first_value < second_value:
                    sorted_other_points = other_points
                else:
                    sorted_other_points = [other_points[1], other_points[0]]
        input_points = rounded_points + sorted_other_points
        output_points = []
        for point in input_points:
            output_points.append(coordinates[0][1])
        final_points = unite_vectors(input_points, output_points)
    else:
        final_points = coordinates
    return final_points