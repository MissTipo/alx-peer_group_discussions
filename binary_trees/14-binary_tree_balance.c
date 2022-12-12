#include "binary_trees.h"

//the difference between the height of the left subtree and 
//that of the right subtree of that node.


//size_t binary_tree_height(const binary_tree_t *tree);

int binary_tree_balance(const binary_tree_t *tree)
{
	if (tree)
	{
		int l_height = 0, r_height = 0;

		if (tree->right)
			r_height = 1 + binary_tree_height(tree->right);
		if (tree->left)
			l_height = 1 + binary_tree_height(tree->left);
		return (l_height - r_height);
	}
	return (0);
}
