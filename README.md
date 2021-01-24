# Regressions Library

A collection of algorithms for fitting data to different functional models by using matrices. This [library](https://github.com/jtreeves/regressions_library) will be made publically available after it is uploaded to Python's database of libraries. It contains all the code for determining regression equations, as well as the code for evaluating said regressions and presenting their results in a raw format. The published version on PyPI is available [here](https://pypi.org/project/regressions/).

**Contents**

1. [File Structure](https://github.com/jtreeves/matrix_regression#file-structure)
2. [Code Examples](https://github.com/jtreeves/matrix_regression#code-examples)

## File Structure

```
regressions_library  
|-- matrices  
|   |-- matrix.py  
|   |-- magnitude.py  
|   |-- dot_product.py  
|   |-- column.py  
|   |-- additions.py  
|   |-- scalar.py  
|   |-- multiplication.py  
|   |-- determinant.py  
|   |-- cofactors.py  
|   |-- minors.py  
|   |-- inverse.py  
|   |-- transpose.py  
|-- regressions  
|   |-- run_all.py  
|   |-- best.py  
|   |-- error.py  
|   |-- linear.py  
|   |-- quadratic.py  
|   |-- cubic.py  
|   |-- hyperbolic.py  
|   |-- exponential.py  
|   |-- logarithmic.py  
|   |-- logistic.py  
|   |-- sinusoidal.py  
|-- tests  
|   |-- matrices.py  
|   |-- regressions.py  
|-- READE.md  
|-- .gitignore  
```

## Code Examples

**Linear Regression**
```python
def linear(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([data[i][0], 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    equation = lambda x: solution[0][0]*x + solution[1][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': solution,
        'error': inaccuracy
    }
    return result
```

**Error Calculation**
```python
def error(data, equation):
    summation = 0
    for i in range(len(data)):
        summation += (data[i][1] - equation(data[i][0]))**2
    result = summation**(1/4)
    return result
```