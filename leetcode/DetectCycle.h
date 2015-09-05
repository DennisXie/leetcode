#ifndef DETECTCYCLE_H
#define DETECTCYCLE_H
#pragma once

struct ListNode
{
	int val;
	ListNode* next;
	ListNode(int x) :val(x){};
};


class DetectCycle{
public:
	static ListNode *detectCycle(ListNode *head);
};
#endif