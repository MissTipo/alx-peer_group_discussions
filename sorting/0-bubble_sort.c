#include "sort.h"

/**
 * Loop through the array
 * swap adjacent element if array at index [j] is greater then array at index [j + 1]
 */


void bubble_sort(int *array, size_t size)
{
  size_t temp, i, j;
  // Array [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]

  for (i = 0; i < size - 1; i++)
  {
    for (j = 0; j < size - i - 1; j++)
    {
	   // if (array[i] > array[j])
      if (array[j] > array[j + 1])
      {
        temp = array[j];  // temp == 19
        array[j] = array[j + 1]; // array[j] = 48
        array[j + 1] = temp;  // array[j + 1] = 19
        print_array(array, size);
      }
//      else
  //      continue;
    }
  }
}
