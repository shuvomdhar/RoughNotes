#include <stdio.h>

int main()
{
    int recv[20], div[10], rem[10], divlen, msglen, i, j, k;

    printf("\nEnter the length of divisor: ");
    scanf("%d", &divlen);

    printf("\nEnter the divisor:\n");
    for (i = 0; i < divlen; i++)
    {
        scanf("%d", &div[i]);
    }

    printf("\nEnter the length of received message: ");
    scanf("%d", &msglen);

    printf("\nEnter the received message:\n");
    for (i = 0; i < msglen; i++)
    {
        scanf("%d", &recv[i]);
    }

    // Perform division using XOR
    for (i = 0; i <= msglen - divlen; i++)
    {
        if (recv[i] == 1) // Perform XOR only if the current bit is 1
        {
            for (j = 0; j < divlen; j++)
            {
                recv[i + j] = recv[i + j] ^ div[j];
            }
        }
    }

    // Copy the remainder from the received message
    for (i = 0; i < divlen - 1; i++)
    {
        rem[i] = recv[msglen - divlen + 1 + i];
    }

    // Check if the remainder is all zeros
    int valid = 1; // Assume valid until proven otherwise
    for (i = 0; i < divlen - 1; i++)
    {
        if (rem[i] != 0)
        {
            valid = 0; // Invalid message
            break;
        }
    }

    if (valid)
        printf("\nThe received message is valid.\n");
    else
        printf("\nThe received message is corrupted.\n");

    return 0;
}