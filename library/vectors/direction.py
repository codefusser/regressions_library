from math import atan, degrees
from library.errors.vectors import vector_of_scalars, length

def vector_direction(vector):
    """
    Calculates the direction of a vector in radians and degrees

    Parameters
    ----------
    vector : list
        List of two numbers representing a vector, in which the first number is the horizontal component and the second is the vertical component

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list
    TypeError
        Elements of argument must be integers or floats
    ValueError
        Argument must contain exactly two elements

    Returns
    -------
    direction['radian'] : float
        Measure of the angle of the vector in radians
    direction['degree'] : float
        Measure of the angle of the vector in degrees

    See Also
    --------
    :func:`~library.vectors.components.component_form`, :func:`~library.vectors.magnitude.vector_magnitude`, :func:`~library.vectors.unit.unit_vector`

    Notes
    -----
    - Vector: :math:`\\langle x, y \\rangle`
    - Direction of vector: :math:`\\theta = \\tan^{-1}(\\frac{y}{x})`
    - |direction|

    Examples
    --------
    Determine the direction of a vector with a component form of [7, 5]
        >>> direction1 = vector_direction([7, 5])
        >>> print(direction1['radian'])
        0.6202494859828215
        >>> print(direction1['degree'])
        35.53767779197438
    Determine the direction of a vector with a component form of [-3, 11]
        >>> direction2 = vector_direction([-3, 11])
        >>> print(direction2['radian'])
        -1.3045442776439713
        >>> print(direction2['degree'])
        -74.74488129694222
    """
    vector_of_scalars(vector)
    length(vector, 2)
    if vector[0] == 0:
        vector[0] = 0.0001
    ratio = vector[1] / vector[0]
    radian_measure = atan(ratio)
    degree_measure = degrees(radian_measure)
    result = {
        'radian': radian_measure,
        'degree': degree_measure
    }
    return result