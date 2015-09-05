#include <cassert>
#include <algorithm>
#include "NextPermutation.h"

using namespace std;

void nextPermutation(vector<int> &nums)
{
	if (nums.size() == 0 || nums.size() == 1) return;

	int _max = nums[nums.size() - 1];
	vector<int>::iterator last = nums.end();
	--last;
	--last;

	bool flag = false;
	//防止last == nums.begin()时，继续--last产生未定义行为～
	for (int i = static_cast<int>(nums.size() - 2); i >= 0; --i, last != nums.begin() ? --last : last)
		if (_max < nums[i])
		{
			_max = nums[i];
		}
		else
		{
			int _min = _max;
			int idx = i;
			for (int j = nums.size() - 1; j > i; --j)
				if (nums[j] > nums[i] && nums[j] <= _min)
				{
					_min = nums[j];
					idx = j;
				}
			
			if (idx == i) continue;

			int temp = nums[idx];
			nums[idx] = nums[i];
			nums[i] = temp;

			++last;
			sort(last, nums.end());
			--last;
			flag = true;
			break;
		}
	if (!flag) sort(nums.begin(), nums.end());
}
