#include "SortList.h"

ListNode *SortList::sortList(ListNode *head)
{
	int count = 0;
	ListNode *pNode = head;
	while (pNode)
	{
		++count;
		pNode = pNode->next;
	}
	sort(&head, count);
	return head;
}


void SortList::sort(ListNode **ppHead, int size)
{
	int count = 0;
	int count2 = 1;
	ListNode *pVal = *ppHead, *pCur, *pPre, *pHead = *ppHead;

	if (size < 2 || *ppHead == nullptr) return;
	pCur = pHead->next;
	pPre = pHead;
	int x = (*ppHead)->val;

	for (int i = 0; i < size - 1; ++i)
	{
		if (pCur->val < x)
		{
			pPre->next = pCur->next;
			pCur->next = pHead;
			pHead = pCur;
			pCur = pPre->next;
			++count;
		}
		else if (pCur->val == x)
		{
			if (pCur == pVal->next)
			{
				pVal = pCur;
				pPre = pCur;
				pCur = pCur->next;
			}
			else
			{
				ListNode *temp = pCur->next;
				pCur->next = pVal->next;
				pVal->next = pCur;
				pPre->next = temp;
				pVal = pCur;
				pCur = temp;
			}
			++count2;
		}
		else
		{
			pPre = pCur;
			pCur = pCur->next;
		}
	}

	sort(&pHead, count);
	sort(&(pVal->next), size - count - count2);
	*ppHead = pHead;
}
