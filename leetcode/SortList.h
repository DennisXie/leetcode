#ifndef SORTLIST_H
#define SORTLIST_H
#pragma once

struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) :val(x), next(nullptr){};
};

class SortList
{
public:
	static ListNode *sortList(ListNode *head);
	static void sort(ListNode **ppHead, int size);
};

#endif