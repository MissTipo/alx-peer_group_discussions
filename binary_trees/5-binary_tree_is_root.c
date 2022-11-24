#include "binary_trees.h"


int binary_tree_is_root(const binary_tree_t *node)
{
    // Return if tree is NULL
    if (node == NULL)
        return (0);
    // Check if Node->parent points to NULL
    if (node->parent == NULL)
        return (1);
    else
        return (0);
}
