from nested_iterator import NestedIterator, NestedList


if __name__ == "__main__":
    # Test case 1: Nested list with integers and sublists
    nested_list1: NestedList = [[1, 2], [3], 4]
    iterator1 = NestedIterator(nested_list1)
    print("Test Case 1:")
    while iterator1.hasNext():
        value = iterator1.next()
        print(value)  # Prints the flattened values.

    # Test case 2: Nested list with empty sublists
    nested_list2: NestedList = [[], [], []]
    iterator2 = NestedIterator(nested_list2)
    print("\nTest Case 2:")
    while iterator2.hasNext():
        value = iterator2.next()
        print(value)  # Prints an empty list.

    # Test case 3: Nested list with no integers
    nested_list3: NestedList = []
    iterator3 = NestedIterator(nested_list3)
    print("\nTest Case 3:")
    while iterator3.hasNext():
        value = iterator3.next()
        print(value)  # Should not print anything.
