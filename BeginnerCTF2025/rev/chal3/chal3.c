#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const unsigned char indexes[] = {
    24, 7,  30, 21, 9,  25, 18, 
    4,  8,  20, 22, 12, 1,  26, 
    15, 13, 0,  23, 29, 14, 31,
    11, 3,  19, 27, 16, 10, 5, 
    2, 17, 28, 6
};
const unsigned char expected[] = {
    97, 95, 105, 116, 105, 118, 
    125, 105, 102, 123, 95, 
    117, 103, 95, 95, 110, 
    102, 101, 104, 95, 105, 
    105, 110, 110, 109, 115, 
    105, 111, 119, 100, 110, 111
};

char shifted_user_input[32];
char user_input [0x100];

int main() {   
    puts("Please give me your flag: ");
    
    fgets(user_input, 0x100, stdin);
    if (user_input[strlen(user_input)-1] == '\n') {
        user_input[strlen(user_input)-1] = '\0';
    }

    if (strlen(user_input) != 32) { 
        puts("Flag must be 32 characters long.\n");
        return 1;
    }

    for (unsigned i = 0; i < 32; i++) {
        shifted_user_input[indexes[i]] = user_input[i];
    }

    for (unsigned i = 0; i < 32; i++) {
        if ((unsigned char)shifted_user_input[i] != expected[i]) {
            puts("Wrong flag!\n");
            return 1;
        }
    }
    puts("Correct flag! Now submit it!\n");
    return 0; 
}