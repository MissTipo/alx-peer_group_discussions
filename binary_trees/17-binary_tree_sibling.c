#include "binary_trees.h"

// Find the sibling of a node

/**binary_tree_t *binary_tree_sibling(binary_tree_t *node)
{
	if (node && (node->parent != NULL))
	{
		binary_tree_t *father;

		father = node->parent;
		if (father->left && father->right)
		{
			if (father->left == node)
				return (father->right);
			else
				return (father->left);
		}
		else
			return (NULL);
	}
	return NULL;
}*/

binary_tree_t *binary_tree_sibling(binary_tree_t *node)
{

        if (node == NULL || node->parent == NULL)
                return (NULL);
        if (node->parent->left == node)
                return (node->parent->right);
        return (node->parent->left);
}
