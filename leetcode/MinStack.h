#pragma once

#include <deque>

class MinStack
{
private:
	std::deque<int> m_Stack;
	std::deque<int> m_MinStack;
public:
	void push(int x);

	void pop();

	int top();

	int getMin();
};