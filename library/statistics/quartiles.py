from library.errors.vectors import vector_of_scalars
from library.errors.scalars import select_integers
from .median import median_value
from .halve import half

def quartile_value(data, q):
    """
    Determines the first, second, or third quartile values of a data set

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze
    q : int
        Number determining which quartile to provide

    Raises
    ------
    TypeError
        First argument must be a 1-dimensional list or tuple
    TypeError
        Elements of first argument must be integers or floats
    ValueError
        Second argument must be an integer contained within the set [1, 2, 3]

    Returns
    -------
    quartile : int or float
        Quartile value of the data set

    See Also
    --------
    :func:`~library.statistics.sort.sorted_list`, :func:`~library.statistics.halve.half`, :func:`~library.statistics.minimum.minimum_value`, :func:`~library.statistics.maximum.maximum_value`, :func:`~library.statistics.median.median_value`

    Notes
    -----
    - Ordered set of numbers: :math:`a_i = ( a_1, a_2, \\cdots, a_n )`
    - For sets with an odd amount of numbers:
        
        - First quartile: :math:`Q_1 = a_{\\lceil n/4 \\rceil}`
        - Second quartile: :math:`Q_2 = a_{\\lceil n/2 \\rceil}`
        - Third quartile: :math:`Q_3 = a_{\\lceil 3n/4 \\rceil}`
    
    - For sets with an even amount of numbers:

        - If :math:`n \\text{ mod } 4 \\neq 0`:

            - First quartile: :math:`Q_1 = a_{\\lceil n/4 \\rceil}`
            - Second quartile: :math:`Q_2 = \\frac{a_{n/2} + a_{n/2 + 1}}{2}`
            - Third quartile: :math:`Q_3 = a_{\\lceil 3n/4 \\rceil}`
        
        - If :math:`n \\text{ mod } 4 = 0`:

            - First quartile: :math:`Q_1 = \\frac{a_{n/4} + a_{n/4 + 1}}{2}`
            - Second quartile: :math:`Q_2 = \\frac{a_{n/2} + a_{n/2 + 1}}{2}`
            - Third quartile: :math:`Q_3 = \\frac{a_{3n/4} + a_{3n/4 + 1}}{2}`

    - |quartiles|

    Examples
    --------
    Determine the first quartile of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> quartile1 = quartile_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1], 1)
        >>> print(quartile1)
        9
    Determine the third quartile of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> quartile3 = quartile_value([12, 81, 13, 8, 42, 72, 91, 20, 20], 3)
        >>> print(quartile3)
        76.5
    """
    vector_of_scalars(data, 'first')
    select_integers(q, [1, 2, 3])
    halved_data = half(data)
    result = ''
    if q == 2:
        result = median_value(data)
    elif q == 1:
        result = median_value(halved_data['lower'])
    elif q == 3:
        result = median_value(halved_data['upper'])
    return result