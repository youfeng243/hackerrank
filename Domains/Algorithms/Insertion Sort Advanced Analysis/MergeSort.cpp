#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

static int Array[100005];
static int Left[100005];
static int Right[100005];

long long Merge( int start, int mid, int end )
{   
    int i = 0;
	int j = 0;
	int k = 0;
	long long cnt = 0;
	
	int leftlen = mid - start + 1;
	int rightlen = end - mid;

	for( i = start; i <= mid; i++ )
	{
		Left[i - start] = Array[i];
	}
	Left[leftlen] = 10000001;

	for( i = mid + 1; i <= end; i++ )
	{
		Right[i - mid - 1] = Array[i];
	}
	Right[rightlen] = 10000001;

	i = 0;
	j = 0;
	k = 0;
	while( i < leftlen || j < rightlen )
	{
		if( Left[i] <= Right[j] )
		{
			Array[k + start] = Left[i];
			i++;
		}
		else
		{
			Array[k + start] = Right[j];
			j++;
			cnt += leftlen - i;
		}   
		k++;
	}
	return cnt;
}

long long MergeSort( int start, int end )
{
	int mid = 0;
	long long cnt = 0;

	if( start == end )
	{
		return 0;
	}

	mid = (start + end) / 2;
	cnt += MergeSort( start, mid );
	cnt += MergeSort( mid + 1, end);
	cnt += Merge( start, mid, end );
	
	return cnt;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T = 0;
	int N = 0;

	scanf("%d", &T);
	for( int k = 0; k < T; k++ )
	{
		scanf("%d", &N);
		for( int i = 0; i < N; i++ )
		{
			scanf("%d", &Array[i]);
		}
		printf("%lld\n", MergeSort(0, N - 1));
	}
	return 0;
}
