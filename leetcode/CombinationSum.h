#pragma once
#include <vector>

std::vector<std::vector<int>> combinationSum(std::vector<int> &candidates, int target);

void findAns(std::vector<int> &candidates, int target, int n, std::vector<std::vector<int>> &ans, std::vector<int> &aAns);
