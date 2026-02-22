# Name
YavaScript

# Description
I found this JS hidden in a site that offers "flag verification services". I wonder if there flags are protected enough

# Solve 
Basic Obfuscator.io obfuscation that can be *mostly* reversed using https://obf-io.deobfuscate.io/ to find its preformin an xor with every numeric value upto 0x32 (resulting in a xor key of 1) then comparing to some master value

# Flag 
`SIGINT{0bfu5c4t0r.10_15_4_p41n_1n_th3_4r53}`

