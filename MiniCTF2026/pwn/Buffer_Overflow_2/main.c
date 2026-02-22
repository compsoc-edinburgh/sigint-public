#include <stdio.h>
#include <string.h>

void win() {
    puts("You win!");
    return execve("/bin/sh", NULL, NULL);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    
    char buffer[16];

    puts("Welcome to buffer overflow pocket edition!");

    int len = 0, c;
    while ((c = getchar()) != '\n')
        buffer[len++] = c;

    if (strcmp(buffer, "p4ssw0rd") == 0) {
        printf("%11$p\n"); // 11 prints the canary

        volatile int ret = main();
        return ret;
    }

    return 0;
}
