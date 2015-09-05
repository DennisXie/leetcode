#pragma once

#include <vector>
#include <string>
#include <cstring>
#include <cstdio>

class TheLargestNum
{
public:
	static bool smaller(int a, int b);

	static std::string largest(std::vector<int> &nums);

	template<class _Fn>
	static void qsort(std::vector<int>::iterator start, std::vector<int>::iterator end, _Fn less);
};


template<class _Fn>
void qsort(std::vector<int>::iterator start, std::vector<int>::iterator end, _Fn less)
{
	using namespace std;
}
