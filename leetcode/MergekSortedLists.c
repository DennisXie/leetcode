#include <stdlib.h>
#include "MergekSortedLists.h"

static struct ListNode *merge(struct ListNode *list1, struct ListNode *list2);

//O(kn*logn) space:O(1)
struct ListNode *mergeKLists(struct ListNode **lists, int listsSize)
{
    int idx = 0;
    int size = listsSize;
    if (lists == NULL || listsSize == 0) return NULL;

    while (size >= 2)
    {
        int i = 0;
        for (idx = 0; idx < size - 1; idx += 2, ++i)
        {
            lists[i] = merge(lists[idx], lists[idx + 1]);
        }

        if (idx == size - 1)
        {
            lists[i] = lists[size - 1];
        }

        size = size - (size >> 1);
    }

    return lists[0];
}


struct ListNode *merge(struct ListNode *list1, struct ListNode *list2)
{
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    struct ListNode *p1 = list1, *p2 = list2;
    struct ListNode *ans = NULL, *pNode = NULL;

    if (p1->val > p2->val)
    {
        ans = p2;
        pNode = p2;
        p2 = p2->next;
    }
    else
    {
        ans = p1;
        pNode = p1;
        p1 = p1->next;
    }

    while (p1 && p2)
    {
        if (p1->val > p2->val)
        {
            pNode->next = p2;
            p2 = p2->next;
        }
        else
        {
            pNode->next = p1;
            p1 = p1->next;
        }
        pNode = pNode->next;
    }

    if (p1 == NULL)
    {
        pNode->next = p2;
    }
    else
    {
        pNode->next = p1;
    }

    return ans;
}
