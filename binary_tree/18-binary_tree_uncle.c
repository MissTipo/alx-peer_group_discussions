#include "binary_trees.h"

// Find the sibling of a node

/**
binary_tree_t *binary_tree_uncle(binary_tree_t *node)
{
	if (node && (node->parent->parent != NULL))
	{
		binary_tree_t *father, *fore_father;

		father = node->parent;
		fore_father = father->parent;
		if (fore_father->left && fore_father->right)
		{
			if (fore_father->left == father)
				return (fore_father->right);
			else
				return (fore_father->left);
		}
		else
			return (NULL);
	}
	return NULL;
}
*/



binary_tree_t *binary_tree_sibling(binary_tree_t *node)
{

        if (node == NULL || node->parent == NULL)
                return (NULL);
        if (node->parent->left == node)
                return (node->parent->right);
        return (node->parent->left);
}

binary_tree_t *binary_tree_uncle(binary_tree_t *node)
{
	if (node && node->parent && node->parent->parent)
		return binary_tree_sibling(node->parent);
	else
		return (NULL);
}



































