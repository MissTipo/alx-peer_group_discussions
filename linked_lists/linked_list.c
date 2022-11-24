#include <stdio.h>
#include <stdlib.h>
<<<<<<< HEAD
/*Olamide's file */
/*Struct for singly list*/
=======

/*Struct node for singly list*/
>>>>>>> master
typedef struct node
{
    int data;
    struct node *next;

} node;

/*Prototypes*/
node *create_node(int data);
void print_list(node *head);
void append_to_list(node *head, node *new_node);
node *push(node *head, node *new_node);
void insert_after_n(node *head, node *new_node, int n);
void swap_after_n(node *head, int n);
void delAtpos(node *head, int pos);
int countList(node *head);

/*creates a new node*/
node *create_node(int data)
{
    node *new_node = malloc(sizeof(node));

    new_node->data = data;
    new_node->next = NULL;
    return (new_node);
}

/*Print list function*/
void print_list(node *head)
{
    while (head != NULL)
    {
            printf("%d\n", head->data);
            head = head->next;
    }
}

/*append to end of list*/
void append_to_list(node *head, node *new_node)
{
    if (head == NULL)
    {
        head = new_node;
    }

    else{
            while (head->next)
            {
                head = head->next;
            }
            head->next = new_node;
        }
}

node *push(node *head, node *new_node)
{
    if (head == NULL)
    {
        head = new_node;
    }
    new_node->next = head;
    head = new_node;
    return (head);
}

void insert_after_n(node *head, node *new_node, int n)
{
    int count = 1;

    while (head->next)
    {
        if (count == n)
        {
            new_node->next = head->next;
            head->next = new_node;
        }
        head = head->next;
        count++;
    }
}

/*Swap after nth position*/
void swap_after_n(node *head, int n)
{
    int count = 1;
    node *temp, *swap, *prev;

    //traverse the list
    while (head->next)
    {
        //help locate node @ n-1 == previous node
        
        if (n != 1 && count == (n - 1))
            prev = head;
        // help locate node @ nth position
        if (count == n)
        {
            temp = head; 
            swap = head->next;
            
            //actual swap operation
            head->next = swap->next;
            if (n != 1) //checks if prev (previous node) needs to be used
                prev->next = swap;
            swap->next = temp;
            //we still haven't dealt 
        }
        head = head->next;
        count++;
    }
}

/*Count nodes*/
int countList(node *head)
{
	int count = 0;

	while (head)
	{
		head = head->next;
		count++;
	}
	return count;
}

//delete node at position (for discussion)
void delAtpos(node *head, int pos)
{
	node *temp, *prevnode;
	int i, count = 0;

	i = countList(head);

	if (pos < 0 || pos > i)
	{
		printf("Error: position out of range\n");
		return;
	}
	else
	{
		temp = head;
		while (pos != count)
		{
			prevnode = temp;
			temp = temp->next;
			count++;
		}
		prevnode->next = temp->next;
		//free(temp);
		return;
	}

}

int main(void)
{
    node *head = NULL;
    node new1, new2, new3, new4, new5, new6, new7, new8;
    node *new9, *new10;
    head = malloc(sizeof(node));


    head = &new1;

    new1.data = 6;
    new1.next = &new4;

    new4.data = 8;
    new4.next = &new2;

    new2.data = 5;
    new2.next = &new3;

    new3.data = 7;
    new3.next = NULL;

    new5.data = 10;
    new5.next = NULL;

    new6.data = 24;
    new6.next = NULL;

    new7.data = 45;
    new7.next = NULL;
    
    new8.data = 2325;
    new8.next = NULL;

    new9 = create_node(355);
    new10 = create_node(87);

    print_list(head);
    
    //append to the end of the list.
    head = &new1;
    append_to_list(head, &new5);
    head = &new1;
    append_to_list(head, &new6);
    head = &new1;
    head = push(head, &new7);
    head = push(head, &new8);
    head = push(head, new9);
    print_list(head);
    printf("\n");
    printf("after insertion\n");
    insert_after_n(head, new10, 2);
    print_list(head);
    printf("\n");
    printf("after swap\n");
    swap_after_n(head, 1);
    print_list(head);

    delAtpos(head, 3);
    printf("After deletion\n");
    print_list(head);
}
