from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def linear(data):
    independent_matrix = [
        [data[0][0], 1],
        [data[1][0], 1]
    ]
    dependent_matrix = [
        [data[0][1]],
        [data[1][1]]
    ]
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    result = multiplication_vector(second_product, dependent_matrix)
    return result