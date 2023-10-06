from typing import List, TypeAlias, Union


NestedList: TypeAlias = List[Union[int, List]]


class NestedIterator:
    """
    an iterator to flatten a list of nested integers.

    usage:
    nested_list = [[1, 2], [3], 4]
    iterator = NestedIterator(nested_list)
    while iterator.hasNext():
        value = iterator.next()
        print(value)  # prints the flattened values.

    args:
    : nestedList(List[Union[int, List]]): a list containing integers and / or
        nested lists.

    Returns:
    None
    """

    def __init__(self, nestedList: NestedList):
        """
        initializes an instance of NestedIterator.

        args:
        nestedList(NestedList): a list containing integers and / or
            nested lists.
        """
        self.flat: list[int] = self.flatten(nestedList)
        self.index: int = 0

    def __repr__(self) -> str:
        """
        returns a string representation of the NestedIterator.

        Returns:
        str: a string representation of the iterator.
        """
        return f"NestedIterator({self.flat})"

    def __iter__(self):
        """
        returns the iterator object itself.

        Returns:
        NestedIterator: the iterator object.
        """
        return self

    def __next__(self) -> Union[int, None]:
        """
        gets the next integer from the flattened list.

        Returns:
        Union[int, None]: the next integer, or None if there are no more
            integers.
        """
        if self.hasNext():
            self.index += 1
            return self.flat[self.index - 1]
        raise StopIteration

    def flatten(self, nestedList: NestedList) -> list[int]:
        """
        recursively flattens a list of nested integers.

        args:
        nestedList(NestedList): a list containing integers and / or
            nested lists.

        Returns:
        list[int]: the flattened list of integers.
        """
        flat: list[int] = []
        for item in nestedList:
            if isinstance(item, list):
                flat.extend(self.flatten(item))
            else:
                flat.append(item)
        return flat

    def next(self) -> Union[int, None]:
        """
        convenience method, calls the __next__ method
        """
        return self.__next__()

    def hasNext(self) -> bool:
        """
        checks if there are more integers to iterate through.

        Returns:
        bool: True if there are more integers, False otherwise.
        """
        size = len(self.flat)
        return self.index < size
