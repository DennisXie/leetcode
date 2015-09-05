//#include <iostream>
extern "C"
{
#include "ReverseNodesinKGroup.h"
}
#include <cstdio>
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	//ListNode *head = nullptr;
	//head = new ListNode(0);
	//ListNode *pLast = head;
	//ListNode *pNow = nullptr;
	//
	//for (int i = 1; i < 8; ++i)
	//{
	//	pNow = new ListNode(i);
	//	pLast->next = pNow;
	//	pLast = pNow;
	//}

	//pLast->next = head;

	//ListNode *pM = DetectCycle::detectCycle(head);
	//
	//if (pM != nullptr) cout << pM->val << endl;

	//pNow = head;
	//bool flag = true;
	//while (pNow!=pM || flag)
	//{
	//	cout << pNow->val << " ";
	//	pLast = pNow;
	//	pNow = pNow->next;
	//	if (pNow == pM) flag = false;
	//	if (pLast != nullptr) delete pLast;
	//}
	//cout << str << endl;
	//for (auto ch = str.rbegin(); ch != str.rend(); ++ch)
	//{
	//	cout << *ch;
	//}
	//cout << endl;
    //int *ans = searchRange(a, 6, 5, &i);
	//printf("%d %d\n", ans[0], ans[1]);
    
    //ListNode a, b, c;
    //a.val = 1;
    //b.val = 2;
    //c.val = 3;
    //a.next = &b;
    //b.next = &c;
    //c.next = NULL;
    //ListNode *p = reverseGroup(&a, 2);
    int a = 1, b = 2;
    (a += 2) *= b;
    printf("%d\n", a);
	system("pause");
	return 0;
}
