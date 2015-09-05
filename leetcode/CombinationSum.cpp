#include "CombinationSum.h"

using namespace std;

vector<vector<int>> combinationSum(vector<int> &candidates, int target)
{
	vector<vector<int>> ans;
	vector<int> aAns;
	findAns(candidates, target, 0, ans, aAns);
	return ans;
}


void findAns(vector<int> &candidates, int target, int n, vector<vector<int>> &ans, vector<int> &aAns)
{
	if (n > target) return;
	if (n == target)
	{
		ans.push_back(aAns);
	}

	for (vector<int>::value_type i : candidates)
	{
		if (aAns.empty() || i >= aAns.back())
		{
			aAns.push_back(i);
			findAns(candidates, target, n + i, ans, aAns);
			aAns.pop_back();
		}
	}
}
