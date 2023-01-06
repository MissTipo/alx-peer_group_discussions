#include "search_algos.h"

int jump_search(int *array, size_t size, int value)
{
	/**
	 * int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	 * jump_step = 3
	 * jump-1 -> 0, 1, 2
	 * jump-2 -> 3, 4, 5
	 * jump-3 -> 6, 7, 8
	 * jump-4 -> 9.
	 * get the jump_step
	 * jump untill the array[current] > value
	 * linearly search the current batch
	 */

	size_t  current, temp, i, jump_step;

	jump_step = sqrt(size);
	current = 0;
	while (array[current] < value)
	{
		current += jump_step;
	}
} 
