#include <string.h>
#include <stdlib.h>
#include "MinimumWindowSubstring.h"

char *minWindow(char *s, char *t)
{
    if (s == NULL || t == NULL) return NULL;

    short hashtable[256];
    short countable[256] = {0};
    int i = 0, j, slen, tlen, min, start = -1, end = -1;
    int count = 0;

    slen = strlen(s);
    tlen = strlen(t);

    min = slen;

    //initial the hashtable.
    for (i = 0; i < 256; ++i)
    {
        hashtable[i] = -1;
    }

    //count is the different character num in t.
    for (i = 0; i < tlen; ++i)
    {
        hashtable[t[i]] = 0;
        ++count;
        ++countable[t[i]];
    }
        

    j = 0;
    for (i = 0; i < slen; ++i)
    {
        if (hashtable[s[i]] != -1)
        {
            ++hashtable[s[i]];
            //hashtable[s[i]] == 0, find a new character for the first time.
            if (hashtable[s[i]] == countable[s[i]])
            {
                count -= countable[s[i]];
            }
            
            //move the idx j.
            if (hashtable[s[i]] > countable[s[j]])
            {
                while (hashtable[s[j]] == -1 || hashtable[s[j]] > countable[s[j]])
                {
                    if (hashtable[s[j]] != -1)
                        --hashtable[s[j]];
                    ++j;
                }
            }

            //if i~j contain all the char and the length is smaller, update the start, end, min.
            if (count == 0 && i - j < min)
            {
                min = i - j;
                start = j;
                end = i;
            }
        }
    }
    
    char *ans;
    if (count > 0)
    {
        ans = (char *)malloc(sizeof(char));
        ans[0] = 0;
        return ans;
    }


    ans = (char *)malloc((min + 2) * sizeof(char));
    for (i = start; i <= end; ++i)
    {
        ans[i - start] = s[i];
    }
    ans[min + 1] = 0;   //append the '\0';

    return ans;
}
