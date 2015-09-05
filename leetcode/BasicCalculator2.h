#ifndef BASICCALCULATOR2_H
#define BASICCALCULATOR2_H
#pragma once

#include <stack>
#include <string>

class BasicCalculator2
{
private:
	std::stack<char> m_opStack;
	std::stack<int> m_numStack;

public:
	int calculate(std::string s);

	int calc(char op, int val1, int val2)
	{
		if (op == '+')
		{
			val1 = val1 + val2;
		}
		else if (op == '-')
		{
			val1 = val1 - val2;
		}
		else if (op == '*')
		{
			val1 = val1 * val2;
		}
		else
		{
			val1 = val1 / val2;
		}
		return val1;
	}
};

#endif