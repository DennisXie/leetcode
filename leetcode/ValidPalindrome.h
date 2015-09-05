#pragma once
#include <stdlib.h>
#include <string.h>

inline void mytolower(char *ch)
{
	if (*ch >= 'A' && *ch <= 'Z')
		*ch = *ch + 'z' - 'Z';
};

inline bool isPalindrome(char* s) {
	if (s == NULL) return true;

	int len = strlen(s);
	if (len == 0) return true;

	int i = 0, j = 0;
	for (i = 0; i < len; ++i)
	{
		mytolower(s + i);
	}

	i = 0;
	j = 0;
	while (j < len)
	{
		if (s[j] >= 'a' && s[j] <= 'z')
		{
			s[i] = s[j];
			++i;
			++j;
		}
		else
		{
			++j;
		}
	}

	s[i] = 0;

	len = strlen(s);
	//if (len == 0 || len == 1) return true;

	for (i = 0; i < len / 2; ++i)
	{
		if (s[i] != s[len - i - 1])
			return false;
	}

	return true;
}