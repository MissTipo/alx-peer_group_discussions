from nested_iterator import NestedIterator, NestedList
import unittest


class TestNestedIterator(unittest.TestCase):
    def test_iterator_with_nested_list(self):
        # Test case 1: Nested list with integers and sublists
        nested_list1: NestedList = [[1, 2], [3], 4]
        iterator1: NestedIterator = NestedIterator(nested_list1)
        flattened_values = list(iterator1)

        self.assertEqual(flattened_values, [1, 2, 3, 4])

    def test_iterator_with_empty_sublists(self):
        # Test case 2: Nested list with empty sublists
        nested_list2: NestedList = [[], [], []]
        iterator2: NestedIterator = NestedIterator(nested_list2)
        flattened_values = list(iterator2)

        self.assertEqual(flattened_values, [])

    def test_iterator_with_no_integers(self):
        # Test case 3: Nested list with no integers
        nested_list3: NestedList = []
        iterator3: NestedIterator = NestedIterator(nested_list3)
        flattened_values = list(iterator3)

        self.assertEqual(flattened_values, [])

    def test_has_next(self):
        # Test case 4: Test hasNext() method
        nested_list4: NestedList = [[1], [2], [3]]
        iterator4: NestedIterator = NestedIterator(nested_list4)

        self.assertTrue(iterator4.hasNext())
        iterator4.next()
        self.assertTrue(iterator4.hasNext())
        iterator4.next()
        self.assertTrue(iterator4.hasNext())
        iterator4.next()
        self.assertFalse(iterator4.hasNext())


if __name__ == "__main__":
    unittest.main(verbosity=2)
