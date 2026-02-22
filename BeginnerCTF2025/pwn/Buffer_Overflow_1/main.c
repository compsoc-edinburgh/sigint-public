#include <stdio.h>

void win() {
    puts("You win!");
    return execve("/bin/sh", 0, 0);
}

int main() {
    setbuf(stdout, NULL);

    char buffer[10];

    puts("Welcome to buffer overflow lite!");

    gets(&buffer);

    return 0;
}
