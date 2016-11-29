# LOL Challenge

## Topics Covered

* LOLCODE

## Tools

* [LOLCODE interpreter](http://www.tutorialspoint.com/execute_lolcode_online.php) 

## Method

Believe it or not, LOLCODE is a real, Turing complete, programming language. 

```
HAI 1.2
   
    HOW IZ I PASSWORD
        FOUND YR ":(73):(69):(67):(69):(6e):(74):(3e):(77):(74):(66):(5f):(77):(61):(73):(5f):(74):(68):(61):(74)"
    IF U SAY SO
    
    
    VISIBLE "ENTER A PASS: "!
    I HAS A ANIMAL
    GIMMEH ANIMAL
    
    BOTH SAEM ANIMAL AN "WTF", O RLY?
    YA RLY
        I HAS A CODE 
        CODE R I IZ PASSWORD MKAY
        CODE IS NOW A YARN 
        VISIBLE CODE
    NO WAI
        VISIBLE "I NOT HAS A CAT, OR DA PASSWD"
    OIC
KTHXBYE
```

This was the challenge code, the astute may have noticed that the numbers in brackets look like ASCII codes. Well they are, but converting those is cheating!!

The important bits are:

```
HOW IZ I PASSWORD
```
and

```   
VISIBLE "ENTER A PASS: "!
    I HAS A ANIMAL
    GIMMEH ANIMAL
```
and 
```
BOTH SAEM ANIMAL AN "WTF", O RLY?
```

The first code example defines the function named "PASSWORD", which returns the flag as text.

The second code example takes user input and saves it in the variable "ANIMAL"

The last code example compares the user input and the string (or YARN in LOLCODE) "WTF", if they match the PASSWORD function is called and the flag is printed. Otherwise the ELSE condition is invoked.

After losing a few brain cells you'll get the flag value:

"sigint>wtf_was_that"
