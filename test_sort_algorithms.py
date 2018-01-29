import unittest
import random
from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from counting_sort import CountingSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from odd_even_sort import OddEvenSort


class SortAlgorithmsTest(unittest.TestCase):
    def setUp(self):
        self.checkList = list(range(0, 100))
        self.targetList = random.sample(list(range(0, 100)), k=100)

    def test_bubble_sort(self):
        sortedList = BubbleSort.bubble_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)

    def test_short_bubble_sort(self):
        sortedList = BubbleSort.short_bubble_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)

    def test_selection_sort(self):
        sortedList = SelectionSort.selection_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)

    def test_counting_sort(self):
        sortedList = CountingSort.counting_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)

    def test_merge_sort(self):
        sortedList = MergeSort.merge_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)

    def test_quick_sort(self):
        sortedList = QuickSort.quick_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)

    def test_odd_even_sort(self):
        sortedList = OddEvenSort.odd_even_sort(self.targetList)
        self.assertTrue(sortedList == self.checkList)


if __name__ == "__main__":
    unittest.main()
