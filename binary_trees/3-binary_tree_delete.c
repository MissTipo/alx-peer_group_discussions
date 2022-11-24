#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>

void binary_tree_delete(binary_tree_t *tree)
{
    if (tree == NULL)
        return;

    // Traversing to delete to the left
    binary_tree_delete(tree->left);

    /* Delete right sub-tree */
    binary_tree_delete(tree->right);

    /* At last, delete root node */
    printf("Deleteing Node : %d\n", tree->n);
    free(tree);

}
