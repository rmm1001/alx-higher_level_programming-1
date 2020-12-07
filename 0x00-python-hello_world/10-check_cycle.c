#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * Description: a singly list has a cycle when one of the elements within
 * the list points to the head address
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/**
	 * Step to explain on the interviewer:
	 * save the head memory address on a temp variable
	 * go over the singly list check if the node is pointing to the head
	 * If yes, return 1, if no, continue.
	 * Return 0 if the loop when until the end (did not find any
	 * case where the node was pointing to the head)
	*/
	listint_t *head;
	listint_t *current;

	head = list;
	current = head->next;

	while (current != NULL)
	{
		if (current == head)
			return (1);
		current = current->next;
	}

	return (0);
}
