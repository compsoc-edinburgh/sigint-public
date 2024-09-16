#include <stdio.h>
#include <stdlib.h>

int main() {
    // initial setup
    int initialBalance = 20;
    int yourBalance = initialBalance;
    int myBalance = initialBalance;
    int flagPrice = 1337;

    // load flag from file
    char flag[100];
    FILE *f = fopen("flag.txt", "r");
    fgets(flag, 100, f);

    while (1) {
        printf("Your balance: %d. My balance: %d\n", yourBalance, myBalance);
        printf("Please choose an action:\n");
        printf("[1] Transfer\n");
        printf("[2] Buy flag\n");
        printf("Enter a number:\n");
        fflush(stdout);

        int choice;
        scanf("%d", &choice);

        if (choice == 1) {
            printf("Transfer to me\n");
            printf("Enter value:\n");
            fflush(stdout);
            long value;
            scanf("%ld", &value);
            if (value < 0) {
                printf("You can only transfer positive balance\n");
            } else if (((int) (myBalance - value) < 0)) {
                printf("You don't have enough balance\n");
            } else {
                myBalance = myBalance + value;
                yourBalance = yourBalance - value;
            }
        } else if (choice == 2) {
            if (yourBalance < flagPrice) {
                printf("You can't afford the flag\n");
            } else {
                printf("Here is the flag: %s\n", flag);
                exit(0);
            }
        } else {
            printf("Invalid choice\n");
            exit(1);
        }
        printf("\n");
    }
}
