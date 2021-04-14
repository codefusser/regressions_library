from math import pi
from numpy import sin, inf
from scipy.optimize import curve_fit
from library.errors.matrices import matrix_of_scalars
from library.errors.vectors import long_vector
from library.errors.scalars import positive_integer
from library.errors.adjustments import no_zeroes
from library.vectors.dimension import single_dimension
from library.vectors.unify import unite_vectors
from library.analyses.equations.sinusoidal import sinusoidal_equation
from library.analyses.derivatives.sinusoidal import sinusoidal_derivatives
from library.analyses.integrals.sinusoidal import sinusoidal_integral
from library.analyses.points import key_coordinates, points_within_range
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.halve import half_dimension
from library.statistics.mean import mean_value
from library.statistics.summary import five_number_summary
from library.statistics.sort import sorted_list
from library.statistics.correlation import correlation_coefficient
from library.statistics.rounding import rounded_value

def sinusoidal_model(data, precision = 4):
    """
    Generates a sinusoidal regression model from a given data set

    Parameters
    ----------
    data : list
        List of lists of numbers representing a collection of coordinate pairs
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        First argument must contain at least 10 elements
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    model['constants'] : list
        Coefficients of the resultant sinusoidal model; the first element is the vertical stretch factor, the second element is the horizontal stretch factor, the third element is the horizontal shift, and the fourth element is the vertical shift
    model['evaluations']['equation'] : function
        Function that evaluates the equation of the sinusoidal model at a given numeric input (e.g., model['evaluations']['equation'](10) would evaluate the equation of the sinusoidal model when the independent variable is 10)
    model['evaluations']['derivative'] : function
        Function that evaluates the first derivative of the sinusoidal model at a given numeric input (e.g., model['evaluations']['derivative'](10) would evaluate the first derivative of the sinusoidal model when the independent variable is 10)
    model['evaluations']['integral'] : function
        Function that evaluates the integral of the sinusoidal model at a given numeric input (e.g., model['evaluations']['integral'](10) would evaluate the integral of the sinusoidal model when the independent variable is 10)
    model['points']['roots'] : list
        List of lists of numbers representing the coordinate pairs of all the x-intercepts of the sinusoidal model (will contain either `None` or an initial set of points within two periods along with general terms for finding the other points)
    model['points']['maxima'] : list
        List of lists of numbers representing the coordinate pairs of all the maxima of the sinusoidal model (will contain an initial set of points within two periods along with a general term for finding the other points)
    model['points']['minima'] : list
        List of lists of numbers representing the coordinate pairs of all the minima of the sinusoidal model (will contain an initial set of points within two periods along with a general term for finding the other points)
    model['points']['inflections'] : list
        List of lists of numbers representing the coordinate pairs of all the inflection points of the sinusoidal model (will contain an initial set of points within two periods along with a general term for finding the other points)
    model['accumulations']['range'] : float
        Total area under the curve represented by the sinusoidal model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (i.e., over the range)
    model['accumulations']['iqr'] : float
        Total area under the curve represented by the sinusoidal model between the first and third quartiles of all the independent coordinates originally provided (i.e., over the interquartile range)
    model['averages']['range']['average_value_derivative'] : float
        Average rate of change of the curve represented by the sinusoidal model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_derivative'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['range']['average_value_integral'] : float
        Average value of the curve represented by the sinusoidal model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_integral'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their value equals the function's average value over that interval
    model['averages']['iqr']['average_value_derivative'] : float
        Average rate of change of the curve represented by the sinusoidal model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_derivative'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['iqr']['average_value_integral'] : float
        Average value of the curve represented by the sinusoidal model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_integral'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their value equals the function's average value over that interval
    model['correlation'] : float
        Correlation coefficient indicating how well the model fits the original data set (values range between 0.0, implying no fit, and 1.0, implying a perfect fit)

    See Also
    --------
    :func:`~library.analyses.equations.sinusoidal.sinusoidal_equation`, :func:`~library.analyses.derivatives.sinusoidal.sinusoidal_derivatives`, :func:`~library.analyses.integrals.sinusoidal.sinusoidal_integral`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`, :func:`~library.statistics.correlation.correlation_coefficient`, :func:`~library.execute.run_all`

    Notes
    -----
    - Provided ordered pairs for the data set: :math:`p_i = \\{ (p_{1,x}, p_{1,y}), (p_{2,x}, p_{2,y}), \\cdots, (p_{n,x}, p_{n,y}) \\}`
    - Provided values for the independent variable: :math:`X_i = \\{ p_{1,x}, p_{2,x}, \\cdots, p_{n,x} \\}`
    - Provided values for the dependent variable: :math:`Y_i = \\{ p_{1,y}, p_{2,y}, \\cdots, p_{n,y} \\}`
    - Minimum value of the provided values for the independent variable: :math:`X_{min} \\leq p_{j,x}, \\forall p_{j,x} \\in X_i`
    - Maximum value of the provided values for the independent variable: :math:`X_{max} \\geq p_{j,x}, \\forall p_{j,x} \\in X_i`
    - First quartile of the provided values for the independent variable: :math:`X_{Q1}`
    - Third quartile of the provided values for the independent variable: :math:`X_{Q3}`
    - Mean of all provided values for the dependent variable: :math:`\\bar{y} = \\frac{1}{n}\\cdot{\\sum\\limits_{i=1}^n Y_i}`
    - Resultant values for the coefficients of the sinusoidal model: :math:`C_i = \\{ a, b, c, d \\}`
    - Standard form for the equation of the sinusoidal model: :math:`f(x) = a\\cdot{\\sin(b\\cdot(x - c))} + d`
    - First derivative of the sinusoidal model: :math:`f'(x) = ab\\cdot{\\cos(b\\cdot(x - c))}`
    - Second derivative of the sinusoidal model: :math:`f''(x) = -ab^2\\cdot{\\sin(b\\cdot(x - c))}`
    - Integral of the sinusoidal model: :math:`F(x) = -\\frac{a}{b}\\cdot{\\cos(b\\cdot(x - c))} + d\\cdot{x}`
    - Potential x-values of the roots of the sinusoidal model: :math:`x_{intercepts} = \\{ c + \\frac{1}{b}\\cdot{\\left(\\sin^{-1}(-\\frac{d}{a}) + 2\\pi\\cdot{k} \\right)}, c + \\frac{1}{b}\\cdot{\\left(-\\sin^{-1}(-\\frac{d}{a}) + \\pi\\cdot(2k - 1) \\right)}, \\\\ c - \\frac{\\pi}{b}\\cdot(2k - 1) \\}`
        
        - :math:`k \\in \\mathbb{Z}`

    - Potential x-values of the maxima of the sinusoidal model: :math:`x_{maxima} = \\{ c + \\frac{\\pi}{b}\\cdot(\\frac{1}{2} + k) \\}`

        - :math:`k \\in \\mathbb{Z}`

    - Potential x-values of the minima of the sinusoidal model: :math:`x_{maxima} = \\{ c + \\frac{\\pi}{b}\\cdot(\\frac{1}{2} + k) \\}`

        - :math:`k \\in \\mathbb{Z}`

    - Potential x-values of the inflection points of the sinusoidal model: :math:`x_{inflections} = \\{ c + \\frac{\\pi}{b}\\cdot{k} \\}`

        - :math:`k \\in \\mathbb{Z}`

    - Accumulatation of the sinusoidal model over its range: :math:`A_{range} = \\int_{X_{min}}^{X_{max}} f(x) \\,dx`
    - Accumulatation of the sinusoidal model over its interquartile range: :math:`A_{iqr} = \\int_{X_{Q1}}^{X_{Q3}} f(x) \\,dx`
    - Average rate of change of the sinusoidal model over its range: :math:`m_{range} = \\frac{f(X_{max}) - f(X_{min})}{X_{max} - X_{min}}`
    - Potential x-values at which the sinusoidal model's instantaneous rate of change equals its average rate of change over its range: :math:`x_{m,range} = \\{ c + \\frac{1}{b}\\cdot{\\left(\\cos^{-1}(\\frac{m_{range}}{ab}) + \\pi\\cdot{k} \\right)}, c + \\frac{1}{b}\\cdot{\\left(-\\cos^{-1}(\\frac{m_{range}}{ab}) + 2\\pi\\cdot{k} \\right)} \\}`

        - :math:`k \\in \\mathbb{Z}`
    
    - Average value of the sinusoidal model over its range: :math:`v_{range} = \\frac{1}{X_{max} - X_{min}}\\cdot{A_{range}}`
    - Potential x-values at which the sinusoidal model's value equals its average value over its range: :math:`x_{v,range} = \\{ c + \\frac{1}{b}\\cdot{\\left(\\sin^{-1}(-\\frac{d - v_{range}}{a}) + 2\\pi\\cdot{k} \\right)}, c + \\frac{1}{b}\\cdot{\\left(-\\sin^{-1}(-\\frac{d - v_{range}}{a}) + \\pi\\cdot(2k - 1) \\right)}, \\\\ c + \\frac{\\pi}{b}\\cdot(2k - 1) \\}`

        - :math:`k \\in \\mathbb{Z}`

    - Average rate of change of the sinusoidal model over its interquartile range: :math:`m_{iqr} = \\frac{f(X_{Q3}) - f(X_{Q1})}{X_{Q3} - X_{Q1}}`
    - Potential x-values at which the sinusoidal model's instantaneous rate of change equals its average rate of change over its interquartile range: :math:`x_{m,iqr} = \\{ c + \\frac{1}{b}\\cdot{\\left(\\cos^{-1}(\\frac{m_{iqr}}{ab}) + \\pi\\cdot{k} \\right)}, c + \\frac{1}{b}\\cdot{\\left(-\\cos^{-1}(\\frac{m_{iqr}}{ab}) + 2\\pi\\cdot{k} \\right)} \\}`

        - :math:`k \\in \\mathbb{Z}`

    - Average value of the sinusoidal model over its interquartile range: :math:`v_{iqr} = \\frac{1}{X_{Q3} - X_{Q1}}\\cdot{A_{iqr}}`
    - Potential x-values at which the sinusoidal model's value equals its average value over its interquartile range: :math:`x_{v,iqr} = \\{ c + \\frac{1}{b}\\cdot{\\left(\\sin^{-1}(-\\frac{d - v_{iqr}}{a}) + 2\\pi\\cdot{k} \\right)}, c + \\frac{1}{b}\\cdot{\\left(-\\sin^{-1}(-\\frac{d - v_{iqr}}{a}) + \\pi\\cdot(2k - 1) \\right)}, \\\\ c + \\frac{\\pi}{b}\\cdot(2k - 1) \\}`

        - :math:`k \\in \\mathbb{Z}`

    - Predicted values based on the sinusoidal model: :math:`\\hat{y}_i = \\{ \\hat{y}_1, \\hat{y}_2, \\cdots, \\hat{y}_n \\}`
    - Residuals of the dependent variable: :math:`e_i = \\{ p_{1,y} - \\hat{y}_1, p_{2,y} - \\hat{y}_2, \\cdots, p_{n,y} - \\hat{y}_n \\}`
    - Deviations of the dependent variable: :math:`d_i = \\{ p_{1,y} - \\bar{y}, p_{2,y} - \\bar{y}, \\cdots, p_{n,y} - \\bar{y} \\}`
    - Sum of squares of residuals: :math:`SS_{res} = \\sum\\limits_{i=1}^n e_i^2`
    - Sum of squares of deviations: :math:`SS_{dev} = \\sum\\limits_{i=1}^n d_i^2`
    - Correlation coefficient for the sinusoidal model: :math:`r = \\sqrt{1 - \\frac{SS_{res}}{SS_{dev}}}`
    - |regression_analysis|

    Examples
    --------
    Generate a sinusoidal regression model for the data set [[1, 3], [2, 8], [3, 3], [4, -2], [5, 3], [6, 8], [7, 3], [8, -2], [9, 3], [10, 8]], then print its coefficients, roots, total accumulation over its interquartile range, and correlation
        >>> model_perfect = sinusoidal_model([[1, 3], [2, 8], [3, 3], [4, -2], [5, 3], [6, 8], [7, 3], [8, -2], [9, 3], [10, 8]])
        >>> print(model_perfect['constants'])
        [-5.0, 1.5708, 3.0, 3.0]
        >>> print(model_perfect['points']['roots'])
        [[3.4097, 0], [4.5903, 0], [7.4097, 0], [8.5903, 0], ['3.4097 + 4.0k', 0], ['4.5903 + 4.0k', 0]]
        >>> print(model_perfect['accumulations']['iqr'])
        11.8169
        >>> print(model_perfect['correlation'])
        1.0
    Generate a sinusoidal regression model for the data set [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], then print its coefficients, inflections, total accumulation over its range, and correlation
        >>> model_agnostic = sinusoidal_model([[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]])
        >>> print(model_agnostic['constants'])
        [14.0875, 0.7119, -3.7531, 34.2915]
        >>> print(model_agnostic['points']['inflections'])
        [[5.0727, 34.291], [9.4856, 34.291], [13.8985, 34.291], [18.3114, 34.291], ['5.0727 + 4.4129k', 34.291]]
        >>> print(model_agnostic['accumulations']['range'])
        307.8889
        >>> print(model_agnostic['correlation'])
        0.9264
    """
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    independent_max = max(independent_variable)
    independent_min = min(independent_variable)
    independent_range = independent_max - independent_min
    dependent_max = max(dependent_variable)
    dependent_min = min(dependent_variable)
    dependent_range = dependent_max - dependent_min
    if independent_range == 0:
        independent_range = 1
    if dependent_range == 0:
        dependent_range = 1
        dependent_min = 1
        dependent_max = 2
    solution = []
    def sinusoidal_fit(variable, first_constant, second_constant, third_constant, fourth_constant):
        evaluation = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return evaluation
    try:
        parameters, covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable, bounds=[(-dependent_range, -inf, -independent_range, dependent_min), (dependent_range, inf, independent_range, dependent_max)])
        solution = list(parameters)
    except RuntimeError:
        parameters, covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable, bounds=[(dependent_range - 1, -independent_range, -independent_range, dependent_min), (dependent_range + 1, independent_range, independent_range, dependent_max)])
        solution = list(parameters)
    coefficients = no_zeroes(solution, precision)
    equation = sinusoidal_equation(*coefficients)
    derivative = sinusoidal_derivatives(*coefficients)
    integral = sinusoidal_integral(*coefficients)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_coordinates('sinusoidal', coefficients, precision)
    interval = 2 * abs(2 * pi / coefficients[1])
    final_roots = points_within_range(points['roots'], independent_min, independent_max, interval, precision)
    final_maxima = points_within_range(points['maxima'], independent_min, independent_max, interval, precision)
    final_minima = points_within_range(points['minima'], independent_min, independent_max, interval, precision)
    final_inflections = points_within_range(points['inflections'], independent_min, independent_max, interval, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area('sinusoidal', coefficients, min_value, max_value, precision)
    accumulated_iqr = accumulated_area('sinusoidal', coefficients, q1, q3, precision)
    averages_range = average_values('sinusoidal', coefficients, min_value, max_value, precision)
    averages_iqr = average_values('sinusoidal', coefficients, q1, q3, precision)
    predicted = []
    for element in independent_variable:
        predicted.append(equation(element))
    accuracy = correlation_coefficient(dependent_variable, predicted, precision)
    evaluations = {
        'equation': equation,
        'derivative': first_derivative,
        'integral': integral
    }
    points = {
        'roots': final_roots,
        'maxima': final_maxima,
        'minima': final_minima,
        'inflections': final_inflections
    }
    accumulations = {
        'range': accumulated_range,
        'iqr': accumulated_iqr
    }
    averages = {
        'range': averages_range,
        'iqr': averages_iqr
    }
    result = {
        'constants': coefficients,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result