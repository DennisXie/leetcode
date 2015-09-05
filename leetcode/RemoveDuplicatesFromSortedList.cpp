#include "RemoveDuplicatesFromSortedList.h"

ListNode *deleteDuplicates(ListNode *head)
{
	if (head == 0) return 0;
	ListNode *pnode = head;
	while (pnode)
	{
		while (pnode->next != 0 && pnode->val == pnode->next->val)
		{
			ListNode *temp = pnode->next->next;
			delete pnode->next;
			pnode->next = temp;
		}
		pnode = pnode->next;
	}

	return head;
}
