#include <stdlib.h>
#include "RegularExpressionMatch.h"

bool tryMatch(const char *s, const char *p)
{
    if (*s == 0 && *p == 0) return true;
    if (*s == 0 || *p == 0) return false;

    if (*(p + 1) == '*')
    {
        if (*p == *s || *p == '.')
            return tryMatch(s + 1, p) || tryMatch(s + 1, p + 2) || tryMatch(s, p + 2);
        else
            return tryMatch(s, p + 2);
    }
    else if (*p == *s || *p == '.')
    {
        return tryMatch(s + 1, p + 1);
    }
    else
    {
        return false;
    }
}

bool isMatch(const char *s, const char *p)
{
    if (s == NULL || p == NULL) return false;
    return tryMatch(s, p);
};
