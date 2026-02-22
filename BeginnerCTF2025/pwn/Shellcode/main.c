#include <stdio.h>
#include <fcntl.h>

int main() {
    setbuf(stdout, NULL);

    char buffer[0x110] = { 0 };

    int fd = open("flag.txt", O_RDONLY);
    read(fd, &buffer[20], 60);

    puts("GIVE ME SHELLCODE (up to 0x100 bytes)!");

    int len = 0, c;
    while ((c = getchar()) != '\n' && len < 0x100)

	    buffer[len++] = c;

    void (*func)() = (void(*)()) buffer;
    func();

    return 0;
}
