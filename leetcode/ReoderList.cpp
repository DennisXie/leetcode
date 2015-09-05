#include "ReoderList.h"

void ReoderList::reoderList(ListNode *head)
{
	//ListNode *pVal, *pPre, *pNode;
	//
	//pVal = head;
	//while (pVal && pVal->next)
	//{
	//	//Find the last node
	//	pPre = pVal;
	//	pNode = pVal->next;
	//	while (pNode->next)
	//	{
	//		pPre = pNode;
	//		pNode = pNode->next;
	//	}
	//	pPre->next = nullptr;

	//	//Insert the last node
	//	pNode->next = pVal->next;
	//	pVal->next = pNode;
	//	pVal = pNode->next;
	//}
	if (head == nullptr || head->next == nullptr) return;

	//Count the total nodes;
	int count = 0;
	ListNode *pNode = head;
	while (pNode)
	{
		++count;
		pNode = pNode->next;
	}

	//Find the middle node;
	count = count / 2;
	pNode = head;
	while (count > 1)
	{
		--count;
		pNode = pNode->next;
	}
	ListNode *pHalf = pNode->next;
	pNode->next = nullptr;

	//Reverse the pHalf list;
	ListNode *pPre = nullptr, *pCur = nullptr, *temp = nullptr;
	pPre = pHalf;
	pCur = pHalf->next;
	pPre->next = nullptr;
	while (pCur)
	{
		temp = pCur->next;
		pCur->next = pPre;
		pPre = pCur;
		pCur = temp;
	}
	pHalf = pPre;

	//Emerge the two list;
	pNode = head;
	while (pNode)
	{
		temp = pHalf->next;
		pHalf->next = pNode->next;
		pNode->next = pHalf;
		pNode = pHalf->next;
		pPre = pHalf;
		pHalf = temp;
	}
	if (pHalf)
	{
		pPre->next = pHalf;
	}
}