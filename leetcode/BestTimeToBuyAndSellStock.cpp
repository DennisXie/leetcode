#include <cstdlib>
#include "BestTimeToBuyAndSellStock.h"

int maxProfit(int *prices, int pricesSize)
{
	int maxPro = 0;
	int i = 0, j = 0;
	int *minPrice = (int *)malloc(pricesSize * sizeof(int));
	minPrice[0] = prices[0];
	for (i = 1; i < pricesSize; ++i)
	{
		if (minPrice[i - 1] < prices[i])
			minPrice[i] = minPrice[i - 1];
		else
			minPrice[i] = prices[i];
	}

	for (i = pricesSize - 1; i > 0; --i)
	{
		if (prices[i] - minPrice[i - 1] > maxPro) maxPro = prices[i] - minPrice[i - 1];
	}

	free(minPrice);
	return maxPro;
}


int maxProfit2(int *prices, int pricesSize)
{
	int maxProfit = 0;
	int i = 0, j = 0;
	int flag = 0;
	for (i = 0; i < pricesSize; ++i)
	{
		if (i == pricesSize - 1 && flag == 1)
		{
			maxProfit = maxProfit + prices[i] - j;
			break;
		}
		else if (i == pricesSize - 1)
		{
			break;
		}

		if (prices[i] < prices[i + 1] && flag == 0)
		{
			j = prices[i];
			flag = 1;
		}

		if (prices[i] > prices[i + 1] && flag == 1)
		{
			maxProfit = maxProfit + prices[i] - j;
			j = 0;
			flag = 0;
		}
	}

	return maxProfit;
}


int maxProfit3(int *prices, int pricesSize)
{
	int maxProfit = 0;
	int i = 0;
	int *fmin = (int *)malloc(pricesSize * sizeof(int));
	int *fprofit = (int *)malloc(pricesSize * sizeof(int));
	int *rmax = (int *)malloc(pricesSize * sizeof(int));
	int *rprofit = (int *)malloc(pricesSize * sizeof(int));

	fmin[0] = prices[0];
	fprofit[0] = 0;
	for (i = 1; i < pricesSize; ++i)
	{
		if (fmin[i - 1] < prices[i])
			fmin[i] = fmin[i - 1];
		else
			fmin[i] = prices[i];

		fprofit[i] = 0;
	}

	rmax[pricesSize - 1] = prices[pricesSize - 1];
	rprofit[pricesSize - 1] = 0;
	for (i = pricesSize - 2; i >= 0; --i)
	{
		if (rmax[i + 1] > prices[i])
			rmax[i] = rmax[i + 1];
		else
			rmax[i] = prices[i];
		rprofit[i] = 0;
	}

	int temp;
	for (i = 1; i < pricesSize; ++i)
	{
		temp = prices[i] - fmin[i];
		if (temp < fprofit[i - 1])
			fprofit[i] = fprofit[i - 1];
		else
			fprofit[i] = temp;
	}

	maxProfit = fprofit[pricesSize - 1];

	for (i = pricesSize - 2; i >= 0; --i)
	{
		temp = rmax[i] - prices[i];
		if (temp < rprofit[i + 1])
			rprofit[i] = rprofit[i + 1];
		else
			rprofit[i] = temp;
	}

	for (i = 0; i < pricesSize; ++i)
	{
		temp = fprofit[i] + rprofit[i];
		if (temp > maxProfit) maxProfit = temp;
	}

	return maxProfit;
}
