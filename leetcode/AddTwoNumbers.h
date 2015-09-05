#pragma once

struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr){};
};


class AddTwoNumbers
{
public:
	static ListNode *addTwoNumbers(ListNode *l1, ListNode *l2);
};
