#ifndef REMOVEELEMENTS_H
#define REMOVEELEMENTS_H
#pragma once

#include <vector>
using namespace std;
class RemoveElements
{

public:
	static int remove(vector<int> &nums, int val)
	{
		bool bStop = false;
		vector<int>::iterator it = nums.begin();
		while (!bStop)
		{
			
			while (it != nums.end())
			{
				if (val == *it)
				{
					nums.erase(it);
					it = nums.begin();
					break;
				}
				++it;
			}
			if (it == nums.end()) bStop = true;
		}

		return nums.size();
	}
};

#endif