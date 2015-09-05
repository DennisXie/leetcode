#ifndef REODERLIST_H
#define REODERLIST_H
#pragma once

struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr){};
};

class ReoderList
{
public:
	static void reoderList(ListNode *head);
};

#endif