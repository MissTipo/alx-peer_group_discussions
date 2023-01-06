#include "search_algos.h"


int binary_search(int *array, size_t size, int value)
{
	/**int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	 * while low <= high
	 * mid = low + high / 2
	 * compare mid with value
	 * if it is equal, return index
	 * if greater than value, compare with the first half, else
	 * compare with the later half
	 */

	size_t mid, low, high, i;
	if (!array)
		return (-1);

	low = 0;
	high = size - 1;

	while (low <= high)
	{
		printf("Searching in array: ");


		for (i = low; i < high; i++)
		{
			printf("%d, ", array[i]);
		}
		printf("%d\n", array[high]);

		
		mid = (high + low) / 2;
		if (array[mid] == value)
			return (mid);
		if (array[mid] < value)
			low = mid + 1;
		if (array[mid] > value)
			high = mid - 1;
	}
	return (-1);
}


