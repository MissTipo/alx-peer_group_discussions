#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>



size_t binary_tree_depth(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (0);
    else
    {
        size_t l_Depth = 0;

	 if (tree->parent)
        {
                l_Depth = 1 + binary_tree_depth(tree->parent);
        }
        else
                l_Depth = 0;
        return (l_Depth);
        }

        //l_Depth = tree->parent ? 1 + binary_tree_depth(tree->parent) : 0;
        /**r_Depth = tree->right ? binary_tree_depth(tree->right) - 1 : 0;
        if (l_Depth >= r_Depth)
            return (l_Depth);
        else
            return (r_Depth);*/
        //return (l_Depth);
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








