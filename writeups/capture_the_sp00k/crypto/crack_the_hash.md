
# Crack the Hash Challenge

## Topics Covered

MD5 hashing algorithm and hashing tools.

## Tools

* Hashcat or John the Ripper

## Method

This is an MD5 hash of the phrase "sigint>Gr33n_G00se". You won't find this in any online databases, you had to crack the hash using tools like Hashcat or John the Ripper to name two.

Since the start of the hash is known "sigint>" you could use this in a mask to speed things up. As an example using Hashcat you can set a mask that would start all hashes attempts. On my windows machine it would look like:

```
hashcat32.exe --increment -a3 0a977b57d8b82b262ca65268ea28cda3 "sigint>?a?a?a?a?a?a?a?a?a?a?a"
```

Breaking this down, '--increment' is used so that the program consumes the mask one symbol at a time, e.g:

```
s
si
sig
sigi
sigin
sigint
sigint>
sigint>?a
```
So this would check all lengths of the possible flag up to 18 characters.

Since no other information is provided we need to check for all letters (upper and lower), numbers and symbols. Which sounds like a lot, that brings us to...

## An apology

I threw this one in at the last minute to see how if people could manage it, however nobody managed to submit the solution and when testing on my machine after the fact I had an estimated time to complete (even with a mask) of around *11 years*. Yikes.

Next time I'll probably limit it to a dictionary attack or some sort of rule based thing.
