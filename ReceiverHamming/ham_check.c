#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
	
	char data[100];
	int data1[100],data2[100];
	int dl,r,i,j,k,z,c,l;
	printf("\n enter the received data \n");	
	scanf("%s",data);
	
//************** Hamming check code start *************

	dl=strlen(data);
	i=0;
	while(1)
	{
		if(pow(2,i)>=dl+1)
			break;
		i++;	
	}
	r=i;
	j=dl-1;
	for(i=1;i<=dl;i++)
	{
		data1[i]=data[j]-48;
		j--;    
	}
	
	l=1;
	data2[0]=0;
	for(i=0;i<r;i++)
	{
		z=pow(2,i);
		c=0;
		for(j=z;j<=dl;j=z+k)
		{
			for(k=j;k<z+j;k++)
			{
				if(k<=dl)
					c=c+data1[k];
			}
		}
		data2[l]=c%2;
		data2[0]=data2[0]+data2[l];
		l++;
	}
		
	if(data2[0]==0)
		{
			printf("\n data recv ok \n");
				
		}
	else
		{
			printf("\n data recv wrong \n");
			j=0;
			for(i=r;i>=1;i--)
			{
				if(data2[i]==1)
				j=j+pow(2,(i-1));
			}
			printf("\n error at position %d",j);
			if(data1[j]==0)
				data1[j]=1;
			else
				data1[j]=0;
			printf("\n corrected codeword is: ");
			for(i=dl;i>=1;i--)
				printf("%d ",data1[i]);
			printf("\n");
		}

//************** Hamming code check complete *************
	
return(0);
}