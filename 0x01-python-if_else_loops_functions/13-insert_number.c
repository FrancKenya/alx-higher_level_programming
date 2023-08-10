#include <stdlib.h>
#include "lists.h"

/**
* insert_node - pointer inserting a number in to a linked list
* @head: points to the head of the list
* @number: integer to be inserted
* Return: a pointer to the new node or NULL if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new_node;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL); /* failed allocation */
}
new_node->n = number;
if (node == NULL || node->n >= number)
{
new_node->next = node;
*head = new_node;
return (new_node);
}
while (node->next && node->next->n < number)
{
node = node->next;
}
new_node->next = node->next;
node->next = new_node;
return (new_node);
}
