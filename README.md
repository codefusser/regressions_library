# Regressions Library

A collection of algorithms for fitting data to different functional models by using matrices. This [library](https://github.com/jtreeves/regressions_library) will be made publically available after it is uploaded to Python's database of libraries. It contains all the code for determining regression equations, as well as the code for evaluating said regressions and presenting their results in a raw format. The published version on PyPI is available [here](https://pypi.org/project/regressions/).

**Contents**
1. [Requirements](https://github.com/jtreeves/regressions_library#requirements)
2. [Installation](https://github.com/jtreeves/regressions_library#installation)
3. [Features](https://github.com/jtreeves/regressions_library#features)
4. [Code Examples](https://github.com/jtreeves/regressions_library#code-examples)
5. [Future Goals](https://github.com/jtreeves/regressions_library#future-goals)

## Requirements

- Python 3.8 or higher
- NumPy
- SciPy

## Installation

**Download Library**
```
pip3 install regressions
```

**Create Local Repository**
```
git clone https://github.com/jtreeves/regressions_library.git
```

## Features

## Code Examples

**Linear Regression Model**
```python
def linear_model(data, precision = 4):
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    independent_matrix = []
    dependent_matrix = column_conversion(dependent_variable)
    for element in independent_variable:
        independent_matrix.append([element, 1])
    solution = system_solution(independent_matrix, dependent_matrix, precision)
    coefficients = no_zeroes(solution, precision)
    equation = linear_equation(*coefficients, precision)
    derivative = linear_derivatives(*coefficients, precision)['first']['evaluation']
    integral = linear_integral(*coefficients, precision)['evaluation']
    points = key_coordinates('linear', coefficients, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area('linear', coefficients, min_value, max_value, precision)
    accumulated_iqr = accumulated_area('linear', coefficients, q1, q3, precision)
    averages_range = average_values('linear', coefficients, min_value, max_value, precision)
    averages_iqr = average_values('linear', coefficients, q1, q3, precision)
    predicted = []
    for element in independent_variable:
        predicted.append(equation(element))
    accuracy = correlation_coefficient(dependent_variable, predicted, precision)
    evaluations = {
        'equation': equation,
        'derivative': derivative,
        'integral': integral
    }
    points = {
        'roots': points['roots'],
        'maxima': points['maxima'],
        'minima': points['minima'],
        'inflections': points['inflections']
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
```

**Correlation Coefficient**
```python
def correlation_coefficient(actuals, expecteds, precision = 4):
    residuals = multiple_residuals(actuals, expecteds)
    deviations = multiple_deviations(actuals)
    squared_residuals = []
    for residual in residuals:
        squared_residuals.append(residual**2)
    squared_deviations = []
    for deviation in deviations:
        squared_deviations.append(deviation**2)
    residual_sum = sum_value(squared_residuals)
    deviation_sum = sum_value(squared_deviations)
    if deviation_sum == 0:
        deviation_sum = 10**(-precision)
    ratio = residual_sum / deviation_sum
    if ratio > 1:
        return 0.0
    else:
        result = (1 - ratio)**(1/2)
        return rounded_value(result, precision)
```

## Future Goals