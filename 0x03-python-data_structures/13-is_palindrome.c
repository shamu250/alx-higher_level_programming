#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        listint_t *temp = slow->next;
        slow->next = prev_slow;
        prev_slow = slow;
        slow = temp;
    }

    // Check if the list has an odd number of elements
    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    // Compare the reversed first half with the second half
    while (prev_slow != NULL && slow != NULL)
    {
        if (prev_slow->n != slow->n)
        {
            is_palindrome = 0;
            break;
        }
        prev_slow = prev_slow->next;
        slow = slow->next;
    }

    // Restore the original list
    while (prev_slow != NULL)
    {
        listint_t *temp = prev_slow->next;
        prev_slow->next = slow;
        slow = prev_slow;
        prev_slow = temp;
    }

    // If the list originally had an odd number of elements, reconnect the mid node
    if (mid != NULL)
    {
        mid->next = slow;
    }

    return is_palindrome;
}
