#include <stdio.h>

int main()
{
	int tc_num = 0;
	char op[7];
	int data = 0;
	int S = 0;
	int check = 0;
	scanf("%d",&tc_num);
	for(int i=0;i<tc_num;i++)
	{
		scanf(" %s %d",&op,&data);
		//printf("%s %d",op,data);
		switch(op[0]){
			case 'a':
				if(op[1] == 'd')
				{
					S = S | (1<<data);
				}
				else
				{
					S = (1 << 21)-1;
				}
				break;
			case 'c':
				check = (S & (1<<data));
				if(check > 0)
					printf("1\n");
				else
					printf("0\n");
				break;
			case 'r':
				S = S & ~(1<<data);
				break;
			case 't':
				S = S ^ (1<<data);
				break;
			case 'e':
				S = 0;
				break;
			default:
				break;
		} 
	}
}
