This guide will be a handy reference point for tools you might want / need for the Beginner CTF and beyond (although its far from exhaustive)  

# General Pointers 
***Make sure to ask for help!*** CTFs are played in teams for a reason, work with your team and feel free to ask the SIGINT members that are around any questions about challenges; We won't solve the challenge for you but we will push you in the right direction and make sure you're working along the right lines and not bashing your head against a wall.

If you are running windows we strongly recommend that you have **WSL** [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) installed on your system as it allows you to run a Linux instance on your machine without needing to dule boot or ever leave windows. It's needed because many CTF challenges may only provide Linux binary's and many tools only provide Linux support (Plus if you're an informatics student you'd need someway to use Linux sooner or later anyway). 

Make sure you have **python installed** and you understand how to program in it and install new packages with pip because it is by far the most common way to create exploits and interact with challenges. 

If you have any issues setting up or have any questions in general feel free to dm `platinumxy` or `emily.747` on discord or ask in the [SIGINT discord server](https://discord.gg/6aTwybA2Wj) for help.


# Web Challenges 
- [PortSwigger's BurpSuite](https://portswigger.net/burp/communitydownload)
    - Allows you to see ***everything*** normally hidden that your browser and server sends between one another 
    - Allows you to send forged requests that normal browsers are unable to produce 
- [Mozilla developer docs](https://developer.mozilla.org/en-US/)
    - Useful checklist for finding things you can use that were missing from filters 
    - Great for reminding yourself on headers or tags you've forgotten
- [cURL](https://curl.se/docs/manpage.html)
    - Command line tool allowing you to quickly send and receive web requests of all kinds
        - Pretty much all attacks you use burp suite for can be done in it though its not as pretty
    - Make sure to use `-vvv` to see full details of what's happening between the request and the response

If you want to practice web exploitation the best place to do it is [Port Swigger Academy](https://portswigger.net/web-security) as it has detailed lessons and labs for most web challenges 

# Reverse Engineering Challenges
- [Binary Ninja](https://binary.ninja/) / [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
    - This will be your bread and butter for converting program binary's into "pesudo C"
    - Both of them can be used however my advice is to learn one well. 
    - For people who've never reversed a binary before I **strongly recommend Binary Ninja**
        - If you know the basics of one don't feel you need to change.  
- JS de-obfuscators 
    - Because of the flexibility JavaScript has it makes it very easy for you to offuscate the behaviour of the code
		- This means that there is tones of different options to encode such as [JSFuck](https://jsfuck.com/)
    - You'll probably have try a few different de-obfuscators before you get some readable code 

If you'd like to see how you can solve some real CTF challenges / push yourself after the beginner CTF have a look at Platinumxys [writeups of ToasterBirb's challenges](https://platinumxy.com/posts/toasterbirb/)

# Pwn Challenges 
- [pwntools](https://github.com/Gallopsled/pwntools) 
    - Allows you to quickly develop exploits for binary's with easy ways to manage the I/O
    - Lets you connect to remote servers over TCP to send exploits
    - Lets you generate shellcode for a target 
- [GDB](https://www.gnu.org/software/gdb/) or [WinGDB](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) for windows
    - Lets you inspect the behaviour of memory and registers of any binary
    - Lets you step though execution and modify behaviour to tests exploits
    - For some basic usage advice have a look at Emily's [guide](https://www.emilymiller.xyz/post/gdb_basics/) 
- [Binary Ninja](#reverse%20engineering%20challenges)
    - A said [above](#Reverse%20Engineering%20Challenges) its critical you've a way to convert the binary into a readable version you can work with 
    - Its important for rev but make especially sure you're confident reading the assembly 

To push yourself further after the CTF [pwn college](https://pwn.college) has tones of lessons and practice for pwn and [Andrej's Notes](https://ir0nstone.gitbook.io) being an excellent reference sheet

# Crypto Challenges 
- [pycryptodome](https://pypi.org/project/pycryptodome/)
    - Its not really a useful tool per se rather its more a mandatory python library if you want to play crypto  
- [Sage Maths](https://www.sagemath.org/)
    - Incredibly powerful language extension for python that allows for complex algebra to be quickly computed 
    - Can solve modular arithmetic, large primes, lattice reduction, and elliptic curves
        - Generally really useful for symbolic solves of calculus and linear algebra questions which will generally help you in any maths course you have to do 
    - Very effective at most CTF crypto attacks like RSA key recovery and discrete logs
- [CryptoHacks Docker Image](https://github.com/cryptohack/cryptohack-docker)
    - Gives you a preconfigured dockerfile for preforming crypto challenges within without cluttering up your host env
    - Includes needed python library's and Sage maths already 

# Miscellaneous Challenges 
- [GCHQ's CyberChef](https://gchq.github.io/CyberChef/)
    - Can be used for most data conversion / manipulations you could ever need
        - Conversions
        - Base encodings
        - Encryption and Decryption 
    - Additionally can often detect possible encodings / file types to help you 
- [dCode.fr](https://www.dcode.fr/en)
    - Has pretty much every cypher under the sun https://www.dcode.fr/tools-list
    - Along with a cipher identifier that can detect a lot of common ciphers https://www.dcode.fr/cipher-identifier 
        - Although don't use it as a crutch as it'll happily give false positives 
- [Google](https://google.com) / [DuckDuckGo](https://duckduckgo.com/)
    - Sounds cliché but it is your best ally in finding new information which is what a misc challenge is at its heart 
    - *When searching things to do with exploits **use DuckDuckGo** as google blocks most hacking related links*
