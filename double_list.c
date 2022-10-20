#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int data;
	struct node *prev;
	struct node *next;
} node;
//creating a node
node *create_node(int data)
{
	node *new = malloc(sizeof(node));
	new->data = data;
	new->prev = NULL;
	new->next = NULL;

	return new;

}

//print_list

void print_list(node *head)
{
	while (head)
	{
		printf( "%d\n", head->data);
		head = head->next;
	}
}

int main()
{
	
