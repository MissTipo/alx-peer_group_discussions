#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>



size_t binary_tree_height(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (0);
    else
    {
        size_t l_Height = 0, r_Height = 0;
        l_Height = tree->left ? 1 + binary_tree_height(tree->left) : 0;
        r_Height = tree->right ? 1 + binary_tree_height(tree->right) : 0;
        if (l_Height >= r_Height)
            return (l_Height);
        else
            return (r_Height);
    }
}

/**
size_t binary_tree_height(const binary_tree_t *tree)
{
	if (tree)
	{
		size_t l = 0, r = 0;

		//l = tree->left ? 1 + binary_tree_height(tree->left) : 0;

        if (tree->left)
        {
            l = 1 + binary_tree_height(tree->left);
        }
        else
            l = 0;





		r = tree->right ? 1 + binary_tree_height(tree->right) : 0;
		return ((l > r) ? l : r);
	}
	return (0);
}

*/








