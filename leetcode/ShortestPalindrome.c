#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include "ShortestPalindrome.h"

bool judgePalindrome(char *, int, int);

char *shortestPalindrome(char *s)
{
    int slen = strlen(s);
    int i = 0, idx = 0;

    for (i = slen - 1; i >= 0; --i)
    {
        if (judgePalindrome(s, 0, i))
        {
            idx = i;
            break;
        }
    }

    char *newStr = (char *)malloc((slen + slen - idx) * sizeof(char));

    for (i = idx + 1; i < slen; ++i)
    {
        newStr[slen - i - 1] = s[i];
    }

    strcpy(newStr + slen - idx - 1, s);

    return newStr;
}


bool judgePalindrome(char *s, int begin, int end)
{
    while (begin < end)
    {
        if (s[begin] == s[end])
        {
            ++begin;
            --end;
        }
        else
        {
            return false;
        }
    }

    return true;
}
