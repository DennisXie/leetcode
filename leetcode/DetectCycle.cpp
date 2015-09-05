#include "DetectCycle.h"

/*
设共有n个节点，编号为0~n-1，编号k处为环的起点。
那么，环的节点数为n-k。
1.	pOne节点走k步后到达环的起点，此时pTwo走了2k步，在环外走了k步以后到达环的入口，
	在环内走了k步。所以，与环的入口的距离为(n-k)-k%(n-k)。
2.	此时，pOne继续走(n-k)-k%(n-k)就会被pTwo追上。追上后，距环的入口k%(n-k).
3.	距环的入口k%(n-k)步，而环的节点数为n-k（或者为n-k步）。说明，再走k步就刚好在
	环的入口处。这个距离正好是环的入口距离链表头的距离。
4.	故，在pTwo追上pOne以后，另一个指针从起始点出发，与pOne相遇的地方即为环的入口
*/


ListNode *DetectCycle::detectCycle(ListNode *head)
{
	if (head == nullptr) return nullptr;

	ListNode *pOne = head, *pTwo = head;
	do
	{
		pOne = pOne->next;
		if (pTwo->next != nullptr)
			pTwo = pTwo->next->next;
		else
			return nullptr;
		
		if (pOne == pTwo) break;
	} while (pOne != nullptr && pTwo != nullptr);

	if (pOne == nullptr || pTwo == nullptr) return nullptr;

	ListNode *pDet = head;
	while (pDet != pOne)
	{
		pDet = pDet->next;
		pOne = pOne->next;
	}

	return pDet;
}
