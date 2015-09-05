#include "RemoveNthNodeFromEndOfList.h"

ListNode *removeNthFromEnd(ListNode *head, int n)
{
	ListNode *pn = head, *p1 = head, *pPre = nullptr;
	for (int i = 0; i < n; i++)
	{
		p1 = p1->next;
	}

	while (p1)
	{
		p1 = p1->next;
		pPre = pn;
		pn = pn->next;
	}

	if (pPre)
	{
		pPre->next = pn->next;
		delete pn;
	}
	else
	{
		head = pn->next;
		delete pn;
	}

	return head;
}