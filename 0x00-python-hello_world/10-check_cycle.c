#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
struct listint_t
{
	int data;
	struct listint_t *next;
};

typedef struct listint_t listint_t;

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If slow and fast pointers meet, there is a cycle. */
		if (slow == fast)
		{
			return 1;
		}
	}

	/* If the loop terminates, there's no cycle. */
	return 0;
}
