#ifndef REMOVELINKEDLISTELEMENTS_H
#define REMOVELINKEDLISTELEMENTS_H
#pragma once

struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr) {}
};

class RemoveLinkedListElements
{
public:
	ListNode *removeElements(ListNode *head, int val);
};

#endif