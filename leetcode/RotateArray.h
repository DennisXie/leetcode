#ifndef ROTATEARRAY_H
#define ROTATEARRAY_H
#pragma once
#include <vector>

class RotateArray
{
public:
	static void rotate(std::vector<int> &nums, int k);

	static void rotate(int *nums, int numsSize, int k);
};

#endif