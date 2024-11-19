// #include <stdio.h>

// int main()
// {
//     int m[20], p[20], d[10], i, j, k, len, rem[10], divlen;
//     int m1[20], rem1[10];
//     printf("\n Enter the length of divisor\n");
//     scanf("%d", &divlen);
//     printf("\n Enter the divisor:\n");
//     for (i = 0; i < divlen; i++)
//     {
//         scanf("%d", &d[i]);
//     }
//     printf("\n Enter the length of data\n");
//     scanf("%d", &len);
//     printf("\n Enter the data:\n");
//     for (i = 0; i < len; i++)
//     {
//         scanf("%d", &m[i]);
//         p[i] = m[i];
//     }
//     for (i = len; i < len + (divlen - 1); i++)
//     {
//         m[i] = 0;
//     }
//     printf("\n The append value is: ");
//     for (i = 0; i < len + (divlen - 1); i++)
//     {
//         printf("%d", m[i]);
//     }
//     // ***********X-OR operation*************//
//     for (i = 0; i < len; i++)
//     {
//         if (m[i] == 1)
//         {
//             for (j = 0; j < divlen; j++)
//             {
//                 if (m[i + j] == d[j])
//                     rem[j] = 0;
//                 else
//                     rem[j] = 1;
//             }
//             for (k = 0; k < divlen; k++)
//             {
//                 m[i + k] = rem[k];
//             }
//         }
//         else
//         {
//             for (k = 0; k < divlen; k++)
//             {
//                 rem[k] = m[i + k];
//             }
//         }
//     }
//     printf("\n");
//     printf("\n CRC =");
//     for (i = 1; i < divlen; i++)
//     {
//         printf("%d", rem[i]);
//     }
// }

#include <stdio.h>

int main()
{
    int data[20], divisor[10], appended_data[30], rem[10], crc[10];
    int data_len, divisor_len, i, j, k;

    printf("\nEnter the length of data: ");
    scanf("%d", &data_len);

    printf("\nEnter the data:\n");
    for (i = 0; i < data_len; i++)
    {
        scanf("%d", &data[i]);
    }

    printf("\nEnter the length of divisor: ");
    scanf("%d", &divisor_len);

    printf("\nEnter the divisor:\n");
    for (i = 0; i < divisor_len; i++)
    {
        scanf("%d", &divisor[i]);
    }

    // Append (divisor_len - 1) zeros to the data
    for (i = 0; i < data_len; i++)
    {
        appended_data[i] = data[i];
    }
    for (i = data_len; i < data_len + divisor_len - 1; i++)
    {
        appended_data[i] = 0;
    }

    printf("\nAppended data: ");
    for (i = 0; i < data_len + divisor_len - 1; i++)
    {
        printf("%d", appended_data[i]);
    }

    // Perform division using XOR
    for (i = 0; i < data_len; i++)
    {
        if (appended_data[i] == 1) // Perform XOR only if the current bit is 1
        {
            for (j = 0; j < divisor_len; j++)
            {
                appended_data[i + j] = appended_data[i + j] ^ divisor[j];
            }
        }
    }

    // The remainder is stored in the last (divisor_len - 1) bits
    for (i = 0; i < divisor_len - 1; i++)
    {
        rem[i] = appended_data[data_len + i];
        crc[i] = rem[i];
    }

    printf("\nCRC: ");
    for (i = 0; i < divisor_len - 1; i++)
    {
        printf("%d", crc[i]);
    }

    // Append CRC to the original data
    printf("\nTransmitted message: ");
    for (i = 0; i < data_len; i++)
    {
        printf("%d", data[i]);
    }
    for (i = 0; i < divisor_len - 1; i++)
    {
        printf("%d", crc[i]);
    }

    return 0;
}
