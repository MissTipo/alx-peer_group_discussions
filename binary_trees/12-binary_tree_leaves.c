#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>



size_t binary_tree_leaves(const binary_tree_t *tree)
{
	if (tree == NULL)
                return (0);
        size_t l_leaf = 0, r_leaf = 0;

        if ((tree->left == NULL) && (tree->right == NULL))
                return (1);
        l_leaf = binary_tree_leaves(tree->left);
        r_leaf = binary_tree_leaves(tree->right);
        return (l_leaf + r_leaf);
}
/**
size_t binary_tree_leaves(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (0);
    else
    {
        size_t l_leaf = 0, r_leaf = 0;

        if ((tree->left == NULL) && (tree->right == NULL))
            return (1);

        l_leaf = binary_tree_leaves(tree->left);
        r_leaf = binary_tree_leaves(tree->right);

        //return(binary_tree_leaves(tree->left) + binary_tree_leaves(tree->right));

        //l_leaf = tree->left ? binary_tree_leaves(tree->left) : 0;
        //r_leaf = tree->right ? binary_tree_leaves(tree->right) : 0;
        //return (l_leaf + r_leaf);
    }
}


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








