#include "search_algos.h"

int exponential_search(int *array, size_t size, int value)
{
	size_t exp, low, high, i, mid;

	/**
	 * int array[] = {0, 1, 2, 3, 4, 7, 12, 15, 18, 19, 23, 54, 61, 62, 76, 99};
	 *
	 * check
	 * while array[exp] < value; then multiply exp by 2
	 *
	 * value = 7
	 * 1- array[1] = 1  bound-> 0, 1
	 * 2- array[2] = 2  bound-> 1, 2
	 * 3- array[4] = 4  bound-> 2, 3, 4
	 * 4- array[8] = 18->  18 !< value    bound->4, 7, 12, 15, 18
	 */
	if (!array)
		return (-1);
	exp = 1;
	while ((array[exp] <= value) && (exp < size))
	{
		printf("Value checked array[%ld] = [%d]\n", exp, array[exp]);
		exp *= 2;
	}
	if (array[exp] == value)
		return exp;
	
	low = exp / 2;
	high = exp - 1;
	printf("Value found between indexes [%ld] and [%ld]\n", low, high);
	
	mid = (low + high) / 2;
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
