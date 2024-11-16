#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[10], b[10], c[20], temp, sum1[10], chkr[20], carry, i, n, p;
    printf("Enter the number of bits in each segment : ");
    scanf("%d", &n);
    printf("\n\r At the RECEIVER's end....");
    carry = 0;
    printf("\n\r Enter the received bits one after another:\n\r ");
    for (i = n - 1; i >= 0; i--)
    {
        scanf("%d", &a[i]);
    }
    printf("\n\r");
    for (i = n - 1; i >= 0; i--)
    {
        scanf("%d", &b[i]);
    }
    printf("\n\rNext bits will be identified as checksum\n\r");
    for (i = n - 1; i >= 0; i--)
    {
        scanf("%d", &c[i]);
    }
    printf("\n\r---------- Calculating Receiver's Checksum----------\n\r");
    for (i = 0; i < n; i++)
    {
        sum1[i] = (a[i] + b[i] + c[i] + carry) % 2;
        carry = (a[i] + b[i] + c[i] + carry) / 2;
    }
    printf("\n sum ....");
    for (i = n - 1; i >= 0; i--)
        printf(" %d", sum1[i]);
    if (carry == 1)
    {
        for (i = 0; i < n; i++)
        {
            p = (sum1[i] + carry) % 2;
            carry = (sum1[i] + carry) / 2;
            sum1[i] = p;
        }
    }
    printf("\n Wrapped sum ....");
    for (i = n - 1; i >= 0; i--)
    {
        chkr[i] = sum1[i];
        printf(" %d", sum1[i]);
    }
    printf("\n Checksum.....");
    temp = 0;
    for (i = n - 1; i >= 0; i--)
    {
        if (chkr[i] == 1)
            chkr[i] = 0;
        else
            chkr[i] = 1;
        temp = temp + chkr[i];
        printf(" %d", chkr[i]);
    }
    if (temp != 0)
    {
        printf("\n\r Checksum FAILED, Received data is Corrupted.");
    }
    else
    {
        printf("\n\r Checksum PASSED.");
    }
    return 0;
}