#include "houserobber2.h"

using namespace std;

int HouseRobber2::rob(vector<int> &nums)
{
	m_nMaxCash = 0;

	for (vector<int>::size_type i = 0; i < nums.size(); ++i)
	{
		cash.push_back(vector<int>(nums.size(), 0));
	}

	//start
	for (int i = 0; i < nums.size(); ++i)
	{
		//end
		cash[i][i] = nums[i];
		if (cash[i][i] > m_nMaxCash) m_nMaxCash = cash[i][i];
		for (int j = i; j < nums.size(); ++j)
		{
			if (j - 2 >= i)
			{
				int nTempCash = cash[i][j - 2] + nums[j];
				if (nTempCash > cash[i][j]) cash[i][j] = nTempCash;
			}

			if (j - 3 >= i)
			{
				int nTempCash = cash[i][j - 3] + nums[j];
				if (nTempCash > cash[i][j]) cash[i][j] = nTempCash;
			}

			if ((cash[i][j] > m_nMaxCash) && ((j + 1) % nums.size() != i)) m_nMaxCash = cash[i][j];
		}
	}

	return m_nMaxCash;
}

//not used
void HouseRobber2::find(vector<int>::size_type k, vector<int>::size_type start, vector<int>::size_type last, vector<int> &nums)
{
	if ((k + 1) % nums.size() == start) return;

	int nTempCash;
	nTempCash = cash[start][last] + nums[k];
	if (nTempCash > cash[start][k]) cash[start][k] = nTempCash;
	if (nTempCash > m_nMaxCash) m_nMaxCash = nTempCash;

	if (k + 2 < nums.size()) find(k + 2, start, k, nums);
	if (k + 3 < nums.size()) find(k + 3, start, k, nums);
}