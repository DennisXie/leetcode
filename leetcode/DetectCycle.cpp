#include "DetectCycle.h"

/*
�蹲��n���ڵ㣬���Ϊ0~n-1�����k��Ϊ������㡣
��ô�����Ľڵ���Ϊn-k��
1.	pOne�ڵ���k���󵽴ﻷ����㣬��ʱpTwo����2k�����ڻ�������k���Ժ󵽴ﻷ����ڣ�
	�ڻ�������k�������ԣ��뻷����ڵľ���Ϊ(n-k)-k%(n-k)��
2.	��ʱ��pOne������(n-k)-k%(n-k)�ͻᱻpTwo׷�ϡ�׷�Ϻ󣬾໷�����k%(n-k).
3.	�໷�����k%(n-k)���������Ľڵ���Ϊn-k������Ϊn-k������˵��������k���͸պ���
	������ڴ���������������ǻ�����ھ�������ͷ�ľ��롣
4.	�ʣ���pTwo׷��pOne�Ժ���һ��ָ�����ʼ���������pOne�����ĵط���Ϊ�������
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
