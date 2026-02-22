#include <stdio.h>

#include <stdbool.h>
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

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0); 
    int condition = 0;
    printf("I love repeating what you tell me. What will you make me say ?\n");
    printf("Condition: %p. Oups, did i say it too early ?\n", &condition);
    printf("Write quit if you want to stop talking to me :(");

    while(true){
        char buffer[0x100];
        read(0,buffer, sizeof(buffer));
        if(strcmp(buffer, "quit\n")==0){
            break;
        }
        printf(buffer);
        
        if (condition == 0xdeadbeef){
            win();
        } 
    }
    return 0;
}