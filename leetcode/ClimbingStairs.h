#pragma once

inline int climbStairs(int n)
{
    int m = 1, k = 2;
    if (n == 1) return m;
    if (n == 2) return k;

    int i = 3;
    int s = 0;
    for (i = 3; i <= n; ++i)
    {
        s = m + k;
        m = k;
        k = s;
    }

    return k;
}