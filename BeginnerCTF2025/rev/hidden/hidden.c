#include <stdio.h>
#include <string.h>

char expected_flag[0x30] = "SIGINT{this_isnt_the_real_flag:3}\n\x00";
char user_input[0xFF];
int xor_key[0x19] = {0x1c,0x59,0x0d,0x17,0x3a,0x07,0x2c,0x5f,0x1a,0x00,0x43,0x00,0x56,0x00,0x10,0x51,0x02,0x07,0x38,0x14,0x5c,0x14,0x09,0x5e,0x12};


void __attribute__ ((constructor)) init() {
    for (int i = 0; i < 0x19; i++) {
        expected_flag[i + 7] ^= xor_key[i];
    }
}  

void __attribute__ ((destructor)) fini() {
    fgets(user_input, 0xFF, stdin);
    if (strcmp(user_input, expected_flag) == 0) {
        printf("Correct!\n");
    } else {
        printf("Incorrect!\n");
    }

}

char* foo_0() { }
char* foo_1() { }
char* foo_2() { }
char* foo_3() { }
char* foo_4() { }
char* foo_5() { }
char* foo_6() { }
char* foo_7() { }
char* foo_8() { }
char* foo_9() { }
char* foo_10() {  }
char* foo_11() {  }
char* foo_12() {  }
char* foo_13() {  }
char* foo_14() {  }
char* foo_15() {  }
char* foo_16() {  }
char* foo_17() {  }
char* foo_18() {  }
char* foo_19() {  }
char* foo_20() {  }
char* foo_21() {  }
char* foo_22() {  }
char* foo_23() {  }
char* foo_24() {  }
char* foo_25() {  }
char* foo_26() {  }
char* foo_27() {  }
char* foo_28() {  }
char* foo_29() {  }
char* foo_30() {  }
char* foo_31() {  }

int main(){
    printf("WOW, who knew I could do that before main, even if you cant see it...\n");
    printf("Anway, ignoring that let me check your flag:\n");
    return 0;
}