#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>



size_t binary_tree_size(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (0);
    else
    {
        size_t l_size = 0, r_size = 0;
        l_size = tree->left ? binary_tree_size(tree->left) : 0;
        r_size = tree->right ? binary_tree_size(tree->right) : 0;
        
        return (l_size + r_size + 1);
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








