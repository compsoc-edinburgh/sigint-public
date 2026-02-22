#include <stdio.h>
#include <string.h>

int main() {
    char str[100];

    printf("Enter a flag: ");
    fgets(str, sizeof(str), stdin);

    if (strcmp(str, "SIGINT{1t_0nl7_g3t5_h4rd3r_fr0m_h3r3}\n\x00") == 0) {
        printf("Correct Flag!\n");
    } else {
        printf("Wrong Flag!\n");
    }
    return 0;
}