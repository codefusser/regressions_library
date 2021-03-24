import unittest

from library.statistics.rounding import rounding
from library.statistics.summation import summation
from library.statistics.sort import sort, sort_dimension
from library.statistics.halve import halve, halve_dimension
from library.statistics.minimum import minimum
from library.statistics.maximum import maximum
from library.statistics.quartiles import quartiles
from library.statistics.median import median
from library.statistics.mean import mean
from library.statistics.five_number_summary import five_number_summary
from library.statistics.ranges import ranges
from library.statistics.deviations import deviations
from library.statistics.residuals import residuals
from library.statistics.correlation import correlation

even_set = [8, 2, 5, 9, 1, 3, 22, 11, 9, 13]
odd_set = [7, 4, 6, 8, 2, 5, 25, 14, 8]
compare_set = [5, 5, 5, 10, 1, 7, 22, 13, 8]
dimension_set = [[2, 7], [1, 9], [5, 2], [3, 4], [4, 3], [8, 1], [2, 3], [7, 7], [1, 1], [5, 3]]

normal_decimal = 6.817239833721
extreme_decimal = 0.000000000000000000005782016894

precision = 4
high_precision = 8

class TestRounding(unittest.TestCase):
    def test_round_normal(self):
        round_normal = rounding(normal_decimal, precision)
        self.assertEqual(round_normal, 6.8172)

    def test_round_normal_high(self):
        round_normal_high = rounding(normal_decimal, high_precision)
        self.assertEqual(round_normal_high, 6.81723983)
    
    def test_round_extreme(self):
        round_extreme = rounding(extreme_decimal, precision)
        self.assertEqual(round_extreme, 0.0001)
    
    def test_round_extreme_high(self):
        round_extreme_high = rounding(extreme_decimal, high_precision) 
        self.assertEqual(round_extreme_high, 1e-08)

class TestSummation(unittest.TestCase):
    def test_sum_even(self):
        sum_even = summation(even_set)
        self.assertEqual(sum_even, 83)

    def test_sum_odd(self):
        sum_odd = summation(odd_set)
        self.assertEqual(sum_odd, 79)

class TestSort(unittest.TestCase):
    def test_sort_even(self):
        sort_even = sort(even_set)
        self.assertEqual(sort_even, [1, 2, 3, 5, 8, 9, 9, 11, 13, 22])

    def test_sort_odd(self):
        sort_odd = sort(odd_set)
        self.assertEqual(sort_odd, [2, 4, 5, 6, 7, 8, 8, 14, 25])
    
    def test_sort_dimension(self):
        dimension_sort = sort_dimension(dimension_set, 1)
        self.assertEqual(dimension_sort, [[1, 9], [1, 1], [2, 7], [2, 3], [3, 4], [4, 3], [5, 2], [5, 3], [7, 7], [8, 1]])

class TestHalve(unittest.TestCase):
    def test_halve_even(self):
        halve_even = halve(even_set)
        self.assertEqual(halve_even, {'upper': [9, 9, 11, 13, 22], 'lower': [1, 2, 3, 5, 8]})

    def test_halve_odd(self):
        halve_odd = halve(odd_set)
        self.assertEqual(halve_odd, {'upper': [8, 8, 14, 25], 'lower': [2, 4, 5, 6]})
    
    def test_halve_dimension(self):
        dimension_halve = halve_dimension(dimension_set, 1)
        self.assertEqual(dimension_halve, {'upper': [[4, 3], [5, 2], [5, 3], [7, 7], [8, 1]], 'lower': [[1, 9], [1, 1], [2, 7], [2, 3], [3, 4]]})

class TestMinimum(unittest.TestCase):
    def test_min_even(self):
        min_even = minimum(even_set)
        self.assertEqual(min_even, 1)

    def test_min_odd(self):
        min_odd = minimum(odd_set)
        self.assertEqual(min_odd, 2)

class TestMaximum(unittest.TestCase):
    def test_max_even(self):
        max_even = maximum(even_set)
        self.assertEqual(max_even, 22)

    def test_max_odd(self):
        max_odd = maximum(odd_set)
        self.assertEqual(max_odd, 25)

class TestQuartiles(unittest.TestCase):
    def test_q1_even(self):
        q1_even = quartiles(even_set, 1)
        self.assertEqual(q1_even, 3)
    
    def test_q1_odd(self):
        q1_odd = quartiles(odd_set, 1)
        self.assertEqual(q1_odd, 4.5)
    
    def test_q3_even(self):
        q3_even = quartiles(even_set, 3)
        self.assertEqual(q3_even, 11)
    
    def test_q3_odd(self):
        q3_odd = quartiles(odd_set, 3)
        self.assertEqual(q3_odd, 11)

class TestMedian(unittest.TestCase):
    def test_median_even(self):
        median_even = median(even_set)
        self.assertEqual(median_even, 8.5)
    
    def test_median_odd(self):
        median_odd = median(odd_set)
        self.assertEqual(median_odd, 7)

class TestMean(unittest.TestCase):
    def test_mean_even(self):
        mean_even = mean(even_set)
        self.assertEqual(mean_even, 8.3)
    
    def test_mean_odd(self):
        mean_odd = mean(odd_set)
        self.assertAlmostEqual(mean_odd, 8.7778, 4)

class TestFiveNumberSummary(unittest.TestCase):
    def test_five_even(self):
        five_even = five_number_summary(even_set, precision)
        self.assertEqual(five_even, {'minimum': 1, 'q1': 3, 'median': 8.5, 'q3': 11, 'maximum': 22})
    
    def test_five_odd(self):
        five_odd = five_number_summary(odd_set, precision)
        self.assertEqual(five_odd, {'minimum': 2, 'q1': 4.5, 'median': 7, 'q3': 11.0, 'maximum': 25})

class TestRange(unittest.TestCase):
    def test_range_even(self):
        range_even = ranges(even_set)
        self.assertEqual(range_even, 21)
    
    def test_range_odd(self):
        range_odd = ranges(odd_set)
        self.assertEqual(range_odd, 23)

class TestDeviations(unittest.TestCase):
    def test_deviations_even(self):
        deviations_even = deviations(even_set)
        self.assertAlmostEqual(deviations_even[0], -0.3)
    
    def test_deviations_odd(self):
        deviations_odd = deviations(odd_set)
        self.assertAlmostEqual(deviations_odd[0], -1.7778, 4)

class TestComparisons(unittest.TestCase):
    def test_residuals_compare(self):
        residuals_compare = residuals(odd_set, compare_set)
        self.assertEqual(residuals_compare, [2, -1, 1, -2, 1, -2, 3, 1, 0])
    
    def test_correlation_compare(self):
        correlation_compare = correlation(odd_set, compare_set, precision)
        self.assertEqual(correlation_compare, 0.967)

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 32 tests in 0.004s ---------- OK ---------- #