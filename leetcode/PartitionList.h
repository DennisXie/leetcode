#ifndef PARTITIONLIST_H
#define PARTITIONLIST_H
#pragma once

struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) :val(x), next(nullptr){};
};


class PartitionList
{
public:
	static ListNode *partition(ListNode *head, int x)
	{
		ListNode *pSmallHead, *pBigHead, *pSmallTail, *pBigTail;
		pSmallHead = pBigHead = pSmallTail = pBigTail = nullptr;

		ListNode *pNode = head;
		while (pNode)
		{
			if (pNode->val < x)
			{
				if (pSmallHead == nullptr)
				{
					pSmallHead = pNode;
					pSmallTail = pNode;
				}
				else
				{
					pSmallTail->next = pNode;
					pSmallTail = pSmallTail->next;
				}
			}
			else
			{
				if (pBigHead == nullptr)
				{
					pBigHead = pNode;
					pBigTail = pNode;
				}
				else
				{
					pBigTail->next = pNode;
					pBigTail = pBigTail->next;
				}
			}

			pNode = pNode->next;
		}

		ListNode *ans = nullptr;
		if (pSmallHead == nullptr)
		{
			ans = pBigHead;
		}
		else
		{
			ans = pSmallHead;
			pSmallTail->next = pBigHead;
			if (pBigTail) pBigTail->next = nullptr;
		}

		return ans;
	}
};

#endif