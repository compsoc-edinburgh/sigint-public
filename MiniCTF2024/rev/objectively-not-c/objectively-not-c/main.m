//
//  main.m
//  objectively-not-c
//
//  Created by Artemis Livingstone on 2024-09-07.
//

#import <Foundation/Foundation.h>

#define LEN_OF_KEY 37

// "This could have been a rust challenge"
static const int kurwa[] = {84, 104, 105, 115, 32, 99, 111, 117, 108, 100, 32, 104, 97, 118, 101, 32, 98, 101, 101, 110, 32, 97, 32, 114, 117, 115, 116, 32, 99, 104, 97, 108, 108, 101, 110, 103, 101};

 NSMutableArray * init_stream(void) {
    NSMutableArray * s = [NSMutableArray arrayWithCapacity:256];
    for (int i = 0; i < 256; i++) {
        [s addObject:[NSNumber numberWithInt:(i)]];
    }
     return s;
}

// Key Scheduling
void KSA(NSMutableArray * input) {
    int i = 0;
    for (int j = 0; j < 256; j++) {
        i = (i + [input[j] intValue] + kurwa[j % LEN_OF_KEY] ) % 256;
        [input exchangeObjectAtIndex:i withObjectAtIndex:j];
    }
}

NSMutableArray * stream_generation(NSMutableArray * sched, unsigned long len) {
    int i = 0;
    int j = 0;
    NSMutableArray * stream = [NSMutableArray arrayWithCapacity:len];
    for (int idx = 0; idx < len; idx++) {
        i = (1 + i) % 256;
        j = ([sched[i] intValue] + j) % 256;
        [sched exchangeObjectAtIndex:i withObjectAtIndex:j];
        
        int i_val = [sched[i] intValue];
        int j_val = [sched[j] intValue];
        
        [stream addObject:[NSNumber numberWithInt:[sched[((i_val + j_val) % 256)] intValue]]];
        
    }
    return stream;
}

void chal_encrypt(const char * input) {
    unsigned long input_len = strlen(input);
    unsigned char xor;
    unsigned char x;
    
    NSMutableArray * s = init_stream();
    KSA(s);
    NSMutableArray * stream = stream_generation(s, input_len);
    
    printf("Encrypted output: 0x");
    for (int i = 0; i < strlen(input); i++) {
        x = [stream[i] charValue];
        xor = input[i] ^ x ;
        printf("%02X", xor);
    }
    printf("\n");
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        const char * input = argv[1];
        
        if (input == NULL) {
            NSLog(@"Please enter data");
            return 1;
        }
        // insert code here...
        chal_encrypt(input);
    }
    return 0;
}
