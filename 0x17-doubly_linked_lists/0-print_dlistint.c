#include "lists.h"

/**
 * print_dlistint - Prints all elements of a dlistint list
 *
 *@h: The head of the list
 *Return: returns the number of nodes traversed
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	dlistint_t *tmp;

	tmp = h;
	if (tmp == NULL)
	{
		printf("You passed an empty list");
		return;
	}
	while (tmp != NULL)
	{
		printf("%d\n", tmp->n);
		count += 1;
		tmp = tmp->next
	}
	return (count);
}
