#ifndef HOUSEROBBER2_H
#define HOUSEROBBER2_H
#pragma once

#include <vector>

class HouseRobber2
{
private:
	std::vector<std::vector<int>> cash;
	int m_nMaxCash;

public:
	int rob(std::vector<int> &nums);

private:
	void find(std::vector<int>::size_type k, std::vector<int>::size_type start,
			std::vector<int>::size_type last, std::vector<int> &nums);
};


#endif