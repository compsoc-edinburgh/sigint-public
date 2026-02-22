#include <stdio.h>
#include <fcntl.h>

int main() {
    setbuf(stdout, NULL);	

    puts("Echo as a Service!");

    char input_buffer[0x30] = { 0 };
    char output_buffer[0x40] = { 0 };
    fgets(input_buffer, 0x2f, stdin); 

    sprintf(output_buffer, "echo \'%s\'", input_buffer);
    system(output_buffer);

    return 0;
}
