#include "binary_trees.h"

//A full Binary tree is a special type of binary tree in which 
//every parent node/internal node has either two or no children

int binary_tree_is_full(const binary_tree_t *tree)
{
	//if (!tree)
	//	return (0);
	// chech if it has 2 or 0 children
	//  if yes, recursive traverse the children
	//
	if (tree)
	{
		if ((!tree->left) && (!tree->right))
			return (1);
		if ((tree->left) && (tree->right))
		{
			return (binary_tree_is_full(tree->left) && binary_tree_is_full(tree->right));
		}
		else
			return (0);
	}
	return (0);
}		
