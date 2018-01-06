#include <stdio.h>
//using namespace std;

#define N_SIZE 1000000

void mergeSort(int st, int la);
void merge(int st, int half, int la);

int nArray[N_SIZE] = { 0 };
int sortArray[N_SIZE] = { 0 };
int number = 0;

int main()
{
//	cin.sync_with_stdio(false);
//	cin >> number;

	scanf("%d", &number);

	for (int i = 0; i < number; i++)
	{
		int temp = 0;
		scanf("%d", &temp);
		nArray[i] = temp;
	}

	mergeSort(0, number - 1);

	for (int i = 0; i < number; i++)
		printf("%d \n", nArray[i]);

	return 0;
}

void mergeSort(int st, int la)
{
	if (st < la)
	{
		int half = (st + la) / 2;
		mergeSort(st, half);
		mergeSort(half + 1, la);
		merge(st, half, la);
	}
}

void merge(int st, int half, int la)
{
//	int half = (st + la) / 2;
	int i = st;
	int j = half + 1;
	int k = st;

	while (i <= half && j <= la)
	{
		if (nArray[i] < nArray[j])
		{
			sortArray[k] = nArray[i];
			i++;
		}
		else 
		{
			sortArray[k] = nArray[j];
			j++;
		}
		k++;
	}

	while (i <= half)
		sortArray[k++] = nArray[i++];

	while (j <= la)
		sortArray[k++] = nArray[j++];

	for (int m = st; m <= la; m++)
		nArray[m] = sortArray[m];
}


