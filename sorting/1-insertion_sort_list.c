#include <stdio.h>
#include <stdlib.h>
 
void print_array(const int *array, size_t size);
void insertion_sort(int array[], size_t n);
 
/**
 * print_array - Prints an array of integers
 *
 * @array: The array to be printed
 * @size: Number of elements in @array
 */
void print_array(const int *array, size_t size)
{
    size_t i;
 
    i = 0;
    while (array && i < size)
    {
        if (i > 0)
            printf(", ");
        printf("%d", array[i]);
        ++i;
    }
    printf("\n");
}
 
 
void insertion_sort(int array[], size_t n)
{
        size_t i, j;
        int temp;
 
        // 8, 13, 19, 52, 71, 73, 86, 96, 99, 7
 
        for (i = 1; i < n; i++)
        {
                temp = array[i]; //i = 9 temp = 7
 
                j = i - 1; //8
 
                while(j >= 0 && array[j] > temp)
                {
                        array[j+1] = array[j];
                        //array[9] = 99
                        //array[8] = 96
                        //array[7] = 86
                        //array[6] = 73
                        //array[5] = 71
                        //array[4] = 52
                        //array[3] = 19
                        //array[2] = 13
                        //array[1] = 8
                        //array[
                        j--;
                }
                array[j + 1] = temp;
                //array[0] = temp
                print_array(array, n);
        }
}
int main(void)
{
        int array[] = {19, 8, 99, 71, 13, 52, 96, 73, 86, 7};
        size_t n = sizeof(array) / sizeof(array[0]);
 
        insertion_sort(array, n);
 
        return (0);
}
