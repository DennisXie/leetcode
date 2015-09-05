#include "RepeatedDNASequences.h"

using namespace std;

struct hashstring
{
    unsigned int times;
    unsigned int idx;
    hashstring(unsigned int x, unsigned int _idx) : times(x), idx(_idx){};
};


unsigned int code(char ch)
{
    switch (ch)
    {
    case 'A': return 0;
    case 'C': return 1;
    case 'G': return 2;
    case 'T': return 3;
    default: return 4;
    }
}


vector<string> findRepeatedDnaSequences(string s)
{
    vector<string> ans;
    unordered_map<unsigned int, hashstring> hashtable;

    if (s.length() < 10) return ans;

    unsigned int hashv = 0;
    for (int i = 0; i < 9; ++i)
        hashv = ((hashv << 2) | code(s[i]));

    for (int i = 9; i < s.length(); ++i)
    {
        hashv = (hashv << 2) | code(s[i]);
        unordered_map<unsigned int, hashstring>::iterator hashit = hashtable.find(hashv & 0xFFFFF);

        if (hashit != hashtable.end())
        {
            hashit->second.times = hashit->second.times + 1;
        }
        else
        {
            hashtable.insert(make_pair(hashv & 0xFFFFF, hashstring(1, i - 9)));
        }
    }

    for (const auto &hashr : hashtable)
    {
        if (hashr.second.times > 1)
        {
            ans.push_back(s.substr(hashr.second.idx, 10));
        }
    }

    return ans;
}