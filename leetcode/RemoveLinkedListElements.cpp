#include "RemoveLinkedListElements.h"

ListNode *RemoveLinkedListElements::removeElements(ListNode *head, int val)
{
	while ((head != nullptr) && (head->val == val))
	{
		ListNode *tempNode = head->next;
		delete head;
		head = tempNode;
	}

	if (head == nullptr) return nullptr;

	ListNode *last = head;
	ListNode *cur = head->next;
	while (cur)
	{
		if (cur->val == val)
		{
			last->next = cur->next;
			delete cur;
			cur = last->next;
		}
		else
		{
			last = cur;
			cur = cur->next;
		}
	}

	return head;
}