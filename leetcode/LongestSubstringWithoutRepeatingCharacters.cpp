#include "LongestSubstringWithoutRepeatingCharacters.h"

using namespace std;

int LongestSubstring::lengthOfLongestSubstring(string s)
{
	string substring;
	string::size_type index = 0;
	long maxLength = 0;
	for (const string::value_type &ch : s)
	{
		index = substring.rfind(ch);
		if (index == string::npos)
		{
			substring.append(1, ch);
		}
		else
		{
			if (substring.length() > maxLength) maxLength = substring.length();

			substring.erase(0, index + 1);
			substring.append(1, ch);
		}
	}

	if (substring.length() > maxLength) maxLength = substring.length();
	return maxLength;
};