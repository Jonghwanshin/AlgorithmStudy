#include <iostream>
#define N 14
using namespace std;

bool promising(int level);
bool queens(int level);
int cols[N + 1] = { 0 };
int n = 0;
int cnt = 0;

int main()
{
	cin >> n;

	queens(0);

	cout << cnt << endl;

	return 0;
}

bool queens(int level)
{
	if (!promising(level))
		return false;

	else if (level == n)
	{
		cnt++;
		return true;
	}

	for (int i = 1; i <= n; i++) {
		cols[level + 1] = i;
		queens(level + 1);
	}
}

bool promising(int level)
{
	for (int i = 1; i < level; i++)
	{
		if (cols[i] == cols[level])
			return false;
		else if (level - i == abs(cols[level] - cols[i]))
			return false;
	}
	return true;
}