#include "binary_trees.h"

binary_tree_t *binary_trees_ancestor(const binary_tree_t *first, const binary_tree_t *second)
{
//22-> [22, 32, 21, 47, 79]

//68-> [68, 47, 79]

	//move from node to root and store the parent pointer in an array *2
	
	const binary_tree_t *temp;

	while (first)
	{
		temp = second;
		while (second)
		{
			if (first == second)
				return (first);
			if (second->parent)
				second = second->parent;
			else
				break;
		}

		second = temp;
		if (first->parent)
			first = first->parent;
		else
			break;
	}
	return (NULL);
}


/**
	if (!first || !second)
		return NULL;


	//compare the array and return the first common element

	binary_tree_t *first_array[30], *second_array[30];
	int i = 0, j = 0;

	while (first)
	{
		first_array[i] = first;
		i++;

		if (first->parent)
		{
			first = first->parent;
		}
		else
			break;
	}

	while (second)
	{
		second_array[j] = second;
		j++;

		if (second->parent)
		{
			second = second->parent;
		}
		else
			break;
	}

	// compare content of both array
	int k = 0, l = 0;

	for (k = 0; k < i; k++)
	{
		for (l = 0; l < j; l++)
		{
			if (first_array[k] == second_array[l])
			{
				return first_array[k];
			}
		}
		return (NULL);
	}
	return NULL;
}

*/















