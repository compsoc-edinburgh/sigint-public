#include <stdio.h>
#include <string.h>

void win() {
    printf("You win, here is the flag!\n");
    FILE *fp = fopen("flag.txt", "r");
    if(fp == NULL){
        printf("If ou run this locally, verify you have a flag file. Otherwise contact the staff of the event.\n");
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
    printf("Do you have something to tell me ?\n");
    char input[0x200];
    scanf("%s", input);

    return;
}