#include "EditDistance.h"
#include <stdlib.h>

int minDistance(char *word1, char *word2)
{
    if (word1 == NULL || word2 == NULL) return -1;
    
    int len1 = 0, len2 = 0;
    int i = 0, j = 0, tempmin;
    
    while (word1[len1++] != 0);
    while (word2[len2++] != 0);
    
    int (*mindis)[503] = (int (*)[503])malloc(503 * 503 * sizeof(unsigned int));

    //初始化边界数据
    for (i = 0; i <= len1; ++i)
        mindis[i][0] = i;

    for (i = 0; i <= len2; ++i)
        mindis[0][i] = i;

    //f[i][j] = f[i - 1][j - 1] a[i] == a[j];
    //f[i][j] = min(f[i-1][j-1], f[i][j-1], f[i-1][j]) + 1;
    for (i = 1; i <= len1; ++i)
        for (j = 1; j <= len2; ++j)
        {
            if (word1[i - 1] == word2[j - 1])
            {
                mindis[i][j] = mindis[i - 1][j - 1];
            }
            else
            {
                tempmin = mindis[i - 1][j];
                if (tempmin > mindis[i][j - 1]) tempmin = mindis[i][j - 1];
                if (tempmin > mindis[i - 1][j - 1]) tempmin = mindis[i - 1][j - 1];
                mindis[i][j] = tempmin + 1;
            }
        }

    return mindis[len1][len2];
}
