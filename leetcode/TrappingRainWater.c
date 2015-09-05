#include "TrappingRainWater.h"
#include <stdlib.h>

int trap(int *height, int heightSize)
{
    int fmax, ftotal, ftemptotal, rmax, rtotal, rtemptotal;
    fmax = 0;
    rmax = heightSize - 1;
    ftotal = 0;
    rtotal = 0;
    ftemptotal = 0;
    rtemptotal = 0;

    for (int i = 1; i < heightSize; ++i)
    {
        if (height[i] >= height[fmax])
        {
            ftotal += ftemptotal;
            ftemptotal = 0;
            fmax = i;
        }
        else
        {
            ftemptotal += height[fmax] - height[i];
        }

        if (height[heightSize - i - 1] > height[rmax])
        {
            rtotal += rtemptotal;
            rtemptotal = 0;
            rmax = heightSize - i - 1;
        }
        else
        {
            rtemptotal += height[rmax] - height[heightSize - i - 1];
        }
    }

    return ftotal + rtotal;
}