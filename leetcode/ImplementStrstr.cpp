#include "ImplemenStrstr.h"
#include <new>

using namespace std;

//Sunday algorithm.
int strStr(string haystack, string needle)
{
	unordered_map<char, int> chMap;
	for (size_t i = 0; i < needle.size(); ++i)
	{
		auto it = chMap.find(needle[i]);
		if (it == chMap.end())
		{
			chMap.insert(make_pair(needle[i], static_cast<int>(i)));
		}
		else
		{
			it->second = i;
		}
	}

	int i = 0, j = 0;
	while (i < static_cast<int>(haystack.size()) && j < static_cast<int>(needle.size()))
	{
		if (haystack[i] == needle[j])
		{
			++i;
			++j;
		}
		else
		{
			int k = i + needle.size() - j;
			auto it = chMap.find(haystack[k]);
			if (it != chMap.end())
			{
				i = k - it->second;
				j = 0;
			}
			else
			{
				i = k + 1;
				j = 0;
			}
		}
	}

	int index = -1;
	if (j == needle.size())
	{
		index = i - needle.size();
	}

	return index;
}
