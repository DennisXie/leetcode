#pragma once

template<int N>
int fibo()
{
	return fibo<N-1>() + fibo<N-2>();
}


template<>
int fibo<0>()
{
	return 1;
}

template<>
int fibo<1>()
{
	return 1;
}
