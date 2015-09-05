#include <stdlib.h>
#include "ReverseNodesInKGroup.h"

void reverse(struct ListNode **, struct ListNode **);

struct ListNode *reverseGroup(struct ListNode *head, int k)
{
    if (head == NULL) return NULL;
    if (k == 1) return head;

    struct ListNode *pNode = head, *ans = NULL, *pStart = head;
    struct ListNode *pre = NULL, *next = NULL;
    int count = 1;


    while (pNode != NULL)
    {
        if (count == k)
        {
            count = 0;
            next = pNode->next;
            reverse(&pStart, &pNode);
            if (ans == NULL)
            {
                ans = pStart;
                pNode->next = next;
                pre = pNode;
                pStart = next;
            }
            else
            {
                pre->next = pStart;
                pNode->next = next;
                pre = pNode;
                pStart = next;
            }
        }
        pNode = pNode->next;
        ++count;//count the nodes.
    }

    if (ans == NULL) ans = head;
    return ans;
}


void reverse(struct ListNode **head, struct ListNode **tail)
{
    struct ListNode *pHead = *head, *pTail = *tail;
    if (pHead == NULL || pTail == NULL) return;

    pTail->next = NULL;
    struct ListNode *pPre = pHead, *pNode = pHead->next, *pNext = NULL;

    pPre->next = NULL;
    *tail = pPre;
    while (pNode != NULL)
    {
        pNext = pNode->next;
        pNode->next = pPre;
        pPre = pNode;
        pNode = pNext;
    }
    *head = pPre;
}
