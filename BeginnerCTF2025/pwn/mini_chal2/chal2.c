#include <stdio.h>
#include <string.h>

void win() {
    printf("You win, here is the flag!\n");
    FILE *fp = fopen("flag.txt", "r");
    if(fp == NULL){
        printf("If you run this locally, verify you have a flag file. Otherwise contact the staff of the event.\n");
        return;
    }
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s\n", buffer);
    }
    return;
}

void main(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0); 
    volatile char *cond = "secret";
    volatile char input[0x200];
    scanf("%s", (char*)input);
    if(strcmp(&cond, "password\x00") == 0){
        win();
    }
    return;
}