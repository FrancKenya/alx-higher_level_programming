#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle
* @list: singly linked list being checkef
* Return: integer
*/

int check_cycle(listint_t *list)
{
listint_t *i = list;
listint_t *j = list;

if (list == NULL || list->next == NULL)
{
return (0);  /* if no cycle return 0 */
}
while (j->next != NULL && j->next->next != NULL)
{
i = i->next;
j = j->next->next;
if (i == j)
{
return (1); /* returns 1 if cycle found */
}
}
return (0); /* retruns 0 if no cycle found */
}
