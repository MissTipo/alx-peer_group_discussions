#include "binary_trees.h"


size_t binary_tree_nodes(const binary_tree_t *tree)
{
	size_t nodes = 0;
	
	if (tree)
	{



		nodes += (tree->left || tree->right) ? 1: 0;
		nodes += binary_tree_nodes(tree->left);
		nodes += binary_tree_nodes(tree->right);
	}
	return (nodes);


	/*size_t l_no_node = 0, r_no_node = 0, total_no_node = 0;

        if (!tree)
                return (0);
        if ((tree->left || tree->right) && tree->parent)
                return (1);
        if (tree->left || tree->right)
        {
                l_no_node = binary_tree_nodes(tree->left) + 1;
                r_no_node = binary_tree_nodes(tree->right);
                total_no_node = l_no_node + r_no_node;
                return (total_no_node);
        }
        return (total_no_node);*/

		
		/*if ((tree->left) || (tree->right))
			return (1);
		l_node = binary_tree_nodes(tree->left);
		r_node = binary_tree_nodes(tree->right);
		return (l_node + r_node); */

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








