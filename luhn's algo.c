#include <stdio.h>
#include <cs50.h>

int n = 0;
long o;

int check_every_other_digit(long x);

int main(void)
{
    long x;
    do
    {
        x = get_long("Number: ");
    }
    while (x < 0);

    o = x;

    int check_sum = check_every_other_digit(x);

    if ((check_sum % 10 == 0 && (o >= 340000000000000 && o <= 350000000000000)) || (check_sum % 10 == 0 && (o >= 370000000000000 && o <= 380000000000000)))
    printf("AMEX\n");

    else if ((check_sum % 10 == 0 && (o >= 5100000000000000 && o < 5600000000000000)))
    printf("MASTERCARD\n");

    else if ((check_sum % 10 == 0 && (o >= 4000000000000 && o < 5000000000000)) || (check_sum % 10 == 0 && (o >= 4000000000000000 && o <= 5000000000000000)))
    printf("VISA\n");

    else
    printf("INVALID\n");
}

int check_every_other_digit(long x)
{
    int counter = 1;
    {
        do
        {
            if (counter % 2 == 0)
            {
                int a = x % 10;
                x = x / 10;
                a = a * 2;
                if (a >= 10)
                {
                    n = n + (a / 10) + (a % 10);
                }
                else
                {
                    n = n + a;
                }
            }
            else
            {
                int b = x % 10;
                n = n + b;
                x = x / 10;
            }
            counter++;
        } while (x > 0);
    }
    return n;
}
