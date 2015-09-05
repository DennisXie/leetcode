#include "MinStack.h"

using namespace std;

void MinStack::push(int x)
{
	if (m_Stack.empty())
	{
		m_MinStack.push_back(x);
		m_Stack.push_back(x);
	}
	else
	{
		if (x < m_MinStack.back())
		{
			m_MinStack.push_back(x);
			m_Stack.push_back(x);
		}
		else
		{
			int m = m_MinStack.back();
			m_MinStack.push_back(m);
			m_Stack.push_back(x);
		}
	}
}


void MinStack::pop()
{
	if (!m_Stack.empty())
	{
		m_MinStack.pop_back();
		m_Stack.pop_back();
	}
}


int MinStack::top()
{
	if (!m_Stack.empty())
	{
		return m_Stack.back();
	}
	else
	{
		return -1;
	}
}


int MinStack::getMin()
{
	if (!m_MinStack.empty())
	{
		return m_MinStack.back();
	}
	else
	{
		return -1;
	}
}
