#include "SubstringWithConcatenationOfAllWords.h"

using namespace std;

vector<int> findSubstring(string s, vector<string> &words)
{
	vector<int> ans;
	if (words.size() == 0 || s.length() == 0 || words[0].length() == 0) return ans;

	unordered_map<string, int> count_map;
	unordered_map<string, int> words_count;
	
	int word_len = (int)words[0].length();
	int counts = 0;

	for (const string &word : words)
	{
		++counts;
		unordered_map<string, int>::iterator it = words_count.find(word);
		if (it != words_count.end())
		{
			++(it->second);
		}
		else
		{
			words_count.insert(make_pair(word, 1));
		}
	}

	int s_len = (int)s.length();

	for (int i = 0; i <= s_len - counts * word_len; ++i)
	{
		count_map.clear();
		int j = 0;
		for (j = 0; j < counts; ++j)
		{
			string sub = s.substr(i + j * word_len, word_len);
			unordered_map<string, int>::iterator it = words_count.find(sub);
			if (it == words_count.end())
			{
				break;	
			}
			else
			{
				decltype(it) it2 = count_map.find(sub);
				if (it2 != count_map.end())
				{
					++(it2->second);
				}
				else
				{
					count_map.insert(make_pair(sub, 1));
					it2 = count_map.find(sub);
				}

				if (it2->second > it->second) break;
			}
		}

		if (j == counts)
		{
			ans.push_back(i);
		}
	}

	return ans;
}
