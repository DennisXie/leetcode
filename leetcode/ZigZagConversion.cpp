#include "ZigZagConversion.h"

using namespace std;

string ZigZagConversion::convert(string text, int nRows)
{
	string ans;
	if (nRows == 1) return text;

	for (int i = 0; i < nRows; ++i)
	{
		string::size_type index = static_cast<string::size_type>(i);
		if (index == 0 || index == static_cast<string::size_type>(nRows - 1))
		{
			string::size_type idx = index;
			while (idx < text.length())
			{
				ans.append(1, text.data()[idx]);
				string::size_type next = idx + static_cast<string::size_type>(2 * nRows - 2);
				if (next == idx)
					break;
				else
					idx = next;
			}
		}
		else
		{
			int col = 0;
			string::size_type idx = index;
			while (idx < text.length())
			{
				ans.append(1, text.data()[idx]);
				if (col % 2 == 0)
				{
					idx = idx + static_cast<string::size_type>((nRows - 1 - i) * 2);
				}
				else
				{
					idx = idx + static_cast<string::size_type>(2 * i);
				}
				++col;
			}
		}
	}

	return ans;
}