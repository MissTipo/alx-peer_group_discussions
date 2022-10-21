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

node *init_list(node *head, node *new_node)
{
	node *temp;
	/*for creating 1st node only*/
	if (head == NULL)
		head = new_node;
	else
	{
		/*for creating other nodes*/
		temp = head;
		/*for getting to end of list*/
		while (temp->next)
			temp = temp->next;
		new_node->prev = temp;
		temp->next = new_node;
	}
	return head;
}

int main()
{
	node *head = NULL;
	node *node_1, *node_2, *node_3;
	node_1 = create_node(100);

	head = init_list(head, node_1);
	/*print_list(head);*/

	node_2 = create_node(200);
	init_list(head, node_2);
	/*print_list(head);*/

	node_3 = create_node(300);
	init_list(head, node_3);
	print_list(head);
	return (0);
}

