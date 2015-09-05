#ifndef ROTATELIST_H
#define ROTATELIST_H
#pragma once

struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) :val(x), next(nullptr) {};
};

class RotateList
{
public:
	static ListNode *rotateRight(ListNode *head, int k)
	{
		if (head == nullptr) return nullptr;
		int count = 0;
		
		//Count the total nodes;
		ListNode *pNode = head;
		while (pNode)
		{
			++count;
			pNode = pNode->next;
		}

		//Calc the true k;
		k = k % count;
		if (k == 0) return head;


		//Calc the first half nodes;
		int n = count - k;
		pNode = head;
		while (n > 1)
		{
			--n;
			pNode = pNode->next;
		}
		ListNode *pHalf = pNode->next;
		pNode->next = nullptr;

		ListNode *ans = pHalf;
		while (pHalf->next)
		{
			pHalf = pHalf->next;
		}
		pHalf->next = head;

		return ans;

	}
};

#endif