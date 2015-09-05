#include "LongestPalindromicSubstring.h"

using namespace std;

string LongestPalindromicSubstring::longestPalindrome(string s)
{
	string ans;
	string temp;
	auto fn = [&s](string &temp1, long pre, long last)
	{
		while (pre >= 0 && last < static_cast<long>(s.length()))
		{
			if (s[pre] == s[last])
			{
				temp1.insert(0, 1, s[pre]);
				temp1.append(1, s[last]);
				--pre;
				++last;
			}
			else
			{
				break;
			}
		}
		return temp1.length();
	};

	for (long i = 0; i < static_cast<long>(s.length()); ++i)
	{
		temp = "";
		//i is the middle char.
		long pre = i - 1, last = i + 1;
		temp.append(1, s[i]);
		if (fn(temp, pre, last) > ans.length()) ans = temp;

		temp = "";
		//i is not the middle char, e.g. aabbaa
		pre = i; last = i + 1;
		if (fn(temp, pre, last) > ans.length()) ans = temp;

		if (ans.length() == s.length()) break;
	}

	return ans;
}
