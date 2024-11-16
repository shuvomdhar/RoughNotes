#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[10], b[10], sum[10], chk[10], carry = 0, n, i, p, chks[20];
    printf("------------------Checksum program for two segments only----------------\n\r");
    printf("\n Enter the number of bits of each segment : ");
    scanf("%d", &n);
    printf("\n At the sender's end....");
    printf("\n\r--------------------------------------------------------\n\r");
    printf("\n\r Enter the first segment(%d bits one after another) : \n", n);
    for (i = n - 1; i >= 0; i--)
    {
        scanf("%d", &a[i]);
    }
    printf("\n\r Enter the second segment : \n");
    for (i = n - 1; i >= 0; i--)
    {
        scanf("%d", &b[i]);
    }
    for (i = 0; i < n; i++)
    {
        sum[i] = (a[i] + b[i] + carry) % 2;
        carry = (a[i] + b[i] + carry) / 2;
    }
    printf("\n sum ....");
    for (i = n - 1; i >= 0; i--)
        printf(" %d", sum[i]);
    if (carry == 1)
    {
        for (i = 0; i < n; i++)
        {
            p = (sum[i] + carry) % 2;
            carry = (sum[i] + carry) / 2;
            sum[i] = p;
        }
    }
    printf("\n Wrappedsum ....");
    for (i = n - 1; i >= 0; i--)
    {
        chk[i] = sum[i];
        printf(" %d", sum[i]);
    }
    printf("\n Checksum.....");
    for (i = n - 1; i >= 0; i--)
    {
        if (chk[i] == 1)
            chks[i] = 0;
        else
            chks[i] = 1;
        printf(" %d", chks[i]);
    }
    return 0;
}