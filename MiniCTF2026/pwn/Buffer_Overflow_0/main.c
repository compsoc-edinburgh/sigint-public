#include <stdio.h>
#include <fcntl.h>

int main() {
    setbuf(stdout, NULL);	

    char buffer[80] = { 0 };

    int fd = open("flag.txt", O_RDONLY);
    read(fd, &buffer[20], 60);

    puts("Welcome to baby's first buffer overflow!");

    int len = 0, c;
    while ((c = getchar()) != '\n' && len < 80)
        buffer[len++] = c;

    printf("You said: %s\n", buffer);

    return 0;
}
