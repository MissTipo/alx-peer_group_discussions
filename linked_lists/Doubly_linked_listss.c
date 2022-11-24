#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int data;
	struct node *prev;
	struct node *next;
} node;


//print_list

void print_list(node *head)
{
    int count = 1;
	while (head)
	{
		printf( "%d: %d\n", count, head->data);
		head = head->next;
        count++;
	}
}


node *init_list(node *head, int data)
{
    node *temp;
	node *new_node = malloc(sizeof(node));
	new_node->data = data;
	//for creating 1st node only
	if (head == NULL)
		head = new_node;
	else
	{
		//for creating other nodes
		temp = head;
        //for getting to end of list
		while (temp->next)
			temp = temp->next;
		new_node->prev = temp;
		new_node->next = NULL;
        temp->next = new_node;
	}
    return head;
}


int main()
{
    node *head = NULL;
    

    head = init_list(head, 100);
    
    
    head = init_list(head, 200);
    
    head = init_list(head, 300);
    print_list(head);
    return (0);
}
