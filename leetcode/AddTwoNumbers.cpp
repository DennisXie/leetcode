#include "AddTwoNumbers.h"

ListNode *AddTwoNumbers::addTwoNumbers(ListNode *l1, ListNode *l2)
{
	ListNode *p1 = l1, *p2 = l2;
	ListNode *ans = nullptr;
	ListNode *pcur = nullptr;
	int nextNum = 0;

	while (p1 && p2)
	{
		ListNode *ptemp = new ListNode(0);
		ptemp->val = p1->val + p2->val + nextNum;
		nextNum = ptemp->val / 10;
		ptemp->val = ptemp->val % 10;
		if (pcur)
		{
			pcur->next = ptemp;
			pcur = ptemp;
		}
		else
		{
			pcur = ptemp;
			ans = ptemp;
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	while (p1)
	{
		ListNode *ptemp = new ListNode(0);
		ptemp->val = p1->val + nextNum;
		nextNum = ptemp->val / 10;
		ptemp->val = ptemp->val % 10;
		if (pcur)
		{
			pcur->next = ptemp;
			pcur = ptemp;
		}
		else
		{
			pcur = ptemp;
			ans = ptemp;
		}
		p1 = p1->next;
	}

	while (p2)
	{
		ListNode *ptemp = new ListNode(0);
		ptemp->val = p2->val + nextNum;
		nextNum = ptemp->val / 10;
		ptemp->val = ptemp->val % 10;
		if (pcur)
		{
			pcur->next = ptemp;
			pcur = ptemp;
		}
		else
		{
			pcur = ptemp;
			ans = ptemp;
		}
		p2 = p2->next;
	}

	if (nextNum)
	{
		ListNode *ptemp = new ListNode(0);
		ptemp->val = nextNum;
		if (pcur)
		{
			pcur->next = ptemp;
			pcur = ptemp;
		}
		else
		{
			pcur = ptemp;
			ans = ptemp;
		}
	}
	return ans;
}