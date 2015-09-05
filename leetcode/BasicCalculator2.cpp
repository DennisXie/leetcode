#include "BasicCalculator2.h"

using namespace std;

int BasicCalculator2::calculate(string s)
{
	int num = 0;

	for (const auto &i : s)
	{
		if ((i == '*') || (i == '/'))
		{
			if (m_opStack.empty() || ((m_opStack.top() != '*') && (m_opStack.top() != '/')))
			{
				m_numStack.push(num);
				m_opStack.push(i);
				num = 0;
			}
			else
			{
				char op = m_opStack.top();
				m_opStack.pop();
				int nTopNum = m_numStack.top();
				m_numStack.pop();
				nTopNum = calc(op, nTopNum, num);
				m_opStack.push(i);
				m_numStack.push(nTopNum);
				num = 0;
			}
		}
		else if ((i == '+') || (i == '-'))
		{
			if (m_opStack.empty())
			{
				m_numStack.push(num);
				m_opStack.push(i);
				num = 0;
			}
			else
			{
				while (!m_opStack.empty())
				{
					char op = m_opStack.top();
					m_opStack.pop();
					int nTopNum = m_numStack.top();
					m_numStack.pop();
					num = calc(op, nTopNum, num);

				}
				m_opStack.push(i);
				m_numStack.push(num);
				num = 0;
			}
		}
		else if (i == ' ')
		{
			continue;
		}
		else
		{
			num = num * 10 + (int)i - (int)'0';
		}
	}

	while (!m_opStack.empty())
	{
		char op = m_opStack.top();
		m_opStack.pop();
		int nTopNum = m_numStack.top();
		m_numStack.pop();
		num = calc(op, nTopNum, num);
	}

	return num;
}