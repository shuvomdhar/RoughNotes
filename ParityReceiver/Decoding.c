#include <stdio.h>
#include <string.h>

int verify_parity(const char *binary, char parity_choice)
{
    size_t i;
    int count = 0;
    size_t len = strlen(binary);

    // Count the number of 1's in the binary string excluding the parity bit
    for (i = 0; i < len - 1; i++)
    {
        if (binary[i] == '1')
        {
            count++;
        }
    }

    // Check the parity bit
    char expected_parity_bit;
    if (parity_choice == 'e')
    {
        expected_parity_bit = (count % 2 == 0) ? '0' : '1';
    }
    else if (parity_choice == 'o')
    {
        expected_parity_bit = (count % 2 == 0) ? '1' : '0';
    }
    else
    {
        printf("Invalid parity choice!\n");
        return -1; // Return an error code for invalid parity choice
    }

    return binary[len - 1] == expected_parity_bit;
}

int main()
{
    char binary[100];
    char parity_choice;

    // Input the received parity encoded binary number as a string
    printf("Enter the received parity encoded binary number: ");
    scanf("%s", binary);

    // Ask the user for parity type
    printf("Choose parity - even (e) or odd (o): ");
    scanf(" %c", &parity_choice);

    // Verify the parity
    if (verify_parity(binary, parity_choice))
    {
        printf("The data is valid.\n");
    }
    else
    {
        printf("The data is invalid.\n");
    }

    return 0;
}