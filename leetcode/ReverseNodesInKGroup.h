#ifndef REVERSENODEINKGROUP_H
#define REVERSENODEINKGROUP_H

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *reverseGroup(struct ListNode *head, int k);

#endif