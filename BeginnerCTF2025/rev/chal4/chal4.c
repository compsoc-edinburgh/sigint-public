#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <openssl/md5.h>

static char HOST [256] = {0};

void show_flag() {
    FILE *f = fopen("/flag.txt", "r");
    if (!f) {
        puts("Correct serial! Now sign-into the server");
        return;
    }

    char flag[128];
    fgets(flag, sizeof(flag), f);
    printf("Heres your signup flag: %s\n", flag);
    fclose(f);
}

void get_hostname() {
    if (gethostname(HOST, sizeof(HOST) - 1) != 0) {
        perror("Couldnt get hostname");
        exit(1);
    }
}

bool unhex(const char* in, unsigned char* out, const int maxlength) {
    if (strlen(in) != maxlength * 2) { return false; }
    
    for (int i = 0; i < maxlength; i++) {
        if (sscanf(in + (i * 2), "%2hhx", &out[i]) != 1 ) {
            return false;
        }
    }
    return true;
}

bool attempt_to_login(const char* input) {
    unsigned char host_hash[MD5_DIGEST_LENGTH] = { 0 };
    MD5(HOST, strlen(HOST), host_hash);
    
    unsigned char input_hash[MD5_DIGEST_LENGTH] = { 0 };
    if (!unhex(input, input_hash, MD5_DIGEST_LENGTH))  {
        return false;
    }
    
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++){
        if (input_hash[i] != host_hash[i]) { return false; }
    }
    return true;
}


int main() {
    get_hostname();
    printf("Welcome to SIGINT's new AI-b2b-SaaS platform!\nPlease enter your login token: ");
    fflush(stdout);
    
    char input[128];
    if (!fgets(input, sizeof(input), stdin)) {
        perror("failed to read input");
        exit(1);
    }
    else if (input[strlen(input)-1] == '\n') {
        input[strlen(input)-1] = '\0';
    }
    
    if (!attempt_to_login(input)) {
        printf("Login failed for user %s\n", HOST);
        return 1;
    }

    printf("Login successful as %s!", HOST);
    
    while (1) {
        puts("\nChoose an option:\n\t1. Talk to AI\n\t2. Show flag\n\t3. Exit");
        fflush(stdout);
    __no_message:
        switch (getchar()) {
            case '1':
                printf("Waiting for the OpenAI API request ...");
                fflush(stdout);
                for (int _ = 0; _ < 10; _++) {
                    sleep(1);
                    putchar('.');
                    fflush(stdout);
                }
                puts("Out of api credits, please buy more to continue using the AI service.");
                break;
            case '2':
                show_flag();
                break;
            case '3':
                puts("Exiting. Goodbye!");
                return 0;
            case '\n':
                goto __no_message;
            default:
                puts("Invalid option. Please try again.");
                int c;
                while ((c = getchar()) != '\n' && c != EOF);

                goto __no_message;
        }

    }
    return 0;
}

